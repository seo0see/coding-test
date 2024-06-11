# 문자열로 풀이
def solution(date1, date2):
    date1 = int('1'+''.join('{0:0>5}'.format(i) for i in map(str,date1)))
    date2 = int('1'+''.join('{0:0>5}'.format(i) for i in map(str,date2)))
    if date1<date2:
        return 1
    return 0

# 숫자로 풀이
def solution(date1, date2):
    for i in range(3):
        if date1[i] < date2[i]:
            return 1
        elif date1[i] != date2[i]:
            break
    return 0


# 테스트 15개 모두 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

## 문자열로 풀이에서 알게된 것: join, 문자열 formatting, map에 대해서 알아보다가.. 이거 함수를 적용하는 것임을 알게 됨.
## 숫자로 풀이에서 깨달은 것: 각 경우(if문에 걸리는 case와 걸리지 않는 case에 대해)에 대해서 더욱 촘촘히 봐야 함.

