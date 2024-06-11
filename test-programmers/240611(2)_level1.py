def solution(bandage, health, attacks):
    # 붕대 감기는 t초 동안 붕대를 감으면서 1초마다 x만큼의 체력을 회복. t초 연속으로 붕대를 감는 데 성공한다면 y만큼의 체력을 추가로 회복
    # bandage: 붕대 감기 기술의 시전 시간, 1초당 회복량, 추가 회복량을 담은 1차원 정수 배열
    # health: 최대 체력을 의미하는 정수
    # attacks: 몬스터의 공격 시간과 피해량을 담은 2차원 정수 배열
    # 목적: 모든 공격이 끝난 직후 남은 체력을 return. 만약 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽는다면 -1을 return
    
    answer = health
    running = 0 # 연속 여부 세기
    attack_time = [i[0] for i in attacks]
    print(0, answer, running)
    
    # 시간 진행에 따라 진행
    for i in range(1, attacks[-1][0]+1):
        if i in attack_time: # 공격 받는다면
            running = 0
            answer -= attacks[attack_time.index(i)][1]
        else: # 공격받지 않는다면
            running += 1
            # 현재 채력 업데이트
            answer = min(health, answer+bandage[1])
            if running >= bandage[0]: 
                answer = min(health, answer+bandage[2])
                running=0                
        print(i, answer, running)
        # 죽었는지 확인
        if answer <=0: return -1
            
    return answer


# 테스트 20개 모두 통과
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

## 문제 다 구현한 후에, 문제가 제시한 조건 중 빠뜨린 것이 있는지 여부 확인 필수.
##(추가 회복의 의미를 잘 알지 못했고, 게임 중간에 체력 0이하가 되면 죽고 더이상 회복 못한다는 것 빼먹음. 또, t가 체력회복 최소단위라고 한 적이 없는데 오해함.)

## 다른 사람의 풀이
