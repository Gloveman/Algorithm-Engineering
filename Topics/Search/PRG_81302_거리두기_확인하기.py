#딱봐도 완전탐색의 냄새가 난다
# dist = abs(r1-r2) + abs(c1 - c2)
'''
bfs 탐색 기법을 적용
그러나 break 위치가 명확하지 않아 별도 함수로 분리해보려고 한다.
그럼에도 문제가 생겨 확인해보니, visited set 초기화 시 시작 위치를 추가하는 것을 제대로 하지 않은 것이 문제였다.

다만, 이 문제의 경우 최대 이동 거리가 정해져 있어 경우의 수가 적으므로, 모든 경우를 직접 확인해 보는 것이 더 빠르다.
즉, 2칸 앞에 사람이 있는지, 오른쪽에 파티션이 없고 오른쪽 위에 사람이 있는지 이런 식으로 충분히 세울 수 있다.
따라서 문제 조건을 잘 확인하여, '이동 거리가 정해져 있고' 경우의 수가 적다면 직접 조건을 다 설정하는 것이 문제 해결을 더 빠르게 할 수도 있다.
다만, bfs 로직을 다시 연습했다는 점에서 의의가 있다.

'''

from collections import deque
def is_valid(grid):
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, 1, -1]
    for i in range(5):
        for j in range(5):
            if grid[i][j] == 'P':
                visited = set()
                visited.add((i,j))
                q = deque([(i, j, 0)])
                while q:
                    cur_x, cur_y, cur_dist = q.popleft()
                    if cur_dist == 2 : continue
                    for d in range(4):
                        nx, ny = cur_x + move_x[d], cur_y + move_y[d]
                        if 0<=nx<5 and 0<=ny<5 and (nx,ny) not in visited:
                            if grid[nx][ny] == 'X': continue
                            if grid[nx][ny] == 'P':
                                return False
                            visited.add((nx, ny))
                            q.append((nx,ny,cur_dist +1))
    return True

def solution(places):
    return [1 if is_valid(grid) else 0 for grid in places]