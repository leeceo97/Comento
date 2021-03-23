# 02-2 문자열 자료형

# 문자열에 특수문자 쓰기 --> 앞에 백슬래시(\)붙이기
print("\"파이썬 기초다지기\"")

# 이스케이프 코드
# \n: 문자열 안에서 줄을 바꿀 때 사용
# \t: 문자열 사이에 탭 간격을 줄 때 사용
# \ : 특수문자를 쓸때 사용
# \a: 벨 소리(출력할 때 '삑'소리가 난다)

# 문자열도 더하기나 곱하기가 가능하다.
# 문자열 길이 구하기: len()
a = "Life is too short"
len(a)

# 문자열 인덱싱: 문자열 안의 특정한 값을 뽑아내는 역할을 한다.
a = "I am python master"
a[0] # 'I' a[-0]과 동일
a[12] # 'm; a[-6]과 동일

# 문자열 슬라이싱: 문자열 단어채로 뽑아내는 역할을 한다.
a[0:4] # 'I am' 0번째부터 4번째 전까지 추출
a[5:] #'python master' 
a[:] # 전체 문자열 추출

# 문자열 포매팅: 문자열 안에 어떤 값을 삽입하는 방법이다.
# 숫자 바로 대입
'I eat %d apples.' %3 # 'I eat 3 apples.'
# 문자열 바로 대입
'I eat %s apples.' % 'five' # 'I eat five apples.'
# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)