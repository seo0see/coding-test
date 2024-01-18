# 실전 문제. 왕실의 나이트

loc = input()
# loc[0] 열(문자) loc[1] 행(수)
n = 8
result = 0

move = [[2,1], [2,-1], [-2, 1], [-2, -1], [-1, 2], [1, 2], [-1, -2], [1, -2]]
for i in move:
    nx_int = ord(loc[0])+i[0]
    ny_int = int(loc[1])+i[1]
    if (ord('a') <= nx_int < ord('a')+n) and (1 <= ny_int < 1+n):
        result += 1

print(result)


## input: a1
## output: 2

## 풀이 중 ord()와 chr() 함수를 검색.

## 답안 예시와 풀이 유사.
## 이동에 대해서 변하지 않는 내용이므로 튜플로 저장하는 것이 더 나았을 듯함.

## '상하좌우' 문제에서는 dx, dy 리스트를 선언하여 이동할 방향을 기록할 수 있도록 하였고, '왕실의 나이트' 문제에서는 steps 변수가 dx와 dy 변수의 기능을 대신하여 수행한다. 2가지 형태 모두 자주 사용되므로 참고.