# 재귀함수를 100번 호출하도록 하기

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1 ,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)



