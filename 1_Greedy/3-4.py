# 예제 3-4. 1이 될 때까지

n, k = map(int, input().split())

result = 0
while n != 1:
    if n >= k:
        remain = n%k
        if remain != 0:
            result += remain
            n -= remain
            # print("빼기", n)
        else:
            result += 1
            n = n//k
            # print("나누기", n)
    else:
        result += n-1
        n = 1
        # print("마무리 빼기", n)

print(result)


## input: 25 5
## output: 2
## input: 25 3
## output: 6

## 잘못 풂. if 조건과 else 조건이 촘촘해야 했는데, 걸러지지 않은 경우(n<k인 경우)가 있어 while 문이 무한대로 돎.
##그래서 n<k인 경우에 대해서 걸릴 수 있도록 조건문을 크게 한 번 씌움.

## 예시 답안과 유사
##하지만 예시답안처럼 나머지가 0인지 여부를 따지는 조건문이 아닌 그냥 한 번에 구하는 방법도 있었네. 그게 더 시간효율적.
##단순하게 푸는 답안에서는 N이 큰 수가 되는 경우에도 빠르게 동작하려면 N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 소스코드를 작성해야 함.

## 답안의 발상: 최대한 많이 나누기 수행. K가 2 이상이기만 하면 K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N의 값을 줄일 수 있으며, N이 결국 1에 도달한다.