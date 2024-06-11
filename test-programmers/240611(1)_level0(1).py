def solution(date1, date2):
    return int(date1 < date2)


## 다른 사람의 풀이
## 알게된 것: 리스트간에도 부등호로 비교연산이 가능하군. & 비교가 같은 인덱스끼리 순서대로 이루어지고 처음에서 결과가 나면 그것대로 가져가는 군.



from datetime import date

def solution2(date1, date2):
    date1 = date(date1[0], date1[1], date1[2])
    date2 = date(date2[0], date2[1], date2[2])
    return 1 if date1 < date2 else 0

## 다른 사람의 풀이
## 알게된 것: datetime.date()를 이용한 날짜비교



def solution3(date1, date2):
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    ymd1 = str(y1) + str(m1).rjust(2, '0') + str(d1).rjust(2, '0')
    ymd2 = str(y2) + str(m2).rjust(2, '0') + str(d2).rjust(2, '0')
    answer = 1 if ymd1 < ymd2 else 0
    return answer


## 다른 사람의 풀이
## 알게된 것: rjust()

