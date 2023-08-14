import pandas as pd

# pandas의 기본형태는 dataframe
df = pd.DataFrame({"name" : ["nick","judy","jack"]
                   ,"age":[10, 15, 20]})
print(df.head()) #내용 출력 기본 5행
df['age_plus'] = df['age'] + 1
df['age_squared'] = df['age'] * df['age']
df['over_15'] = df['age'] > 15
print(df.head()) #내용 출력 기본 5행
total = df['age'].sum()
print(total)
# 데이터 기본정보(null여부, 데이터 형식)
print(df.info())
# 데이터 기초통계량
print(df.describe())
# 함수 적용 가능
df['age'] = df['age'].apply(lambda x : x * x)
# join
df2 = pd.DataFrame({"name":["nick", "judy", "jack"]
                    ,"height":[180, 165, 187]
                    ,"gender":["M","F","M"]})
joined = df.set_index("name").join(df2.set_index("name"))
print(joined.head()) #dataFrame 데이터 출력(기본 5행 출력)
# group by
print(joined.groupby('gender').mean())