import os.path

import joblib

# os.path.dirname(__file__) 현재 파일 폴더
pkl_file = os.path.dirname(__file__) + "/freq.pkl"
clf = joblib.load(pkl_file)

def detect_lang(text):
    text = text.lower() #소문자로 변경
    code_a, code_z = (ord("a"), ord("z"))
    cnt = [0 for i in range(26)] #a 부터 z까지 카운팅
    for ch in text:
        n = ord(ch) - code_a
        if 0 <= n < 26:
            cnt[n] += 1
    total = sum(cnt)
    if total == 0:
        return "입력이 없습니다"
    freq = list(map(lambda n:n / total, cnt)) # 알파벳 출현 빈도 구하기
    # 언어 예측
    res = clf.predict([freq])
    lang_dic = {"en" : "영어", "fr": "프랑스어", "id":"인도네시아어","tl":"타갈로그어"}
    return lang_dic[res[0]]

unknown_lang="""
        Ce jour-là, Park Seong-woong a révélé l'histoire secrète qui est devenue une échelle super luxueuse lorsque Bae Yong-joon, "Yonsama", est apparu dans un hélicoptère lors de son mariage. Il a dit: "Le lieu du mariage était à Hongcheon. Il y a quelques jours, un appel téléphonique est venu et a demandé:" Y a-t-il une piste d'atterrissage pour hélicoptère sur le lieu du mariage? Park Seong-woong a déclaré: "J'ai pris un hélicoptère à 2 heures, j'ai pris des photos avec la mariée pendant 30 minutes et je suis retourné à Cheongju en hélicoptère."
    """
print(detect_lang(unknown_lang))