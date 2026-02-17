'''
쉬운 구현을 위해 1초 단위의 count 사용, 문제 내용을 그대로 구현
체력이 0 이하가 된 경우 즉시 return하도록 설정

pop 방식은 O(N)의 시간 복잡도를 가지므로, deque를 통해 popleft를 하는 방식이 더 유리
각 공격 시간의 차이 dt 기준으로 계산하는 로직도 시도해보기
'''
def solution(bandage, health, attacks):
    T_max = attacks[-1][0]
    bandage_t, x, y = bandage
    succ_t = 0 #연속 성공 시간
    answer = health #남은 체력
    for t in range(1,T_max+1):
        #공격 받았을때
        if t ==attacks[0][0]:
            answer -= attacks[0][1] #체력 깎임
            if answer <=0: #죽은 경우
                return -1
            succ_t = 0  # 연속 성공 초기화
            attacks.pop(0) #해당 공격 제거
            continue 
        #붕대 감기
        answer = min(health, answer+x)
        succ_t +=1
        #연속 성공 채웠는가?
        if succ_t == bandage_t:
            succ_t = 0
            answer = min(health, answer+y)
    return answer

#t초동안 붕대 - 1초마다 +x / t초 연속으로 유지되면 +y 추가
#최대 체력 이상 X
#몬스터 공격 시 취소 - 연속 성공 0, 다시 스킬 시작
#붕대 감기를 성공적으로 끝낸 뒤에도
#정해진 피해량/0 이하이면 사망
#캐릭터는 끝까지 생존하는가?
# 남은 체력 or -1(죽으면) return
# bandage = [t, x, y]
# attacks= [[when, dmg],....]