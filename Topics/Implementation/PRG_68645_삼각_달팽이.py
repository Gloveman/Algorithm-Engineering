'''
우선, n이 1이나 2인 경우는 쉽게 구할 수 있으므로 바로 return하도록 했다.
1차원 배열로 풀이해보려 했지만 index 계산에서 막혔다.
어차피 1001 * 1000을 해도 그렇게 값이 크지 않다.
그냥 2차원 배열을 사용하여 O(n^2) 풀이를 해보자.
기존에는 반복 숫자를 3으로 나눈 나머지를 통해 '현재 차수에서 정확히 어느 방향으로 이동해야 하는가'를 생각했다.
그러나, 실제로는 한 방향으로의 이동이 끝나면 그 다음 회전을 해 주면 된다. 즉, 반복문과 별개의 '현재 방향' 변수를 도입하면
조금 더 쉽게 생각이 가능했다. 이것도 분명 '좌표 탐색'의 일종으로 볼 수 있는데, bfs/dfs에서 자주 활용하던 방법을 응용할 수 있다는 것을 알았다.
또한, 시작 위치를 (-1,0)으로 지정하는 트릭을 통해 '움직이고 대입한다'라는 규칙을 일관성 있게 적용하는 것도 기억해 둘 포인트이다.
2차원 배열을 1차원으로 펼치는 맨 마지막줄 역시 반드시 기억해야다.
'''

# def solution(n):
#     if n == 1: return [1]
#     if n == 2: return [1,2,3]
#     total_len = (n * (n+1)) // 2
#     answer = [0 for _ in range(total_len)]
#     num = 1 # 채워질 숫자
#     next_idx = 0 #방문 '할' 인덱스   
#     for i in range(n,0,-1):
#         # 3k-2번째: 왼쪽 아래
#         if i % 3 == 1:
#             for j in range(i):
#                 next_idx += j
#                 answer[next_idx] = num
#                 num += 1
#         # 3k-1번째: 오른쪽        
#         elif i % 3 == 2:
#             for j in range(i):
#                 next_idx += 1
#                 answer[next_idx]= num
#                 num +=1
#         # 3k번째: 왼쪽 위
#         else:
#             for j in range(i):
#                 next_idx -=
#                 answer[last_idx]= num
#                 num +=1 
#     return answer

def solution(n):
    if n == 1: return [1]
    if n == 2: return [1,2,3]
    answer = [[0] * i for i in range(1,n+1)] #삼각형을 표현한 2차원 배열
    num = 1 # 채워질 숫자
    cur_state = 0 #방향 정보
    cur_r, cur_c = -1,0 #맨 처음에도 내려가는 것으로 생각 - 움직인 뒤 대입한다는 일관성 성립
    move_c = [0, 1, -1]
    move_r = [1, 0, -1]
    
    for i in range(n,0,-1):
        for j in range(0,i):
            cur_r, cur_c = cur_r + move_r[cur_state], cur_c + move_c[cur_state]
            answer[cur_r][cur_c] = num
            num +=1
        cur_state = (cur_state+1) % 3
        
    return [j for i in answer for j in i]