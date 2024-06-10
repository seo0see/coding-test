def hanoi(n):

    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    return ans

## 다른 사람의 풀이
## 나와 같은 접근인대, yield와 yield from을 사용함.. 새롭게 배움..

