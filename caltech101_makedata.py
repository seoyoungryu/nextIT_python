from PIL import Image
import glob
import numpy as np
from sklearn.model_selection import train_test_split

caltech_dir = "101_ObjectCategories"
categories = ["chair", "camera", " butterfly", "elephant", "flamingo"]
nb_classes = len(categories) #5개 카테고리

image_w = 64
image_h = 64
pixels = image_w * image_h * 3 # RGB 3개

X = [] # 학습할 데이터
y = [] # 레이블 데이터(카테고리 폴더 명)
for idx, cat in enumerate(categories):
    label = [0 for i in range(nb_classes)] # [ 0 0 0 0 0 ]
    label[idx] = 1

    image_dir = f"{caltech_dir}/{cat}"
    files = glob.glob(f"{image_dir}/*.jpg")
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)
        X.append(data)
        y.append(label)
        if i % 10 == 0:
            print(i, "\n", data)

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)
xy = (X_train, X_test, y_train, y_test)
np.save("5ojb-X.npy", X)
np.save("5ojb-y.npy", y)

print(f"ok,{len(y)}")