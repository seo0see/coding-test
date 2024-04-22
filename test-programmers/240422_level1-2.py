# 시간 초과로 실패
from itertools import combinations_with_replacement

def solution(n, s):
    # for i in range(ceil(s/n), s): # 첫번째 수(제일 큰 수)
    best = []
    cddt = []
    cb = list(combinations_with_replacement(range(1, s), n))
    for i in range(len(cb)):
        if sum(cb[i]) == s:
            cddt.append(cb[i])  
    if len(cddt) == 0:
        return [-1]
    for j in cddt:
        mul = 1
        temp = 1
        for k in j:
            mul *= k
        if mul > temp:
            temp = mul
            best = j
    
        
    answer = list(best)
    return answer

# 채점 결과
# 정확성: 0 (14개)
# 효율성: 0 (6개)
# 합계: 0 / 100.0