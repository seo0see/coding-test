# permutations
# 리스트 ['A', 'B', 'C']에서 3개(r=3)를 뽑아 나열하는 모든 경우의 수 출력
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result) ##결과: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]


# combinations
# 리스트 ['A', 'B', 'C']에서 2개(r=2)를 뽑아 순서에 상관없이 나열하는 모든 경우를 출력
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result) ##결과: [('A', 'B'), ('A', 'C'), ('B', 'C')]


# product
# 리스트 ['A', 'B', 'C']에서 중복을 포함하여 2개(r=2)를 뽑아 나열하는 모든 경우를 출력
from itertools import product
data = ['A', 'B', 'C'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result) ##결과: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]


# combinations_with_replacement
# 리스트 ['A', 'B', 'C']에서 중복을 포함하여 2개(r=2)를 뽑아 순서에 상관없이 나열하는 모든 경우를 출력
from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result) ##결과: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

