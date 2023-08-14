#키(key) - 값(value)
param = {} # 비어있는 dict
print(type(param))
param['nm'] = '팽수'
param['age'] = 10
print(param)
param2 = {"nm":"팽수", "age":10}
print(param2)
for key in param2:
    print("key:", key,"val:", param2[key])

# 불변형(immutable), 가변형(mutable)
# python에서 불변형 자료는 : 숫자, 문자열, 튜플
#           가변형 자료는 : array, dict, set
nm = '팽수'
print(id(nm))
nm = '팽팽수'
print(id(nm))
arr = [1,2]
print(id(arr))
arr[0] = 3
print(id(arr))
