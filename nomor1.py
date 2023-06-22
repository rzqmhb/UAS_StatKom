import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Nomor1():
    def __init__(self):
        print('Nomor 1\n')
        df = pd.read_csv('Walmart.csv', usecols=['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment'])
        store_id = 4
        df_filtered = df[df['Store'] == store_id].copy()  # Buat salinan DataFrame

        # Konversi kolom Fuel_Price, CPI, dan Unemployment menjadi tipe data numerik
        df_filtered['Fuel_Price'] = pd.to_numeric(df_filtered['Fuel_Price'], errors='coerce')
        df_filtered['CPI'] = pd.to_numeric(df_filtered['CPI'], errors='coerce')
        df_filtered['Unemployment'] = pd.to_numeric(df_filtered['Unemployment'], errors='coerce')

        self.df = df
        self.df_filtered = df_filtered

    def calculate_statistics(self):
        print('\n1b\n')

        weekly_sale_stats = self.df_filtered['Weekly_Sales'].describe()
        holiday_flag_stats = self.df_filtered['Holiday_Flag'].describe()
        temperature_stats = self.df_filtered['Temperature'].describe()
        fuel_price_stats = self.df_filtered['Fuel_Price'].describe()
        customer_price_index_stats = self.df_filtered['CPI'].describe()
        unemployment_stats = self.df_filtered['Unemployment'].describe()
        
        weekly_sale_variance = self.df_filtered['Weekly_Sales'].var()
        holiday_flag_variance = self.df_filtered['Holiday_Flag'].var()
        temperature_variance = self.df_filtered['Temperature'].var()
        fuel_price_variance = self.df_filtered['Fuel_Price'].var()
        customer_price_index_variance = self.df_filtered['CPI'].var()
        unemployment_variance = self.df_filtered['Unemployment'].var()

        print("Weekly Sale:")
        print(weekly_sale_stats)
        print("Varians : ",weekly_sale_variance)

        print("Holiday Flag:")
        print(holiday_flag_stats)
        print("Varians : ",holiday_flag_variance)

        print("Temperature:")
        print(temperature_stats)
        print("Varians : ",temperature_variance)

        print("Fuel Price:")
        print(fuel_price_stats)
        print("Varians : ",fuel_price_variance)

        print("Customer Price Index:")
        print(customer_price_index_stats)
        print("Varians : ",customer_price_index_variance)

        print("Unemployment:")
        print(unemployment_stats)
        print("Varians : ",unemployment_variance)
        
        print('\n1c\n')
        fuel_price_q1 = self.df_filtered['Fuel_Price'].quantile(0.25)
        fuel_price_q2 = self.df_filtered['Fuel_Price'].quantile(0.50)
        fuel_price_q3 = self.df_filtered['Fuel_Price'].quantile(0.75)
        fuel_price_iqr = fuel_price_q3 - fuel_price_q1

        cpi_q1 = self.df_filtered['CPI'].quantile(0.25)
        cpi_q2 = self.df_filtered['CPI'].quantile(0.50)
        cpi_q3 = self.df_filtered['CPI'].quantile(0.75)
        cpi_iqr = cpi_q3 - cpi_q1

        unemployment_q1 = self.df_filtered['Unemployment'].quantile(0.25)
        unemployment_q2 = self.df_filtered['Unemployment'].quantile(0.50)
        unemployment_q3 = self.df_filtered['Unemployment'].quantile(0.75)
        unemployment_iqr = unemployment_q3 - unemployment_q1
        
        print("Statistics for Store ID = 4:")
        print("Fuel Price:")
        print("Q1:", fuel_price_q1)
        print("Q2:", fuel_price_q2)
        print("Q3:", fuel_price_q3)
        print("IQR:", fuel_price_iqr)

        print("Customer Price Index:")
        print("Q1:", cpi_q1)
        print("Q2:", cpi_q2)
        print("Q3:", cpi_q3)
        print("IQR:", cpi_iqr)

        print("Unemployment:")
        print("Q1:", unemployment_q1)
        print("Q2:", unemployment_q2)
        print("Q3:", unemployment_q3)
        print("IQR:", unemployment_iqr)
        
        print('\n1d\n')
        grouped_data = self.df.groupby('Holiday_Flag')['Weekly_Sales'].var()
        print("Variance Description:")
        for flag, variance in grouped_data.items():
            if flag == 1:
                print("Holiday Week:")
            else:
                print("Non-Holiday Week:")
            print("Variance:", variance)
            
        print('\n1e\n')
        average_sales_by_store = self.df.groupby('Store')['Weekly_Sales'].mean()
        is_average_sales_equal = average_sales_by_store.nunique() == 1
        if is_average_sales_equal:
            print("Mean untuk Weekly Sales pada toko menunjukkan hasil sama.")
        else:
            print("Mean untuk Weekly Sales pada toko menunjukkan hasil berbeda.")
            
        print('\n1f\n')
        self.df['CPI'] = pd.to_numeric(self.df['CPI'], errors='coerce')  # Konversi tipe data kolom CPI menjadi numerik
        max_cpi_by_store = self.df.groupby('Store')['CPI'].max()
        higher_cpi_by_store = max_cpi_by_store.idxmax()
        print("Store ID dengan nilai CPI tertinggi:", higher_cpi_by_store)
        
        print('\n1g\n')
        average_cpi_holiday = self.df[self.df['Holiday_Flag'] == 1]['CPI'].mean()
        average_cpi_non_holiday = self.df[self.df['Holiday_Flag'] == 0]['CPI'].mean()
        if average_cpi_holiday > average_cpi_non_holiday:
            print("Rata-rata CPI pada holiday week lebih tinggi.")
        elif average_cpi_holiday < average_cpi_non_holiday:
            print("Rata-rata CPI pada non-holiday week lebih tinggi.")
        else:
            print("Rata-rata CPI pada holiday week dan non-holiday week sama.")

# Membuat objek dari class
objek = Nomor1()

# Menghitung statistik
objek.calculate_statistics()
