# 실전 문제. 게임 개발

n, m = map(int, input().split())
a, b, d = map(int, input().split())
# 여기서는 위치의 정의에 따라, 위치 보정해줄 필요가 없음.
# d - 왼쪽으로 돌면 방향 -1. 0에서 -1을 하게 되면 3이 되도록 하기.
map = [list(map(int, input().split())) for _ in range(n)]

move = {0:(0,-1), 1:(-1,0), 2:(0,1), 3:(1,0)} # 해당 방향을 바라볼 때, 가능한 움직임.
count = 1
map[a][b] = 2 # 현재 위치 방문 처리

# 시뮬레이션 시작
while True:
    # 네 방향 다 봤는지 체크용
    chance=4
    for i in range(4):
        chance -= 1
        # 왼쪽이 비었는지 탐색하기
        new_x = a+move[d][0]
        new_y = b+move[d][1]
        # print(new_x, new_y, "/d", d, "/ 그 자리:", map[new_x][new_y])
        # 방향 바꾸기
        if d >= 1:
            d -= 1
        else:
            d = 3
        if map[new_x][new_y] == 0:
            break
    # 네 방향 다 봤는데, 해당이 안되면 뒤로 가기
    if chance == 0:
        # 가는 방향이 바다이면 종료
        if map[new_x][new_y] == 1:
            break
        a = a+move[d+1][0]
        b = b+move[d+1][1]
        continue
    # 이동하기
    if map[new_x][new_y] == 0:
        a = new_x
        b = new_y
        map[a][b] = 2 # 가 본 칸으로 처리
        count += 1
        # print("이동", a,b)

print(count)


## input: 4 4 \n 1 1 0 \n 1 1 1 1 \n 1 0 0 1 \n 1 1 0 1 \n 1 1 1 1
## output: 3

## 풀기 너무 어려웠던 문제. 너무 오래 걸렸고, 한 번에 작성하는 것으로는 틀렸던 문제. 계속 확인하는 작업이 필요했음.
##또한, 처음 위치에 대해 방문 처리를 안함.
##if문으로 확인할 때, 꼭 자료형 확인하기!

## 답안 예시와 유사하지만 조금 차이나는 풀이
##답안에서는 어차피 회전을 하면 그 방향으로 이동하기에 바라보고 있는 방향과 이동방향을 같게 정의하고, 나는 바라보고 있는 방향에 따른 이동방향을 문제 정의에 따라 (둘이 서로 다르게) 정의
##답안에서는 방향에 따른 이동 지침을 x,y 좌표별로 각각 list로 만들었고, 나는 dictionary로 만듦.
##답안에서는 회전에 대하여 함수를 따로 정의하였으며, global 키워드 사용. 나는 어차피 재사용되지도 않으니 그냥 코드 안에 집어넣음.
##답안에서는 방문한 칸을 저장하기 위한 list를 새로 짰는데, 나는 바다와 육지가 구분되어 있으니 맵 정보를 가진 list에 그 정보를 다른 표현 방식으로 덮어씌움.
##★답안에서 확인 횟수를 while문 하나 안에서 모든 것을 진행하고 회전 횟수를 따로 확인함. 나는 반복문을 중첩함. 쓸데없는 중첩이었던 듯. <- 이건 답안 풀이가 더 좋은 듯.

## 전형적인 시뮬레이션 문제


