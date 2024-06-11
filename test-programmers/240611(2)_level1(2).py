
def solution1(bandage, health, attacks):
    hp = health
    start = 1
    for i, j in attacks:
        hp += ((i - start) // bandage[0]) * bandage[2] + (i - start) * bandage[1]
        start = i + 1
        if hp >= health:
            hp = health
        hp -= j
        if hp <= 0:
            return -1
    return hp


## 다른 사람의 풀이
## 알게된 것
## - 시간 순서가 아닌 attack 리스트 안에서 풀어가기. 이렇게하면 반복 수행이 줄어 시간 적게 소요
## - hp를 계산할 때 이렇게 수식으로 풀 수 있으며, 이렇게 하면 짧게도 표현 가능함. & 비교연산이 줄어 시간이 적게 소요



def solution2(bandage, health, attacks):
    t, x, y = bandage
    time=temp=int(not ([]))
    attacks={x[temp-temp]:x[temp] for x in attacks} # {2: 10, 9: 15, 10: 5, 11: 5}와 같이 딕셔너리로 표현
    hp=health
    while time<=max(attacks.keys()):
        target=time+t
        while time<target:
            if time in attacks.keys():
                health-=attacks[time]
                if health<=temp-temp:
                    return -temp
                break
            health+=x
            if health>hp:
                health=hp
            time+=temp
        else:
            time-=temp
            health+=y
            if health>hp:
                health=hp
        time+=temp
    return health

## 다른 사람의 풀이
## 알게된 것: 딕셔너리로 표현하여 리스트 추가로 만들어 공간 차지하지 않게 하기
