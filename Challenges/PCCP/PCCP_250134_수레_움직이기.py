'''
수레 종류별로 '방문 여부'를 독립적으로 관리하는 것이 핵심
초기에는 두 수레의 방문 여부를 모두 확인하는 4차원 배열을 활용했으나, 이것은 한 수레가 도착한 경우
나머지 수레에 대해 제대로 확인이 불가함
이에 bfs queue에 각 수레별 방문했던 칸을 set으로 저장하여 탐색

서로 자리를 바꾸는지 확인하는 조건에서, 둘 중 하나라도 이동할 자리가 상대 수레의 원래 자리가 아니라면 문제가 없음
즉, or로 조건을 연결해야 하는데, and로 조건을 연결하여 답이 맞지 않는 실수가 있었음
'''
from collections import deque
# '동시에 이동'
def bfs(red_s, red_e, blue_s, blue_e, maze):
    q = deque([(red_s,blue_s, 0, {red_s}, {blue_s})]) #각 수레의 방문 여부를 독립적으로 확인 
    MIN_I, MIN_J, MAX_I, MAX_J = 0, 0, len(maze)-1, len(maze[0]) -1
    next_move = [(-1,0),(0, -1), (1,0), (0,1)]
    while q:
        cur_red, cur_blue , cur_t, red_visited, blue_visited = q.popleft()
        red_end = (cur_red == red_e)
        blue_end = (cur_blue == blue_e)
        if red_end and blue_end: #둘 다 도달한 경우
            return cur_t
        #어느 한 쪽이 도달한 상황에서는???
        for red_di, red_dj in next_move:      
            red_ni = cur_red[0] if red_end else cur_red[0] + red_di
            red_nj = cur_red[1] if red_end else cur_red[1] + red_dj
            for blue_di, blue_dj in next_move:
                blue_ni = cur_blue[0] if blue_end else cur_blue[0] + blue_di
                blue_nj = cur_blue[1] if blue_end else cur_blue[1] + blue_dj
                if MIN_I <= red_ni <= MAX_I and MIN_J <= red_nj <= MAX_J:
                    if MIN_I <= blue_ni <= MAX_I and MIN_J <= blue_nj <= MAX_J:
                        if (red_end or (red_ni, red_nj) not in red_visited) and\
                        (blue_end or (blue_ni, blue_nj) not in blue_visited): # 이미 방문한 경로 X
                            if maze[red_ni][red_nj] != 5 and maze[blue_ni][blue_nj] != 5 and \
                            (red_ni, red_nj) != (blue_ni, blue_nj): #벽 X, 서로 안겹침
                                #서로 자리 바꾸기 X
                                if (red_ni, red_nj) != cur_blue or (blue_ni, blue_nj) != cur_red:
                                    next_red_visited = red_visited if red_end else red_visited | {(red_ni, red_nj)}
                                    next_blue_visited = blue_visited if blue_end else blue_visited | {(blue_ni, blue_nj)}
                                    q.append(((red_ni, red_nj), (blue_ni, blue_nj), cur_t+1,
                                    next_red_visited, next_blue_visited ))
                                
    return 0

def solution(maze):
    red_start = blue_start = red_end = blue_end = (0,0)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_end = (i, j)
            elif maze[i][j] == 4:
                blue_end = (i, j)
    return bfs(red_start, red_end, blue_start, blue_end, maze)

#모든 수레를 도착 칸으로 이동
#매 턴마다 '모든 수레'를 이동
#도착 칸 이동 X, 이미 방문 칸 이동 X
#한 칸에는 한 수레만, 서로 자리 바꾸기 X - 반드시 해당 시점에서 비어있는 칸으로만 이동이 된다

#필요한 turn 최솟값

#time t를 고려한 bfs