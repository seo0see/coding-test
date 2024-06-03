def solution(n):
    divi = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divi.add(i)
            divi.add(n//i)
    answer = sum(divi)
    return answer


# 17개 테스트 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

# 이 문제를 풀면서 알게 된 것: 집합(set)도 sum 연산이 됨.
