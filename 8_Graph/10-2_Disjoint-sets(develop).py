# 경로 압축 기법 소스코드
# 개선된 서로소 집합 알고리즘 소스코드

### find 함수를 최적화. 경로 압축(Path Compression 기법 적용). 이를 통해 시간복잡도 개선.
###find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법.
### find_parent(parent,x) 함수 외에는 10-1과 소스코드 동일
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속핮 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합을 출력 ### 각 원소의 루트 노드
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

## input
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
## output
# 각 원소가 속한 집합: 1 1 1 1 5 5
# 부모 테이블: 1 1 1 1 5 5
    
### 노드의 개수가 V개이고, 최대 V -1 개의 union 연산과 M개의 find 연산이 가능할 때,
###경로 압축 방법을 적용한 시간 복잡도는 O(V + M(1 + log_(2-M/V)V))

