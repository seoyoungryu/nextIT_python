# 경로, 파일명을 입력받아
# 파일을 찾고 경로를 출력하는 함수를 만드시오
import os
from builtins import input


def fn_search(filename, path='/'): #경로가 없으면 전체에서 검색
    print('찾았습니다')
    dir = os.path.abspath(path)
    for dirpath, dirnames, filenames in os.walk(dir):
        for file in filenames:
            #contains
            if filename in file:
                print(dirpath + "/" + file)

if __name__ == '__main__':
    path = input('탐색 경로 입력:')
    nm = input('찾고자 하는 파일명 입력:')
    fn_search(nm,path)