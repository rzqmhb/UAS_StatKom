from scipy import stats
import pandas as pd

df = pd.read_csv('Walmart.csv', usecols=['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment'])

print('Nomer 3')
print('3a')
correlation = df[['Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Weekly_Sales']].corr(numeric_only=True)
print("Nilai korelasi antara variabel independen dan variabel dependen:")
print(correlation['Weekly_Sales'])

print('3b')
correlation = df[['Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Weekly_Sales']].corr(numeric_only=True)
negative_correlations = correlation[correlation['Weekly_Sales'] < 0]
negative_correlations = negative_correlations['Weekly_Sales'].drop('Weekly_Sales', errors='ignore')
if negative_correlations.empty:
    print("Tidak ada pasangan variabel independen dan dependen dengan korelasi negatif.")
else:
    print("Pasangan variabel independen dan dependen dengan korelasi negatif:")
    print(negative_correlations)
