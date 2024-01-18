# 예제 4-1. 상하좌우

n = int(input())
plan = list(input().split())

result = [1,1]


move = {'L':[0,-1], 'R':[0,1], 'U':[-1,0], 'D':[1,0]}

for i in plan:
    a1 = result[0] + move[i][0]
    a2 = result[1] + move[i][1]
    # if a1 >=1  and a1 <= n and a2 >= 1 and a2 <= n:
    if (0 < a1 <= n) and (0 < a2 <= n):
        result[0] = a1
        result[1] = a2

print(result)


## input: 5 \n R R R U D D
## output: 3 4

## 답안에서는 x,y를 따로 정의하고, 이동에 대해서도, x, y에 대해서 리스트로 만들었으며, 리스트 내의 인덱스를 기반으로 이동을 정

## 이동 횟수가 N번인 경우, 시간 복잡도는 O(N)
##이 문제를 요구사항대로 구현하면 연산 횟수는 이동 횟수에 비례하게 됨.
## 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션(Simulation) 유형으로 분류되며 구현이 중요한 대표적인 문제 유형.

