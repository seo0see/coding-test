data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data) ##결과: {'사과': 'Apple', '바나나': 'Banana', '코코넛': 'Coconut'}

# 사전 자료형에 특정한 원소가 있는지 검사
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.") ##결과: '사과'를 키로 가지는 데이터가 존재합니다.

# 키 데이터만 담은 리스트
key_list = data.keys()
print(key_list) ##결과: dict_keys(['사과', '바나나', '코코넛'])
# 값 데이터만 담은 리스트
value_list = data.values()
print(value_list) ##결과: dict_values(['Apple', 'Banana', 'Coconut'])

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key]) #결과: Apple \n Banana \n Coconut