# 클래스
# python도 객체지향 프로그래밍(OOP)
# 클래스 명은 capwords 방식으로 표시
# 함수, 변수, 속성 - 스네이크 표기볍 abc_def
#  클래스, 예외는 - 파스칼표기법 : 첫 문자 대문자.
class Rectangle:
    count = 0 # 클래스 변수
    #initalizer
    def __init__(self,width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1
    #인스턴스 메소드
    def calcArea(self):
        area = self.width * self.height
        return area
    # 정적 메소드 self 접근할 수 없음
    @staticmethod
    def isSquare():
        print('정적 메소드')
    #클래스 메소드 self 대신 cls 접근
    @classmethod
    def printCount(cls):
        print('클래스 메소드')
        print(cls.count)
    #연산자 오버로딩
    def __add__(self, other):
        obj = Rectangle(self.width + other.width, self.height + other.height)
        return obj
    def __sub__(self, other):
        obj = Rectangle(self.width - other.width, self.height - other.height)
        return obj
#  인스턴스 a
a = Rectangle(5,10)
print(a.calcArea())
Rectangle.isSquare()
Rectangle.printCount()
b = Rectangle(10,10)
c = a + b   # 객체 + 하게 되면 __add__라는 함수를 호출함
d = a - b
print(c.width)
print(d.width)