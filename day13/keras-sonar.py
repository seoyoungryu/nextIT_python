import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split #데이터 분리(학습, 테스트 데이터로 자동 분류)

# git clone https://github.com/taehojo/data.git

df = pd.read_csv("../data/sonar3.csv", header=None)

model = Sequential()
model.add(Dense(24, input_dim=60)) #24개 노드, 60개의 dimension
model.add(Activation('relu'))

model.add(Dense(10))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
X = df.iloc[:, 0:60]
y = df.iloc[:, 60]
X_train, X_test, y_train, y_test = train_test_split(X, y)

#훈련
history = model.fit(X_train, y_train, epochs=200, batch_size=10)    # epochs : 전체 데이터셋을 몇 번 반복학습할지 설정, batch_size : 몇 개의 샘플로 가중치를 갱신할 것인지 설정

score = model.evaluate(X_test, y_test)
print(f"Test Accuracy : {score[1]}")
