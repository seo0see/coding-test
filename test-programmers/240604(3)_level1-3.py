def solution(x):
    # 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 함.
    answer = True if x%sum(list(map(int,str(x))))==0 else False
    return answer


# 17개 테스트 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0


## 다른 사람의 풀이
# def Harshad(n):
#     return n%sum(int(x) for x in str(n)) == 0
## 나는 list로 놓고 문제를 풀었지만, 아예 문자열로 생각해서 문제를 풀어갈 수도 있음.