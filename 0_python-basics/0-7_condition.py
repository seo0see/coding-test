score = 85

# pass 문
if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')
print('프로그램을 종료합니다.')


# 줄바꿈 없이 조건문 표현
if score >= 80: result = "Success"
else: result = "Fail"
print(result)

# 조건부 표현식
result = "Success" if score >= 80 else "Fail"
print(result)
