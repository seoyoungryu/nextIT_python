from sklearn import svm, metrics
import os.path, glob, re, json

def check_freq(fname):
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2,}',name).group()

    # with => 파일 입출력 할 때 사용 / "r" : read
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    cnt = [0 for n in range(0, 26)]
    code_a = ord("a") # ord : 문자 "a" 아스키 코드 값 반환
    code_z = ord("z")  # z: 122 a : 97

    for ch in text:
        # ch=> b라면
        n = ord(ch) # b 아스키 코드 값 98
        if code_a <= n <= code_z: # a~z코드 값 사이에 n 있을 때
            cnt[n - code_a] += 1

    total = sum(cnt)
    # 람다식으로 빈도를 리스트로 반환시킴
    freq = list(map(lambda n: n / total, cnt))
    return freq, lang # return(freq, lang) => 튜플형태

# 각 피일 처리하기
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}

data = load_files("../lang/train/*.txt")
test = load_files("../lang/test/*.txt")

with open("../lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)

# 학습
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

#예측
predict = clf.predict(test["freqs"])

#결과
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"],predict)
print(f"정답률 = {ac_score}")
print(f"리포트 = {cl_report}")