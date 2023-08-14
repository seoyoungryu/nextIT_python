import os
print(os.getcwd()) #현재 경로
path = os.getcwd() + "/files"
file_list = os.listdir(path) # 현재 위치 경로의 파일에 접근
for file_nm in file_list:
    # 파일이 존재하면 true
    file_path = path + "/" + file_nm
    if os.path.exists(file_path):
        print(file_nm)
    if os.path.isdir(file_path):
        print('디렉토리')
        os.rmdir(file_path) #폴더 삭제
    if os.path.isfile(file_path):
        print('파일임')
        os.remove(file_path) #파일 삭제