# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i%2==1]
print(array) ##결과: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array) ##결과: [1, 4, 9, 16, 25, 36, 49, 64, 81]


# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array) ##결과: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# N X M 크기의 2차원 리스트 초기화(잘못된 방법)
array = [[0] * m] *n
print(array) ##결과: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
array[1][1] = 5
print(array) ##결과: [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]


# 조건부 표현식(Conditional Expression) 사용
a = [1,2,3,4,5,5,5]
remove_set={3,5}

result = []
for i in a:
    if i in a:
        if i not in remove_set:
            result.append(i)
print(result) ##결과: [1, 2, 4]

result = [i for i in a if i not in remove_set]
print(result) ##결과: [1, 2, 4]

