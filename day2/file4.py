import os
path = './' #현재 폴더
# filename = 'file1.py'
filename = 'delay' #delay라는 키워드를 가진 파일
dir = os.path.abspath(path)
for dirpath, dirnames, filenames in os.walk(dir):
    #print(dirpath, dirnames, filenames)
    for file in filenames:
        # if file == filename:
        #     print(dirpath, filename)
        if filename in file:
            print(dirpath, file)
            msg = input('찾는 파일이 맞나요?(y/n')
            if msg == 'y':
                break