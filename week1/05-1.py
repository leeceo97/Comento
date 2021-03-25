# 05-1 클래스
result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

result1 = 0 
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
# 이처럼 클래스는 각각의 객체를 생성하므로 기존에 하던방식처럼 
# 새롭게 값을 저장할때마다 새로운 함수를 생성하지 않아도된다.


# 클래스 예
class Cookie:
    pass
a = Cookie()
b = Cookie()

print("-"*50)
# 사칙연산 클래스 만들기
class FourCal:
    def setdata(self, first, second): # self에는 객체 a가 전달되는것이다 관례적으로 self를 쓸뿐 다른 이름으로 변경가능하다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal() # FourCal.setdata(a,4,2)와 같은 의미지만 잘쓰이지는 않는다.
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print("-"*50)

# 생성자 (Constructor)
class FourCal:
    def __init__(self, first, second):# __init__메서드를 추가하면
        self.first = first
        self.second = second
    def setdata(self, first, second): 
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result