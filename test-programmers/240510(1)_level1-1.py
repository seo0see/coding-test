def solution(k, m, score):
    answer = 0
    
    # 과일 장수가 가능한 많은 사과 팔았을 때 얻을 수 있는 최대 이익 (최저 사과 점수 * 개수가 수익.)
    # 최저 사과 점수를 높이는 게 관건. 높은 것부터 우선 짝지어 만들고, 그 다음 낮은 것으로 만들면 될듯.
    score.sort()
    for i in range(len(score)//m):
        answer += score[-(m*(i+1))]*m
    
    return answer


# 24개 테스트 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

## 다른 사람의 풀이 중 참고할 만한 것.
# sum(sorted(score)[len(score)%m::m])*m
# 인덱스를 m 번씩 뛰어넘는거에요. A = [1,2,3,4,5,6,7,8,9]일 때 A[::3] >>> [1,4,7]