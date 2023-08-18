import cv2
import sys

image_file = "photo1.jpg"

# 캐스케이드 파일 =>
cascade_file = "haarcascade_frontalface_alt.xml"

image = cv2.imread(image_file)

image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_file)

face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150,150))

if len(face_list) > 0:
    print(face_list)
    color = (0, 0, 255)
    for face in face_list:
        x, y, w, h = face # 좌표별로 얼굴 이미지
        face_img = image[y:y+h, x:x+w] #y~y+h x~x+w까지 이미지 자르기
        face_img = cv2.resize(face_img, (w//30, h//30)) #확대
        face_img = cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
        image[y:y+h, x:x+w] = face_img

    cv2.imwrite(f"{image_file}--mosaic.png", image)
else:
    print("no face")