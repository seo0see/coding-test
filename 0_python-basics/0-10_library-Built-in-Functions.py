# 내장함수
# sum()
result = sum([1,2,3,4,5])
print(result) ##결과: 15

# min()
result = min(7,3,5,2)
print(result) ##결과: 2

# max()
result = max(7,3,5,2)
print(result) ##결과: 7

# eval()
result = eval("(3 + 5) * 7")
print(result) ##결과: 56

# sorted()
result = sorted([9, 1, 8, 5, 4]) # 오름차순으로 정렬
print(result) ##결과: [1, 4, 5, 8, 9]
result = sorted([9, 1, 8, 5, 4], reverse = True) # 내림차순으로 정렬
print(result) ##결과: [9, 8, 5, 4, 1]
result = sorted([('홍길동', 35), ('이순신', 75), ('이무개', 50)], key=lambda x: x[1], reverse=True)
print(result) ##결과: [('이순신', 75), ('이무개', 50), ('홍길동', 35)]