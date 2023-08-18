import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import ModelCheckpoint, EarlyStopping

df = pd.read_csv("../data/wine.csv", header=None)

X = df.iloc[:, 0:12]
y = df.iloc[:, 12]

X_train, X_test, y_train, y_test = train_test_split(X, y)

# 머신러닝 생성
model = Sequential()
model.add(Dense(30, input_dim=12, activation='relu')) #dense와 activation 합쳐 쓰기
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])

# 학습 자동 중단 설정 / early stopping : 오버피팅이 일어날 것 같으면 학습을 종료 / patience의 값 이상으로 낮아지지 않을 경우 학습 종료
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=20)

# 에포크마다 정확도 출력해보기
# 모델 저장(파일명 : 에포크 번호 - 정확도.hdf5)
model_path = "../data/model/wine/{epoch:02d}--{accuracy:.4f}.hdf5"
check_pointer = ModelCheckpoint(filepath=model_path, verbose=1)

#훈련(epoch 하나 끝날 때 마다 callback 호출)
history = model.fit(X_train, y_train, epochs=2000, batch_size=500, callbacks=[early_stopping_callback, check_pointer], validation_split=0.25)

#history에 저장된 학습 결과 가져오기
hist_df = pd.DataFrame(history.history)
# 검증 데이터셋
y_vloss = hist_df['val_loss']
# 학습 데이터셋의 오차
y_loss = hist_df['loss']

# 그래프 그리기
x_len = np.arange(len(y_loss))
plt.plot(x_len, y_vloss, "o", c="red", markersize=2, label="Testset_loss")
plt.plot(x_len, y_loss, "o", c="blue", markersize=2, label="Trainset_loss")
plt.legend(loc="upper right") # legend : 그래프 좌표값의 상세정보 보임/ 위치를 정할 수 있음
plt.xlabel('epoch')
plt.ylabel('loss')
plt.savefig("wine_overfit")

#결과
score = model.evaluate(X_test, y_test)

print(f"Accuracy : {score[1]}")