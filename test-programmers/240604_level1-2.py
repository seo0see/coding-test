def solution(k, score):
    answer = []
    fame = [0 for _ in range(k)]
    cnt,temp = 0, [] # 명예의 전당의 점수의 개수가 k개가 되기 전까지 사용할 변수
    for i in score:
        if min(fame) < i:
            fame[fame.index(min(fame))] = i
        if cnt < k: # 명예의 전당의 점수가 다 차기 전까지
            temp.append(i)
            answer.append(min(temp))
            cnt += 1
        else:
            answer.append(min(fame))
        
    return answer


# 26개 테스트 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
