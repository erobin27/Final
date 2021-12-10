import pandas as pd;

url = 'https://raw.githubusercontent.com/erobin27/ZillowDashboard/master/rawdata/ListAndSalePrice.csv'
df = pd.read_csv(url,index_col=0)
print(df.head())