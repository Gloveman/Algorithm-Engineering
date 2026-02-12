'''
매 시행을 반복하며,
1. 모든 0 제거 => 제거된 개수 누적
2. 남은 문자열의 '길이'를 이진수로 표현한것으로 대체
[시행 횟수, 제거된 0 개수 총합] 을 반환

python 내장 함수 bin의 존재는 검색을 통해 알게 되었다.
진법 변환과 관련된 bin() oct() hex()를 기억해 두어야겠다.
이에 더하여 ascii 값을 구하는 ord(문자)와 chr(코드값) 역시 기억해 두어야겠다.
또한, 남은 문자열 자체를 사용하는 것이 아니라 길이만 사용하기 때문에,
실제로 0을 제거한 문자열을 구하는 것이 아니라 s.count("0")을 통해
제거할 0의 개수를 더 간편하게 구하는 방법이 존재했다.
'''
def solution(s):
    count = 0
    removed_zeros = 0
    while s != "1":
        s_zero_removed = s.replace('0','')
        N = len(s_zero_removed)
        removed_zeros +=len(s) - N
        s = bin(N)[2:]
        count +=1
    return [count, removed_zeros]

#s.count() 활용
def solution(s):
    count = 0
    removed_zeros = 0
    while s != "1":
        removed_zeros +=s.count("0")
        N = len(s) - s.count("0")
        s = bin(N)[2:]
        count +=1
    return [count, removed_zeros]
