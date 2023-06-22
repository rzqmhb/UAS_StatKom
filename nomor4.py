from scipy.stats import kstest, norm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Walmart.csv', usecols=['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment'])

# Mengambil data yang diperlukan
data = df[['Fuel_Price', 'Weekly_Sales']]

# Pisahkan variabel independen (X) dan dependen (y)
X = data[['Fuel_Price']]
y = data['Weekly_Sales']

# Inisialisasi model regresi linear
model = LinearRegression()

# Melatih model menggunakan data
model.fit(X, y)

# Prediksi nilai y berdasarkan X
y_pred = model.predict(X)

# Menampilkan scatter plot data
plt.scatter(X, y, color='blue', label='Data')

# Menampilkan garis regresi
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')

# Menampilkan label dan judul pada grafik
plt.xlabel('Fuel_Price')
plt.ylabel('Weekly_Sales')
plt.title('Linear Regression')

# Menampilkan legenda
plt.legend()

# Menampilkan grafik
plt.show()