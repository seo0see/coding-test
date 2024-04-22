def solution(n, s):
    if s//n == 0:
        return [-1]


    answer = [s//n] * (n-s%n)
    answer2 = [(s//n)+1] * (s%n)
    answer.extend(answer2)
    return answer

## 다른 사람의 접근법.
## 이렇게 문제 자체를 보고 접근할 수 있는 센스가 있어야 할 듯.
## 나는 전체 탐색으로 접근했음.

# 채점 결과
# 정확성: 70.0 (14개 모두 통과)
# 효율성: 30.0 (6개 모두 통과)
# 합계: 100.0 / 100.0