import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mr = pd.read_csv("mushroom.csv", header=None)

label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    label.append(row[0])

    row_data = []
    for col, v in enumerate(row[1:]):
        if row_index == 0:
            attr = {"dic": {}, "cnt" : 0}
            attr_list.append(attr)
        else:
            attr = attr_list[col]

        #버섯의 특징 기호를 배열로 나타내기
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        row_data += d
    data.append(row_data)

data_train, data_test, label_train, label_test = train_test_split(data, label)

# 학습
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# 예측
predict = clf.predict(data_test)

#결과
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print(f"정답률= {ac_score}")
print(f"리포트= {cl_report}")
