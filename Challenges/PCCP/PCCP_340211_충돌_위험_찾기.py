"""
<생각의 흐름>
(r_i,c_i) 좌표 가진 n개의 point (1~n의 고유번호)
로봇별로 m개의 point를 지나는 경로, 할당된 순서대로
총 x대, 0초 동시 출발, 1초마다 상하좌우 1만큼
항상 최단경로, r좌표 변화 우선순위
마지막 포인트 도착하면 끝
같은 좌표에 2대 이상이 모이는 경우의 합

내가 계속 관리해야 하는 데이터
i번째 로봇의 데이터 - 현재 위치, 다음 목적지(routes 중 몇 번째 인덱스 위치인가)

같은 칸에 있는지 확인
이때, 3명 이상이어도 1개로 취급해야 한다
그리고 로봇 리스트의 경우에도 '목적지에 도착한 로봇'을 제외할 필요가 있음

문제점) for idx in robot_map:으로 순환하는 도중에 robot_map의 요소를 삭제하면 문제가 발생하게 됨.
Lazy deletion을 실행해야 함
이동 중인 robot이 1대 남을때까지 반복 - ㅇ
개선점) 장애물이 없고, 좌표 중복도 되는 점에서 일단 r 좌표를 같게 만들고 그 이후에 c를 맞춰주면 됨

풀이 방식 - pre-calculation
t초마다 모든 이동을 시뮬레이션하고, 이후 매 초마다 겹치는 로봇이 있는지 확인
모든 이동을 저장하므로 메모리 사용 많음
이 문제와 같이 충돌이 없는 '특수한 경우'에 적용되는 방식

풀이 방식 - lazy delete
우리의 접근 방식대로 모든 로봇이 이동을 마칠때까지 이동 및 충돌 여부 확인
현재 위치만 저장하므로 메모리 사용 적음
일반적인 시뮬레이션에도 적용 가능

"""
def get_distance(r1, c1, r2, c2):
    return abs(r1-r2)+abs(c1-c2)

def solution(points, routes):
    NEXT_MOVE = [(-1,0), (1,0), (0,-1), (0,1)]
    N_ROBOT = len(routes)
    #robot map 초기화
    #[[cur_r, cur_c], cur_goal]
    robot_map = dict()
    for i in range(N_ROBOT):
        start_point = routes[i][0]
        robot_map[i] = [points[start_point-1],1] # 지금이 몇 번째 목적지야?
    #위험한 횟수 총합
    collision_count = 0
    # 모든 로봇이 운송을 완료하는 경우
    while len(robot_map)>1: #하나 남은 경우도 상관없음!!!!!
        #모두 이동
        for idx in robot_map:
            min_dist = 10000
            final_r, final_c = 0, 0
            for dr, dc in NEXT_MOVE:
                nr, nc = robot_map[idx][0][0] + dr, robot_map[idx][0][0] + dc
                if 1 <= nr <= 100 and 1<= nc <=100:
                    cur_goal = routes[idx][robot_map[idx][1]]-1
                    cur_dist = get_distance(nr, nc, points[cur_goal][0],points[cur_goal][1])
                    if cur_dist < min_dist:
                        min_dist = cur_dist
                        final_r, final_c = nr, nc
            robot_map[idx][0] = [final_r, final_c]                        
        
        #겹침 확인
        cur_points = set()
        visited = set()
        for idx in robot_map:
            if (robot_map[idx][0][0],robot_map[idx][0][1]) not in cur_points:
                cur_points.add((robot_map[idx][0][0],robot_map[idx][0][1]))  
            elif (robot_map[idx][0][0],robot_map[idx][0][1]) not in visited:
                collision_count +=1
                visited.add((robot_map[idx][0][0],robot_map[idx][0][1]))
                
        #현재 설정 목적지 도달 확인
        for idx in robot_map:
            cur_goal = routes[idx][robot_map[idx][1]]-1
            if robot_map[idx][0] == points[cur_goal]:
                #마지막이면 map에서 삭제
                if cur_goal == len(routes[0]) -1:
                    del robot_map[idx]
                #아니면 다음 목적지로
                else:
                    robot_map[idx][1] +=1
                    
    return collision_count

# pre-calculation으로 풀이
from collections import Counter

