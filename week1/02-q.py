# Q1
Hong= {'국어':80, '영어':75, '수학':55}
print(Hong)
score = Hong['국어'] + Hong['영어'] + Hong['수학']
avg = score/3
print(avg)

# Q2
# 13을 2로 나누면 1이나오므로 홀수이다. 이와같이 2로 나누었을때 0인지 1인지 판별하는 조건을 붙여 구별한다.

# Q3
a = '881120-1068234'
print('앞부분:', a[0:6])
print('뒷부분:', a[7:])

# Q4
pin = "881120-1068234"
print(pin[7])

# Q5
a = "a:b:c:d"
print(a.replace(':','#'))

# Q6
c = [1,3,5,4,2]
c.sort()
print(c)

# Q7
a = ['Life', 'is', 'too', 'short']
print(' '.join(a))

# Q8
a = set([1,2,3])
b= set([4])
print(a.union(b))

# Q9
# 3번이 정답이다. 그 이유는 딕셔너리의 키 값은 리스트형태가 나오면 안되기 때문이다.

# Q10
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))

# Q11
a = set([1,1,1,2,2,3,3,3,4,4,5])
print(a)

# Q12
# a와 같이 b의 2번째값이 2에서4로 바뀐다. 그 이유는 a=b라고 선언을 했기때문에 변수 a와b는 이름만 다를뿐 완전 동일한 함수이며 id값또한 같기 때문이다.
