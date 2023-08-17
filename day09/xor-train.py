from sklearn import svm

# 1. XOR의 계산 결과 데이터
xor_data = [
    # [P, Q, P xor Q(Label)]
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 데이터 분리(학습을 위한 데이터와 레이블 분리)
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q])
    label.append(r)

# 2. 알고리즘 선택
clf = svm.SVC() #SVC() : 분류시킴

# 3. 학습
clf.fit(data, label)

# 4. 예측 => 학습시킨 label데이터를 기반으로 test 데이터를 삽입해서 테스트 하기
predict = clf.predict(data) # 기존 학습했던 data 데이터로 예측하는 경우
# 테스트에 사용할 데이터
test_data = [
    [0,1],
    [0,0],
    [1,1],
    [1,0],
    [1,1]
]
#predict = clf.predict(test_data)
print(predict)
# 5. 결과
ok = 0 # 맞춘 개수
total = 0 # 전체 개수
for idx, answer in enumerate(label):
    p = predict[idx]
    if p == answer:
        ok += 1
    total += 1
print(f"정답률 = {ok} / {total} = {ok/total}")