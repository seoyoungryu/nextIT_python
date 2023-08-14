import random
def make_lotto(num):
    result = []
    #num의 수 만큼 lotto 번호를 생성하여 리턴하는 함수.
    for i in range(num):
        make_num = set()
        while len(make_num) < 6:
            make_num.add(random.randint(1, 45))
        result.append(make_num)
    return result

# 모듈 자체 실행 시 true
if __name__=='__main__':
    print('모듈 자체 실행')
    lotto_num = make_lotto(3)
    print(lotto_num)
else:
    print('import 했음.')