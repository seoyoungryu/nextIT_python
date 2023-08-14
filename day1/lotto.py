# 사용자에게 숫자를 입력받아
# 입력받은 수 만큼 로또 번호를 생성(출력)해주세요
# 로또 번호는 1 ~ 45 숫자의 6자리
# ex2를 입력받으면 6자리 2개 출력
import random

# 랜덤함수, input, 조건 ,반복문 활용

msg = input('몇 개 생성할까요?:')
for i in range(int(msg)):
    lotto = set()
    while len(lotto) < 6:
        lotto.add(random.randrange(1, 46))
        print(i + 1, "번 째 생성 번호 ", lotto)

msg = input('몇 개 생성할까요?:')
for i in range(int(msg)):
    lotto = set()
    while len(lotto) < 6:
        lotto.add(random.randint(1, 45))
        print(i + 1, "번 째 생성 번호 ", lotto)