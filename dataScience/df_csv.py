import pandas as pd

iphone_df = pd.read_csv('C:/Users/hyjin/Desktop/iphone.csv', index_col=0)
# index_col = 0 => index 의 column 을 row의 0번째 데이터를 index 로 해달라는 뜻이다.
# read_csv return => DataFrame 

print(iphone_df)
print(type(iphone_df))
# print(iphone_df.loc['iphone', '메모리'])

