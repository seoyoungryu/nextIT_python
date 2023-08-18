from PIL import Image
import numpy as np

def average_hash(fname, size=16):
    img = Image.open(fname) #이미지 파일 열기
    img = img.convert('L') #그레이스케일(무채색)으로 변경
    img = img.resize((size,size), Image.ANTIALIAS)

    pixel_data = img.getdata() # 이미지의 픽셀 데이터 가져옴
    pixels = np.array(pixel_data) # => 1차 배열 형태로 담기
    pixels = pixels.reshape((size, size)) # 2차원 배열로 변환하기

    # 0,1로 표현
    avg = pixels.mean()
    diff = 1 * (pixels > avg)
    return diff
    # 픽셀값 리턴
    #return pixels

ahash = average_hash('tower.jpg')
print(ahash)
