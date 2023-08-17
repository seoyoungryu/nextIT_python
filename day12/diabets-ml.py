from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/taehojo/data/master/pima-indians-diabetes3.csv')
X = df.iloc[:,0:8]
y = df.iloc[:, 8]
clf = svm.SVC(gamma=0.001)
# 데이터 분리
X_train , X_test , y_train, y_test =\
    train_test_split(X, y, test_size=0.5 ,shuffle=False) # test_size 훈련데이터 50% 테스트데이터 50%
clf.fit(X_train,y_train)
# 학습
clf.fit(X_train,y_train)
#예측
predicted = clf.predict(X_test)
ac_score = metrics.accuracy_score(y_test,predicted)
cl_reprot = metrics.classification_report(y_test,predicted)
print(f"정답률 = {ac_score}")
print(f"리포트 = {cl_reprot}")