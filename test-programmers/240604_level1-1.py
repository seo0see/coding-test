def solution(n, m):
    
    # 최대 공약수 계산
    mad_cand = []
    for i in range(1, min(m,n)+1):
        if n%i==0 and m%i==0:
            mad_cand.append(i)
    mad = max(mad_cand)
            
    # 최대 공약수 계산 - 둘 중에 가장 작은 것의 루트로 나누어지는지 하나씩 확인하기.  # 아래의 코드가 안되는 이유를 모르겠음..
    # a, b = (n,m) if n<m else (m,n)
    # mad_cand = []
    # for i in range(1, int(a**0.5)+1):
    #     if n%i==0 and m%i==0:
    #         mad_cand.append(i)
    #         if b % (a//i) == 0:
    #             mad_cand.append(a//i)
    # mad = max(mad_cand)
    
    # 최소 공배수 계산
    # 최대공약수*그들만 가지고 있는 것
    mim = n*m/mad
       
    answer = [mad, mim]
    return answer


# 16개 테스트 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

# 주석처리한 부분으로 실행시, 16개 테스트 중 13개 통과 (3개 실패 -  7, 9, 15번)
# 채점 결과
# 정확성: 81.3
# 합계: 81.3 / 100.0

