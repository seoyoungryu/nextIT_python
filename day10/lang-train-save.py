import joblib
from sklearn import svm
import json

with open("../lang/freq.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)
    data = d[0]

# 학습
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 학습 데이터 저장
joblib.dump(clf, "freq.pkl")
print("ok")
