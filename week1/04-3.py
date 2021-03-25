# 04-3 파일 읽고 쓰기
f = open("새파일.txt",'w')
f.close()
# 파일 열기 모드 종류
# r: 읽기모드-파일을 읽기만 할 때 사용
# w: 쓰기모드-파일에 내용을 쓸 때 사용
# a: 추가모드-파일의 마지막에 새로운 내용을 추가 시킬 때 사용

# C:/doit 디렉터리에 새파일을 생성하고 싶을때 작성법
#f = open("C:/doit/새파일.txt", 'w')
#f.close() # 이문장은 생략 가능하지만 쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생하기 때문에 사용하는게 좋다.

# 파일을 쓰기 모드로 열어 출력값 적기
f = open("새파일.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
# readline()함수 이용하기
# 첫줄만 출력
f = open("새파일.txt",'r')
line = f.readline()
print(line)
f.close()

# 모든줄 출력
# 첫번째 방법: 반복문 무한루프사용
f = open("새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 두번째 방법: readlines함수 사용하기
f = open("새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# 세번째 방법: read함수 사용하기
f = open("새파일.txt",'r')
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
# 'a'
f = open("새파일.txt",'a')
for i in range(11,20):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)
f.close()

f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# with문과 함께 
# with문을 사용하면 close가 자동실행되므로 f.close()를 사용하지 않아도 된다.
f = open("foo.txt",'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

f = open("foo.txt",'r')
data = f.read()
print(data)
f.close()

#sys 모듈로 매개변수 주기
import sys

args = sys.argv[1:]
for i in args:
    print(i)