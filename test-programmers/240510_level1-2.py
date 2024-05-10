def solution(record):
    # 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.
    answer = [] 
    temp = [] # 각 원소의 처음은 id, 다음은 들어갈 텍스트
    id_nick = {} # key는 id, value는 nickname.
    template = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    
    for i in record:
        txt = i.split()
        if txt[0] == "Change":
            id_nick[txt[1]] = txt[2]
        else:
            temp.append([txt[1], txt[0]])
            if txt[0] == "Enter":
                id_nick[txt[1]] = txt[2]
    # print(temp)
    # print(id_nick)
        
    for i in temp:
        answer.append(id_nick[i[0]] + template[i[1]])
    return answer


# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

# 이걸 하면서 되새기게 된 점: 딕셔너리의 사용, 어떻게 문제를 푸는 것이 좋을지 차근차근 생각하게 됨(생각 다 마친 후에 코드 작성하는 것이 맞는 듯)
