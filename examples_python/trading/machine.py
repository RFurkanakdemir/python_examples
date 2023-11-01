import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Turkcell hisse fiyatlarını yfinance kullanarak al
data = yf.download("TCELL.IS", start="2020-01-01", end="2023-7-14")

# Öznitelikleri oluşturma
data['Close_Diff'] = data['Close'].diff()
data['Target'] = data['Close'].shift(-1)
data.dropna(inplace=True)

# Öznitelikleri ve hedefi ayırma
X = data[['Close_Diff']]
y = data['Target']

# Son gözlemi ayrı bir değişkende saklama
last_observation = X.iloc[[-1]]
last_observation_date = data.index[-1]

# Son gözlemi veri setinden çıkarma
X = X[:-1]
y = y[:-1]

# Eğitim ve test veri setlerini oluşturma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Makine öğrenmesi modelini oluşturma ve eğitme
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Son gözlem için tahmin yapma
next_closing_price = model.predict(last_observation)

print("Tahmin Edilen Bir Sonraki Kapanış Fiyatı (%s): %.2f" % (last_observation_date, next_closing_price))
