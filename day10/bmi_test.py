from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv("bmi.csv")

label = tbl["label"]
w = tbl["weight"] / 100 # weight열에 해당 하는 값
h = tbl["height"] / 200
wh = pd.concat([w,h], axis=1) # 학습데이터 정의 /concat 따로 떨어진 데이터를 붙인다/ axis =1 => 옆으로 붙임 axis = 0 => 세로로 붙임

data_train, data_test, label_train, label_test = train_test_split(wh,label) # 학습데이터 :wh, 정답 데이터 : label

# 학습
clf = svm.SVC()
clf.fit(data_train, label_train)

# 예측
predict = clf.predict(data_test)

# 결과
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print(f"정답률 = {ac_score}")
print(f"리포트 = {cl_report}")