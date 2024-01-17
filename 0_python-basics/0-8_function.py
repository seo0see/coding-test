# 대표적인 함수 예시
def add(a, b):
    return a+b

print(add(3,7)) ##결과: 10


# 동일한 함수를 return문 없이 작성 (함수 안에서 결과까지 출력하도록)
def add (a,b):
    print(3+7)

add(3,7) ### 여기에 print를 씌우면 None이 출력됨.


# 함수 호출에서 argument를 넘길 때, 파라미터의 변수를 직접 지정하여 값 넣기
def add(a,b):
    return a+b

print(add(b=3, a=7))


# 함수에서 global 키워드 사용
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a) ##결과: 10


# Lambda Express (람다 표현식)
print((lambda a,b: a+b)(3,7)) ## 결과: 10