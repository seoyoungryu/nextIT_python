from sklearn import svm, metrics
import pandas as pd

# 1. 데이터
xor_input = [
    # [P, Q, P xor Q(Label)]
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.loc[:, 0:1] # 데이터
xor_label = xor_df.loc[:, 2] # 레이블

# model
clf = svm.SVC()

# 학습
clf.fit(xor_data, xor_label)

#predict
predict = clf.predict(xor_data)

#result
ac_score = metrics.accuracy_score(xor_label,predict) #정확도 측정(레이블 값과 예측한 값 비교)
print(f"정답률={ac_score}")