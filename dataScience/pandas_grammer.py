import numpy as np
import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91],['yoonsoo', 88, 75]]
my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'english_score', 'math_score'], index=['a', 'b', 'c', 'd'])

print(my_df.dtypes) # 한 컬럼 내에서는 모두 동일한 데이터 타입의 값을 갖는다.

'''
2차원 리스트, numpy array, pandas Series 로 DataFrame 만들기
two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91],['yoonsoo', 88, 75]]
two_dimensional_array = np.array(two_dimensional_list)
# my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'english_score', 'math_score'], index=['a', 'b', 'c', 'd'])
list_of_series = [
    pd.Series(['dongwoook', 50, 86]),
    pd.Series(['dongwoook', 89, 31]),
    pd.Series(['dongwoook', 68, 91]),
    pd.Series(['dongwoook', 88, 75]),
]

df1 = pd.DataFrame(two_dimensional_list)
df2 = pd.DataFrame(two_dimensional_array)
df3 = pd.DataFrame(list_of_series)
'''
'''
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
파이썬 dictionary 로 DataFrame 만들기

names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

dict1 = {
    'name': names,
    'english_score': english_scores,
    'math_score': math_scores
}
dict2 = {
    'name': np.array(names),
    'english_score': np.array(english_scores),
    'math_socre': np.array(math_scores)
}
dict3 = {
    'name': pd.Series(names),
    'english_score': pd.Series(english_scores),
    'math_score': pd.Series(math_scores)
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)
'''

# print(my_df)
# print(type(my_df))
# print(my_df.columns)
# print(my_df.index)
# print(my_df.dtypes)
# print(df1)