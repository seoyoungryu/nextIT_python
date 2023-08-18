from PIL.ImageOps import pad
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPool2D
from sklearn.model_selection import train_test_split
import numpy as np

categories = ["chair", "camera", " butterfly", "elephant", "flamingo"]
nb_classes = len(categories) #5개 카테고리

image_w = 64
image_h = 64

X = np.load("5ojb-X.npy")
y = np.load("5ojb-y.npy")
X_train, X_test, y_train, y_test = train_test_split(X, y)

X_train = X_train.astype("float") / 256
X_test = X_test.astype("float") / 256

print(f"X_train shape:, {X_train.shape}")

#모델구축
model = Sequential()
model.add(Conv2D(32, 3, 3, padding='same', input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25)) # dropout : 학습을 잘하기 위해 불필요한 데이터 제거

model.add(Conv2D(64, 3, 3, padding='same'))
model.add(Activation('relu'))
#model.add(Conv2D(64, 3, 3))
#model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten()) # 하나의 값으로 평평하게 만듦

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=32, epochs=50)

score = model.evaluate(X_test, y_test)
print(f"loss={score[0]}")
print(f"accuracy={score[1]}")