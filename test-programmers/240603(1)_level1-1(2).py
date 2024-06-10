
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]


## 다른 사람의 접근법.
## 이렇게 쉽게 하나씩 모두 접근하면서 append하면 되는데,, 이 쉬운 생각을 못했네