import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def compute_rsi(data, window=14):
    close_prices = data.values
    deltas = np.diff(close_prices)
    seed = deltas[:window+1]
    up = seed[seed >= 0].sum() / window
    down = -seed[seed < 0].sum() / window
    rs = up / down
    rsi = np.zeros_like(close_prices)
    rsi[:window] = 100.0 - (100.0 / (1.0 + rs))

    for i in range(window, len(close_prices)):
        delta = deltas[i-1]  # i-1 because the diff is 1 shorter
        if delta > 0:
            upval = delta
            downval = 0.0
        else:
            upval = 0.0
            downval = -delta

        up = (up * (window - 1) + upval) / window
        down = (down * (window - 1) + downval) / window
        rs = up / down
        rsi[i] = 100.0 - (100.0 / (1.0 + rs))

    return rsi

# Türkcell hissesinin verilerini yükleme
data = yf.download('TCELL.IS', start='2022-01-01', end='2023-07-14')

# Veri setini işleme
data['Return'] = data['Close'].pct_change()
data.dropna(inplace=True)

# Özelliklerin oluşturulması
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()
data['RSI'] = compute_rsi(data['Close'], 14)

# Hedef değişkenin oluşturulması
data['Target'] = data['Close'].shift(-1)
data.dropna(inplace=True)

# Özellikler ve hedef değişkenin ayrılması
X = data[['SMA_50', 'SMA_200', 'RSI']]
y = data['Target']

# Veri setinin eğitim ve test olarak bölünmesi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Doğrusal regresyon modelinin eğitimi
model = LinearRegression()
model.fit(X_train, y_train)

# Test veri seti üzerinde tahmin yapma
y_pred = model.predict(X_test)

# Tahminlerin grafik üzerinde gösterilmesi
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Gerçek Değerler')
plt.plot(y_pred, label='Tahminler')
plt.xlabel('Gün')
plt.ylabel('Fiyat')
plt.title('Doğrusal Regresyon ile Al-Sat Tahminleri')
plt.legend()
plt.show()

# En son tahminin tarihini belirterek konsola yazdırma
latest_date = X_test.index[-1]
latest_prediction = y_pred[-1]
print(f"En son tahmin ({latest_date}): {latest_prediction}")
