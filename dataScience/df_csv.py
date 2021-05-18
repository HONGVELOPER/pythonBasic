import pandas as pd

iphone_df = pd.read_csv('C:/Users/hyjin/Desktop/iphone.csv', index_col=0)
# read_csv return => DataFrame 

print(iphone_df)
print(type(iphone_df))