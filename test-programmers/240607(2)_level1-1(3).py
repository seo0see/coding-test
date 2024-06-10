def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer


## 다른 사람풀이
## 기준점을 두고 그것과 덧칠 필요한 부분과의 차이를 롤러의 크기(커버 가능 크기)와 비교하여 계산하는 것.
## 이런 발상을.. 참...