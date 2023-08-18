import cv2
import sys

image_file = "photo2.jpg"

# 캐스케이드 파일 =>
cascade_file = "haarcascade_frontalface_alt.xml"

image = cv2.imread(image_file)

image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_file)

face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150,150))

if len(face_list) > 0:
    print(face_list)
    color = (0,0,255)
    for face in face_list:
        x,y,w,h = face # 좌표별로 얼굴 이미지
        cv2.rectangle(image, (x,y), (x+y, y+h),color, thickness=7) #사각형 그리기
    cv2.imwrite(f"{image_file}--facedetect.png", image)
else:
    print("no face")