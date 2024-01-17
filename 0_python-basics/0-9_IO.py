# 입력을 위한 전형적인 소스코드
n = int(input()) # 데이터의 개수 입력
data = list(map(int, input().split())) # 각 데이터를 공백으로 구분하여 입력
data.sort(reverse=True)
print(data) ## 예시에서는 공백으로 구분된 한 줄 짜리 데이터 입력


# 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split()) # n, m, k를 공백으로 구분하여 입력
print(n, m, k)


# readline() 사용 소스코드 예시
import sys
data = sys.stdin.readline().rstrip() # 문자열 입력 받기
print(data) ## 예시에서는 'Hello World'를 입력하고 그걸 그대로 받도록 함.


## f-string 사용 예시
answer = 7
print(f'정답은 {answer}입니다.') ##결과: 정답은 7입니다.
