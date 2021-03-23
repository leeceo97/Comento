# 02-5 딕셔너리 자료형
# 딕셔너리 자료형(순서X, 중복X, 수정O, 삭제O)

# 선언
dic ={'name':'pey', 'phone':'01051920394', 'birth':'1118'}
# key값은 문자열뿐만아니라 정수 값도 가능하다. value는 리스트도 넣을수 있다.

# 추가
dic['sex':'male'] #{'name':'pey', 'phone':'01051920394', 'birth':'1118', 'sex':'male'}

# 삭제
del dic['name']

# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey'] # 10
grade['julliet'] # 99

# 주의사항
# 딕셔너리에서 key는 고유한 값이므로 중복되는 key값 설정x 가장 최근의 value값이 설정됨

# Key 리스트 만들기
a = {'name': 'pey', 'phone': '01051972093', 'birth': '0211'}
a.keys() # dict_keys(['name','phone','birth'])

# Value 리스트 만들기(values)
a.values() # dict_values(['pey','01051972093','0211'])

# Key,Value 쌍 얻기(items)
a.items() #dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

