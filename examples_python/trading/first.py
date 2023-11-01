import yfinance as yf
import matplotlib.pyplot as plt

# Turkcell hisse senedi sembolü
symbol = 'TCELL.IS'

# Verileri indir
data = yf.download(symbol, start='2021-01-01', end='2023-7-14')

# Basit bir al-sat stratejisi
data['SMA_50'] = data['Close'].rolling(window=50).mean()  # 50 günlük hareketli ortalama
data['SMA_200'] = data['Close'].rolling(window=200).mean()  # 200 günlük hareketli ortalama

data['Signal'] = 0
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1  # Al emri ver
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1  # Sat emri ver

# Grafik çizimi
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Turkcell')
plt.plot(data['SMA_50'], label='50 Günlük Hareketli Ortalama')
plt.plot(data['SMA_200'], label='200 Günlük Hareketli Ortalama')

# Al-sat işaretleri
buy_signals = data[data['Signal'] == 1]
sell_signals = data[data['Signal'] == -1]
plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', label='Alış Sinyali')
plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', label='Satış Sinyali')

plt.title('Turkcell Hisse Senedi')
plt.xlabel('Tarih')
plt.ylabel('Fiyat (TRY)')
plt.legend()
plt.grid(True)
plt.show()