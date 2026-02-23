"""
n개의 퍼즐

diff <= level : 안틀림, time_cur동안 완성
diff > level: 총 diff-level번 틀림, 틀리는 경우에는 time_cur에 더해 time_prev 추가로
다 틀린 이후에 time_cur로 해결
제한 시간안에 해결하는 숙련도의 최솟값.
숙련도는 양의 정수
이분 탐색 활용.

개선점
- level_test에서 마지막에 elapsed와 limit을 비교하는 대신, 매번 초과 여부를 검증하여 False 조기 리턴 적용 가능
- 이때는 loop가 종료되면 무조건 true를 반환하면 됨
"""
def level_test(level, diffs, times, limit):
    N = len(diffs)
    elapsed = 0
    for i in range(N):
        if diffs[i] <= level:
            elapsed += times[i]
        else:
            elapsed += (times[i] + times[i-1]) * (diffs[i] - level) 
            elapsed += times[i]
    return elapsed <= limit
def solution(diffs, times, limit):
    min_level = diffs[0]
    max_level = 100000
    answer = 0
    while min_level <=max_level:
        cur_level = (max_level+min_level+1)//2
        if level_test(cur_level, diffs, times, limit):
            answer = cur_level
            max_level = cur_level -1
        else:
            min_level = cur_level + 1
    return answer

#수정된 level_test
def level_test(level, diffs, times, limit):
    N = len(diffs)
    elapsed = 0
    for i in range(N):
        if diffs[i] <= level:
            elapsed += times[i]
        else:
            elapsed += (times[i] + times[i-1]) * (diffs[i] - level) 
            elapsed += times[i]
        if elapsed >limit:
            return False
    return True