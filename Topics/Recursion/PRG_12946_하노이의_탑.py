'''
대표적인 재귀 문제 중 하나인 하노이의 탑 문제
시작 지점, 중간 지점, 종료 지점으로 나누어 생각
원판 하나 : 시작 지점 -> 종료 지점으로 바로 이동 (base 조건)
원판 둘(문제 예시) : 시작 지점 -> 중간 지점 / 시작 지점 -> 종료 지점 / 중간 지점 -> 종료 지점
이들 각각은 base case에서 시작과 끝만 바뀐 것이다.
이를 n개로 확장해 생각해 보자.
n개의 원판을 옮길 때, 결국 맨 마지막 n번째를 제외한 n-1번째를 중간 지점으로 옮겨놓고
n번째 원판을 종료 지점으로 옮긴다. 이후 중간 지점의 n-1개를 종료 지점으로 옮기면 된다.
이것은, 시작-> 중간으로 n-1개의 원판 옮기기를 하고, 시작 -> 종료로 base case를 수행한 뒤
다시 중간 -> 종료로 n-1개 옮기기를 수행하는 것과 같다.
이를 그대로 재귀로 옮기면 아래 답안이 나오게 된다.

nonlocal 대신 answer 배열 자체를 재귀 함수의 인수로 넣는 것이 closure의 특징을 살리는 것이긴 하다.
'''
def solution(n):
    answer = []
    def solve_hannoi(cur_n, start, inter, end):
        nonlocal answer
        if cur_n == 1:
            answer.append([start, end])
            return
        solve_hannoi(cur_n-1,start,end, inter)
        #solve_hannoi(1, start, inter, end)
        answer.append([start, end])
        solve_hannoi(cur_n-1, inter, start, end)
    solve_hannoi(n, 1, 2, 3)
    return answer

print(solution(3))
