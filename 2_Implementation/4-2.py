# 예제 4-2. 시각

n = int(input())
result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            a = "{0:0>2}".format(i)+"{0:0>2}".format(j)+"{0:0>2}".format(k)
            if str(3) in a:
                # print(a)
                result += 1

print(result)


## input: 5
## output: 11475

## 틀림. n에 대해서는 +1을 해줘야 함을 놓침. 
## 풀이 중 문자열 formatting에 대해 코딩테스트용으로 정리한 것을 보면서 진행함.

## 답안 예시와 풀이 매우 유사.
##하지만 내 것이 formatting을 해주어 더 정교한 듯. 3의 존재여부가 아닌 0의 존재여부를 확인하는 경우라면..

## 완전 탐색(Brute Forcing) 유형. 
##가능한 전체 경우의 수가 100,000개도 되지 않으므로 파이썬에서 문자열 연산을 이용해 확인을 해도 시간 제한 2초 안에 문제를 해결할 수 있음.

