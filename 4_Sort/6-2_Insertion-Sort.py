# 삽입 정렬 (Insertion Sort) 소스코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

#=====
## 내가 작성한 것은 아래의 것으로,
##예시답안은 선택한 것이 위치를 찾기 위해 선택한 원소 앞의 것들의 원소와 하나씩 비교하며 위치를 찾음(정렬이 되어 있으니 리스트 인덱스 역순으로 비교).
##나는 선택한 것의 위치를 찾기 위해 앞에서부터 크기를 비교하고, 찾은 위치 이후의 것들은 자리바꿈.
##반복문을 덜 중첩하여 쓴 예시답안의 것이 더욱 효율적임. 


for i in range(1, len(array)):
    # 하나 선택하기
    point = array[i]
    # print(point)
    # 앞 배열과 비교해서 자리 찾기 (자리 찾으면 그 자리 이후의 것은 한 칸씩 이동)
    for j in range(len(array[:i])):
        if point < array[j]:
            location = j
            for k in range(i, j,-1):
                # print(array[k], array[k-1])
                array[k] = array[k-1]
            array[j] = point
            # print(array)
            break

print("답:", array)
