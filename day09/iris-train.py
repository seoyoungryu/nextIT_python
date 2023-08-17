import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 파일 읽어오기
csv = pd.read_csv('iris.csv')

#필요한 열 추출
csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_label = csv["Name"]

train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

#머신러닝 model
clf = svm.SVC()
#학습
clf.fit(train_data, train_label)

#예측
predict = clf.predict(test_data)

#결과
ac_score = metrics.accuracy_score(test_label, predict)
print(f"정답률 = {ac_score}")