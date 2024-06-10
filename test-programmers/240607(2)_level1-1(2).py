def solution(n, m, section):
    answer = 1 # 페인트칠 횟수
    start = section[0]
    while True:
        # print("커버범위: ", start, start+m-1)
        for j in section:
            if j > start+m-1:
                # print(j)
                answer += 1
                start = j
                continue
        if start+m-1 >= section[-1]:
            break
        else:
            answer += 1
    return answer


# 앞의 코드에서 집합은 생각하지 않고 단순히 숫자놀이로 생각해서 풂.
# 테스트 50개 모두 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

