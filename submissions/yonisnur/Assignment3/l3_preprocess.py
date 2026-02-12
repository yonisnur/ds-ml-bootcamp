import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 1. Load & inspect (issues identified)
csv_path = pd.read_csv('car_l3_dataset.csv')
df = csv_path
print(df.head())
print(df.info())
print(df.describe())

# missing value
print(df.isnull().sum())

# 2. Clean target formatting 
df['Price'] = df['Price'].replace(r'[$,]','',regex=True).astype(float)

# 3. Fix categorical issues
df['Location'] = df['Location'].replace({'Subrb':'Suburb', '??': pd.NA})

# 4. Impute Missing Values (justify choices) 
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])


# 5 Remove Duplicates — report shape before/after and rows removed.
print(df.head(10))

before = df.shape
print(before)
df = df.drop_duplicates()
after = df.shape
# print(f'Remove duplicate data {before} ---> {after}')

# 6. Outliers (IQR capping)
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_km, high_km = iqr_fun(df['Odometer_km'])
# print(low_price,high_price)
# print(low_km,high_km)

df['Price'] = df['Price'].clip(lower=low_price, upper=high_price)
df['Odometer_km'] = df['Odometer_km'].clip(lower=low_km, upper=high_km)

# 7. One-hot encode categorical variables
df = pd.get_dummies(df,columns=['Location'], drop_first= False, dtype='int')

# 8. Feature engineering

curent_year = 2026
df['CarAge'] = curent_year - df['Year']


df['Km_per_year'] = (df['Odometer_km'] / df['CarAge'])
df['is_urban'] = df['Location_City']
df['Log_Price'] = np.log1p(df['Price'])
 

 # 9. Feature Scaling (X only) 
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.to_list()
scale_cols = [col for col in numeric_cols if col not in dont_scale]
scaler = StandardScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])


# 10. Final Checks & Save
df.info()
df.isnull().sum()
df.describe()

output_path = 'car_l3_dataset_cleaned.csv'
df.to_csv(output_path, index=False)
print(f"Cleaned dataset saved to {output_path}")