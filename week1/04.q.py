# Q1
def is_odd(n):
    if n%2==0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")
print(is_odd(2))

# Q2
def avg(*args):
    sum = 0
    for i in args:
        sum += i
    return sum/len(args)

print(avg(3,3,3))

# Q3
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))
total = input1 + input2
print("두 수의 합은 %d 입니다." % total)    

# Q4
# 3번: ,는 띄어쓰기가 되므로 you need python으로 출력된다.

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
data = f2.read()
print(data)
f2.close()

# Q6
c = input("문장을 입력하세요: ")
f = open("test2.txt",'w')
data = f.write(c)
f.close()

# Q7
f = open("test3.txt", 'w')
data = f.write("Life is too short\n you need java")
f.close()

f = open("test3.txt", 'r')
data = f.read()
print(data)
f.close()

mod_data = data.replace('java','python')

f = open("test3.txt",'w')
data = f.write(mod_data)
f.close()

f = open("test3.txt",'r')
data = f.read()
print(data)
f.close()