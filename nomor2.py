import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest, norm

# Membaca data dari file CSV
df = pd.read_csv('Walmart.csv')

# Mengambil kolom 'Weekly_Sales' dan 'Fuel_Price'
weekly_sales = df['Weekly_Sales']
fuel_price = df['Fuel_Price']

# Uji normalitas menggunakan uji Kolmogorov-Smirnov (KS)
alpha = 0.05

# Uji normalitas untuk kolom 'Weekly_Sales'

print('Nomor 2\n')

print('2a\n')
statistic, p_value = kstest(weekly_sales, norm.fit(weekly_sales))
print("Uji Normalitas Weekly Sales:")
print(f"Statistic: {statistic}")
print(f"P-value: {p_value}")
if p_value > alpha:
    print("Weekly Sales didistribusikan secara normal")
else:
    print("Weekly Sales tidak didistribusikan secara normal")
print('\n')

# Uji normalitas untuk kolom 'Fuel_Price'
statistic, p_value = kstest(fuel_price, norm.fit(fuel_price))
print("Uji Normalitas Fuel Price:")
print(f"Statistic: {statistic}")
print(f"P-value: {p_value}")
if p_value > alpha:
    print("Fuel Price didistribusikan secara normal")
else:
    print("Fuel Price tidak didistribusikan secara normal")
print('\n')

