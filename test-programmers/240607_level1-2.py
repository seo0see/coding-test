def solution(n, m, section):
    answer = 0 # 페인트칠 횟수
    while section:
        answer += 1
        temp=set()
        for j in section:
            if j < section[0]+m: # 영역이 아닌 횟수를 구하는 것이니 꼼꼼히 따지지 않아도 되어 이렇게 코드 작성
                temp.add(j)
            else:
                break
        print(section, j, temp)
        section = list(set(section)-temp)
    
    return answer


## 이게 왜 테스트를 못 통과하는지 이해가 안됨.
# 테스트 50개 중 18개 통과
# 채점 결과
# 정확성: 36.0
# 합계: 36.0 / 100.0

