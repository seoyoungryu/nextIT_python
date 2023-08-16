# pip install easyocr
# pip install opencv-python
import easyocr
import cv2
#  이미지 릭기
image = cv2.imread('./img/test1.png')
# easyocr 생성
reader = easyocr.Reader(['en'])
# 텍스트 추출
result = reader.readtext(image)
# 결과 출력
for bbox, text, prob in result:
    # print(f'Text:{text}, BBox:{bbox},prob:{prob}')
    print(text)