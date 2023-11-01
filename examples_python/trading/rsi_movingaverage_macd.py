import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Turkcell hisse senedi sembolü
#symbol = 'KONTR.IS'
symbol = "TCELL.IS"
#symbol = "A1CAP.IS"
#symbol ="ASELS.IS"
# Verileri indir
data = yf.download(symbol, start='2020-01-01', end='2023-7-14')

# Hareketli Ortalama (Moving Average) stratejisi
data['SMA_50'] = data['Close'].rolling(window=50).mean()  # 50 günlük hareketli ortalama
data['SMA_200'] = data['Close'].rolling(window=200).mean()  # 200 günlük hareketli ortalama

# RSI (Relative Strength Index) stratejisi
delta = data['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
data['RSI'] = 100 - (100 / (1 + rs))

# MACD (Moving Average Convergence Divergence) stratejisi
data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = data['EMA_12'] - data['EMA_26']
data['Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

# Al-sat işaretleri
data['SMA_Signal'] = np.where(data['SMA_50'] > data['SMA_200'], 1, -1)
data['RSI_Signal'] = np.where(data['RSI'] > 70, -1, np.where(data['RSI'] < 30, 1, 0))
data['MACD_Signal'] = np.where(data['MACD'] > data['Signal'], 1, -1)

# Ortak al-sat sinyalleri
data['Signal_Crossover'] = np.where((data['SMA_Signal'] == data['RSI_Signal']) & (data['RSI_Signal'] == data['MACD_Signal']), data['SMA_Signal'], 0)

# Grafik çizimi
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Turkcell')
plt.plot(data['SMA_50'], label='50 Günlük Hareketli Ortalama')
plt.plot(data['SMA_200'], label='200 Günlük Hareketli Ortalama')

# Alış ve satış sinyallerini gösterme
buy_signals = data[data['Signal_Crossover'] == 1]
sell_signals = data[data['Signal_Crossover'] == -1]
plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', label='Alış Sinyali')
plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', label='Satış Sinyali')

plt.title('Turkcell Hisse Senedi')
plt.xlabel('Tarih')
plt.ylabel('Fiyat (TRY)')
plt.legend()
plt.grid(True)
plt.show()
