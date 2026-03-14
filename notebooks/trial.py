# import pandas as pd

# df = pd.read_csv('./data/raw/eagle_i/eaglei_outages_2014.csv')

# print(df[(df['state'] == 'Texas') & (df['customers_out'] == 0)].head(50))

import pandas as pd

df23 = pd.read_csv('data/raw/eagle_i/eaglei_outages_2023.csv', nrows=1000)
print(df23.columns.tolist())
print(df23.dtypes)
print(df23.describe())
