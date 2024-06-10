
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer


## 다른 사람의 풀이
## 막 쓰고, append 수에 조건을 걸어 최소의 수를 지우는 것을 반복하면 되는 거군.
## 이게 훨씬 간결하고 이해하기 좋음.