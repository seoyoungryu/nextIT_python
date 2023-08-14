import random #라이브러리 임포트
# import requests #사용시 터미널 열어서 pip install requests
com = random.randint(1,10) # 1~10 랜덤값
print(com)

while True:
    msg = int(input('숫자 맞추기!! 1~10값을 입력하세요 : '))
    #  조건문
    if com == msg:
        print('맞았음!!')
        break
    else:
        print('틀렸음')
        if com > msg:
            print('힌트 : ', 'up')
        elif msg > 10:
            print('10이하로 입력하세요!!')
        else:
            print('힌트 : ', 'down')