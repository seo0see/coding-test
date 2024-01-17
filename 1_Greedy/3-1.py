# 예제 3-1. 거스름돈
N=1260

last = N
coin_type = [500, 100, 50, 10]
count = 0
for i in coin_type:
    count += last//i
    last = last%i #(last//i)*i

print(count)


## 답안과 같은 풀이
##답안에서는 last를 따로 정의하지 않고 N을 갱신하는 방법으로 진행. (어차피 N은 쓰이지 않으니 그래도 될 듯.)

## 답안 발상: 가장 큰 화폐 단위부터 거슬러 준다.