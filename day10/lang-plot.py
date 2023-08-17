import matplotlib.pyplot as plt
import pandas as pd
import json

#  알파벳 출현 빈도 fp (배열)
with open("../lang/freq.json","r",encoding="utf-8") as fp:
    freq = json.load(fp)

lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]):
    fq = freq[0]["freqs"][i]
    if not(lbl in lang_dic):
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) / 2

asclist = [[chr(n) for n in range(97, 97 + 26)]] # 97(a) 부터 아스키코드 값 끝번(z)까지 반복문으로 chr(n)으로 담기 => 알파벳으로 담김
df = pd.DataFrame(lang_dic, index=asclist)

plt.style.use('ggplot')
df.plot(kind="bar", subplots=True, ylim=(0, 0.15))
plt.savefig("lang-plot")