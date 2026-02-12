'''
우선, 문자열로 주어지므로 이를 파싱할 방법이 필요.
또한 어떻게 순서를 찾을지 고민한다.
우선, replace를 통해 모든 중괄호를 제거하고, 쉽표로 분리하여 숫자들을 얻고 Counter 객체로 빈도수를 구했다.
빈도수가 높은 것일수록 앞에 위치하므로, 정렬을 통해 답을 구했다.
그러나 s의 길이가 긴 만큼 정렬을 하는 것보다 최적화된 풀이를 확인해 보았다.
1. 정규식 활용하기
문자열에 있어 정규식을 쓰면 '숫자인 원소'만 빠르게 뽑아낼 수 있다.
2. 이미 결정된 index
애초에 freq를 아는 순간 tuple에서의 index도 정해져 있다.
'''
#초기 풀이
from collections import Counter

def solution(s):
    s=s[1:-1]
    s=s.replace('{',"")
    s=s.replace('}',"")
    count_s = Counter(list(s.split(',')))
    return [int(c) for c in sorted(count_s, key=lambda x:-count_s[x])]

# 정렬 대신 인덱스 바로 구하기
def solution(s):
    s=s[1:-1]
    s=s.replace('{',"")
    s=s.replace('}',"")
    count_s = Counter(list(s.split(',')))
    n = len(count_s)
    answer = [0] * n
    for c, freq in count_s.items():
        # freq = 1 ~ n
        answer[n-freq] = int(c)
    return answer 

# 정규식까지.

import re
def solution(s):
    nums = re.findall(r'\d+', s)
    count_s = Counter(nums)

    n = len(count_s)
    answer = [0] * n
    
    for c, freq in count_s.items():
        answer[n - freq] = int(c)
        
    return answer