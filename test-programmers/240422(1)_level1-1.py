def solution(nums):
    answer = 0
    length = len(nums)
    # 3개 고르기 (i, j, k 순으로 인덱스 정해 구하)
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                # 소수인지 확인
                result_sum = sum([nums[i], nums[j], nums[k]])
                count = 0
                ## 이 부분에서 count가 0이면 소수임을 인정하는 것이 아니라, 애초에 아래 조건문이 True가 아닌 순간 break 하는 방법으로 접근해도 좋을듯.
                ## 기본적인 소수판별 알고리즘에 판별 범위를 x의 제곱근으로 축소시킨겁니다. range(1,int(x**0.5)+1):
                for l in range(1, result_sum-1):
                    if result_sum % (l+1) == 0:
                        count += 1
                if count == 0:
                    answer +=1
    
    return answer


# 26개 테스트 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
