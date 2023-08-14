# set : 중복없이 유니크한 값만 얻고자 할 때
my_set = {1,2,2,3,4,5,5}
print(my_set)
my2_set =set()
print(type(my2_set))
my2_set.add(1)
my2_set.update({4,2,10}) #여러개 추가
print(my2_set)
# 교집합
a = my_set & my2_set
print(a)
# 합집합
b = my_set | my2_set
print(b)
# 차집합
c = my_set - my2_set
print(c)