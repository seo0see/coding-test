# 예제 3-3. 숫자 카드 게임

n,m = map(int, input().split())
card = [list(map(int, input().split())) for _ in range (n)]
row_min = [0]*n

for i in range(n):
    row_min[i] = min(card[i])
print(max(row_min))


## input: 3 3 \n 3 1 2 \n 4 1 4 \n 2 2 2
## output: 2
## input: 2 4 \n 7 3 1 8 \n 3 3 3 4
## output: 3

## min() 함수를 이용하는 답안 예시와 유사하나,
##답안은 입력을 반복문으로 받음과 동시에 계산을 수행하였고,
##나는 입력을 다 받고, 최솟값을 계산 및 정리하여 그 중 최댓값을 구함.
##공간효율성, 시간효율성 면에서 모두 답안이 더 나은 듯.

## 답안 발상: 각 행마다 가장 작은 수를 찾은 뒤에 그 중에서 가장 큰 수를 찾는다.

