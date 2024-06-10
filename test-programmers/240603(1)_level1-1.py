def solution(wallpaper):
    loc_x, loc_y = set(),set()
    
    for i in range(len(wallpaper)):
        
        # lux와 rdx 결정
        if '#' in wallpaper[i]:
            loc_x.add(i)
            
        # luy와 rdy 결정
        strg = wallpaper[i]
        y = 0
        while True:
            temp = strg.find('#')
            if temp == -1:
                break
            else:
                y += temp
                loc_y.add(y)
                y += 1
                strg = wallpaper[i][y:]

                
    print(loc_x, loc_y)
    print(min(loc_x), min(loc_y), max(loc_x), max(loc_y))
    luy, rdy, lux, rdx = min(loc_y), max(loc_y)+1, min(loc_x), max(loc_x)+1
    
    answer = [lux, luy, rdx, rdy]
    return answer


# 31개 테스트 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

# 이 문제를 풀면서 알게 된 것: 문자열에의 find 메소드, one-line으로 if-else문 구성
# 애먹은 부분
#  - loc_y 원소 결정 부분에서의 else 이후의 부분 구성에 있어 논리 생각
#  - 줄별로 '#'이 하나가 있는 것이 아닌데 간과했었음.
#  - 뭔가 문제에서 x랑 y가 반대로 되어 있는 것 같음..