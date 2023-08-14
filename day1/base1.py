# ^^^^^
# 문자열은 '' or "" 긴문자열 쓸 경우 ''' ''', """ """
# a = "hi"
# print(a)
# print(type(a)) #type 함수는 자료의 타입을 볼 때 사용
# a=1
# print(type(a))
# a=str(a) # to str
# print(type(a))
# a=int(a) # to int
# print(type(a))
from builtins import int

# 동적 배열
arr = [] # 빈 배열
arr.append(1)
arr.append('hi')
arr.append([1,2,3,4])
# print(arr)
# print(arr[2][1]) #2번째의 1번째 데이터
# print('슬라이스 1:3 ->', arr[1:3])
# print(arr * 100)

# 반복문 for(3가지)
# 1. 1값만 필요할 때
for v in arr:
    print(v) #<-- v는 순차적인 배열의 값
# 2. 인덱스값과 value값이 필요할 때
for i, v in enumerate(arr):
    print('idx:', i , 'val:' , v)

# 3. 단순 반복이 필요할 때
for i in range(1, 10):
    print(i)
for i in range(len(arr)): # len -> length
    print(arr[i])

msg = input('숫자를 입력해 주세요 ^^:')
# input의 읿력값은 문자열임
for i in range(int(msg)):
    print(i)