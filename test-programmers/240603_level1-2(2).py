def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return sum([i for i in range(1, (num // 2) + 1) if num % i == 0])


## 다른 사람의 풀이
## 내 것이 더 효율적인 듯. 탐색 범위가 확 줄기에
## 다만, list comprehension을 쓴 부분은 참고하면 좋을 듯.
## (만약 그렇게 진행한다면 한 번 i에 대해서 쭉 한 후, n을 i로 나눈 몫을 추가하도록 하는 방법.)