'''
BFS를 통해 '연결된 석유 덩어리' 그룹을 찾아 고유 id 부여
연결 요소를 찾는 과정에서 land 배열 값을 즉시 수정하여 별도의 visited set 없이 탐색 가능
id - count의 hash map을 사용하여 총 시추량 계산
visited를 통해 중복 카운팅을 방지

group index가 연속된 숫자인 만큼 리스트를 활용하는 것이 더 빠를 수 있음
빈 공간은 어차피 카운팅하지 않아도 되므로 열 단위 탐색 시 if land[r][c] > 1 조건으로
불필요한 연산 차단 가능
'''
from collections import deque
def find_connected_oils(start, region_idx, land, oil_map):
    land[start[0]][start[1]] = region_idx
    count = 1
    oil_map[region_idx] = 0

    q = deque([start])
    next_move = [(0,1), (0, -1), (1, 0), (-1, 0)]
    MIN_R, MIN_C, MAX_R, MAX_C = 0, 0, len(land) - 1, len(land[0]) - 1

    while q:
        cur_r, cur_c = q.popleft()
        for dr, dc in next_move:
            nr, nc = cur_r+dr, cur_c+dc
            if MIN_R<=nr<=MAX_R and MIN_C <= nc <= MAX_C:
                if land[nr][nc] == 1:
                    land[nr][nc] = region_idx
                    q.append((nr, nc))
                    count +=1
    oil_map[region_idx] = count
    return


def solution(land):
    answer = 0
    oil_map={0:0}
    region_idx = 2
    # 각 영역 구분
    for r in range(len(land)):
        for c in range(len(land[0])):
            if land[r][c] == 1: #새로운 영역
                find_connected_oils((r,c),region_idx,land, oil_map)
                region_idx +=1
    # 가장 좋은 시추 위치 찾기
    for c in range(len(land[0])):
        visited=set()
        cur_total = 0
        for r in range(len(land)):
            if land[r][c] not in visited:
                visited.add(land[r][c])
                cur_total += oil_map[land[r][c]]
        answer = max(answer, cur_total)    
    return answer


#연결 요소 구하기
#각각의 영역을 2, 3, 4,...로 구분 (1과 구분되게)
#해당 영역의 총 석유 덩어리 수를 mapping
#{0: 10, 1:5, ...}