def solution(points, routes):
    # 1. 각 로봇의 전체 이동 경로(History)를 저장할 리스트
    # robot_paths[i] = [(r,c) at t=0, (r,c) at t=1, ...]
    robot_paths = []
    
    for route in routes:
        path = []
        # 각 로봇의 시작점
        start_idx = route[0] - 1
        curr_r, curr_c = points[start_idx]
        
        # 시작 위치 기록 (0초)
        path.append((curr_r, curr_c))
        
        # 포인트들을 순서대로 방문
        for i in range(1, len(route)):
            next_idx = route[i] - 1
            target_r, target_c = points[next_idx]
            
            # 현재 위치에서 다음 목적지까지 이동 기록 (최단 경로)
            # r 좌표 우선 이동
            while curr_r != target_r:
                if curr_r < target_r:
                    curr_r += 1
                else:
                    curr_r -= 1
                path.append((curr_r, curr_c))
            
            # c 좌표 나중 이동
            while curr_c != target_c:
                if curr_c < target_c:
                    curr_c += 1
                else:
                    curr_c -= 1
                path.append((curr_r, curr_c))
                
        robot_paths.append(path)

    # 2. 충돌 횟수 계산
    collision_count = 0
    
    # 가장 오래 걸리는 로봇의 시간 구하기
    max_time = 0
    for path in robot_paths:
        max_time = max(max_time, len(path))
    
    # 시간(t) 별로 모든 로봇의 위치 확인
    for t in range(max_time):
        # t초에 각 로봇이 어디에 있는지 수집
        positions = []
        for path in robot_paths:
            # 로봇이 t초에 아직 움직이고 있다면 위치 추가
            if t < len(path):
                positions.append(path[t])
            # 이미 도착해서 사라진 로봇은 무시
        
        # 좌표별 로봇 개수 세기
        pos_counter = Counter(positions)
        
        # 2대 이상 모인 좌표 개수 더하기
        for count in pos_counter.values():
            if count >= 2:
                collision_count += 1
                
    return collision_count


from collections import Counter


# Lazy delete 활용
def solution(points, routes):
    """
    Lazy Delete 방식을 사용하여 매 초 로봇의 이동과 충돌을 시뮬레이션합니다.
    
    Args:
        points (list): 포인트 좌표 리스트 [[r1, c1], [r2, c2], ...]
        routes (list): 로봇별 방문 포인트 번호 리스트
        
    Returns:
        int: 누적된 충돌 위험 횟수
    """
    N_ROBOT = len(routes)
    # 1. 로봇 상태 초기화: [현재_r, 현재_c, 다음_목적지_순서]
    # points는 1-based index이므로 호출 시 -1 처리
    robots = []
    for i in range(N_ROBOT):
        r, c = points[routes[i][0] - 1]
        robots.append([r, c, 1]) # 0번 포인트에서 시작, 다음 목적지는 1번 인덱스
    
    collision_count = 0
    arrived_set = set() # 논리적으로 삭제된(도착한) 로봇 인덱스 관리
    
    # [Step 1] 0초 시점 초기 위치 충돌 체크
    initial_positions = [(r[0], r[1]) for r in robots]
    counts = Counter(initial_positions)
    for c in counts.values():
        if c >= 2:
            collision_count += 1

    # [Step 2] 시뮬레이션 루프 (모든 로봇이 도착할 때까지)
    while len(arrived_set) < N_ROBOT:
        # 이번 초(tick)에 이동한 로봇들의 위치를 담을 리스트
        current_tick_positions = []
        
        for i in range(N_ROBOT):
            if i in arrived_set:
                continue
            
            # 현재 위치와 다음 목적지 좌표 가져오기
            curr_r, curr_c, goal_idx = robots[i]
            target_r, target_c = points[routes[i][goal_idx] - 1]
            
            # 최단 경로 이동 (r 우선순위)
            if curr_r != target_r:
                curr_r += 1 if curr_r < target_r else -1
            else:
                curr_c += 1 if curr_c < target_c else -1
            
            # 상태 업데이트
            robots[i][0], robots[i][1] = curr_r, curr_c
            current_tick_positions.append((curr_r, curr_c))
            
            # 목적지 도달 판정
            if curr_r == target_r and curr_c == target_c:
                # 마지막 포인트였다면 Lazy Delete 대상에 추가
                if goal_idx == len(routes[i]) - 1:
                    arrived_set.add(i)
                else:
                    robots[i][2] += 1 # 다음 목적지로 인덱스 증가
        
        # [Step 3] 현재 초의 충돌 횟수 계산
        tick_counts = Counter(current_tick_positions)
        for c in tick_counts.values():
            if c >= 2:
                collision_count += 1
                
    return collision_count