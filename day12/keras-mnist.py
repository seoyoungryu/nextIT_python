from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.utils import np_utils

# MNIST 데이터 읽어 들이기
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.res