# 04-1 함수

# 선언
def add(a,b):
    #print a+b
    return a+b

a = 3
b = 4
c= add(a,b)
print(c)

# 매개변수와 인수
# 매개변수(parameter): 함수에 입력으로 전달된 값을 받는 변수
# 인수(arguments): 함수를 호출할 때 전달하는 입력값

def add(a,b): # a,b는 매개변수
    return a+b

print(add(3,4)) # 3,4는 인수

# 일반적인 함수의 전형적인 예: 입력값을 받아서 결과값을 돌려준다.
def add(a,b):
    result = a + b
    return result
a = add(3,4)
print(a)

# 입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

# 결과값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add(3,4)

# 입력값도 결괏값도 없는 함수
def say():
    print('Hi')
say()

# 매개변수 지정하여 호출하기
def add(a,b):
    return a+b
result = add(a=3, b=7)
print(result)

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args): # args는 임의로 정한 변수 이름이므로 앞에 *만 붙이면 아무이름이나 사용가능
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add',1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

# 키워드 파라미터 kwargs: 모두 딕셔너리로 만들어준다.
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo',age=3)

# return
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3,4)
print(result1, result2)

# 함수는 return 값을 만나는순간 함수밖으로 값을 반환하므로 return 여러개여도 처음만나는 return 값만을 반환한다.
def add_and_mul(a,b):
    return a+b
    return a*b
result = add_and_mul(2,3)
print(result)

# return의 또 다른 쓰임새 --> 탈출
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." %nick)
say_nick("야호")
say_nick("바보")

# 매개변수에 초깃값 미리 설정하기
def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다."%old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용",27) # 3번째 인수를 주지않았지만 초깃값 True를 갖게되어 아래와 동일하게 출력된다.
say_myself("박응용",27,True) 
say_myself("박응선",27,False)

#def say_myself(name, man=True, old):
#    print("나의 이름은 %s입니다."%name)
#    print("나이는 %d살입니다."%old)
#    if man:
#        print("남자입니다.")
#    else:
#        print("여자입니다.")
# say_myself("박응용",man,27) 
# 이럴경우 파이썬 인터프리터는 27을 man변수와 old변수 중 어느 곳에 대입해야 할지 알수없으므로 오류가 발생한다.
# 그러므로 초기화 시키고 싶은 매개변수는 항상 뒤쪽에 놓는 것을 잊지 말자!

# 함수 안에서 선언한 변수의 효력 범위
# 함수 안에서 선언한 함수만의 변수이기때문에 1이 출력된다.
a =1 
def vartest(a):
    a = a+1
vartest(a)
print(a)


def vartest(a):
    a = a+1
vartest(3)
print(a)
# 오류가 발생한다. 그이유는 출력때 담아야할 변수 a가 선언되지 않았기 떄문이다.

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a = a+1
    return a
a = vartest(a)
print(a)

# 2. global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a+1
vartest()
print(a)
# But 사용하는건 지양하도록...


#lambda
# lambda는 함수를 생성할때 사용하는 예약어로 def와 동일한 역할을 담당한다.
# def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할수 없는곳에 사용된다.

add = lambda a, b: a+b
result = add(3,4)
print(result)