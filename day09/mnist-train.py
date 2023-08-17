from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

# 시각화
import matplotlib.pyplot as plt

# data 불러오기
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=10, figsize=(10, 3)) #axes=> 1x10 빈 칸 생성
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title(f"Traing: {label}")

plt.savefig("training")

n_sample = len(digits.images)
data = digits.images.reshape((n_sample, -1)) #숫자 이미지 평면화

# model
clf = svm.SVC(gamma=0.001)

# 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.5, shuffle=True) #digits.target => 레이블(정답 데이터)
# 학습
clf.fit(x_train, y_train)

# 예측
predicted = clf.predict(x_test)

_, axes = plt.subplots(nrows=1, ncols=10, figsize=(10, 3))
for ax, image, label in zip(axes, x_test, predicted):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title(f"Prediction: {label}")
plt.savefig("prediction")
# 결과
result = metrics.classification_report(y_test, predicted)
print(result)