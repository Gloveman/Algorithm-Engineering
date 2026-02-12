'''
처음 접근 시
원래 실제로 만들어서 구하려고 했지만, Tree의 성질을 사용하여 수식적으로 구하는 접근을 택했다.
다만, 해당 식을 혼자서 세우지 못해서 식 부분을 다시 확인해야 한다. 
핵심은, 해당 노드 전에 ‘몇 개의 노드를 건너뛰는가’ 를 일관된 점화식으로 표현할 수 있다는 것이다. 

Tree로 표현이 가능하다는 것은 곧 재귀로 해결이 가능하다는 것이다.
두 번재 풀이에서는 재귀 함수를 이용하여 풀이에 도전했다.
원래는 해당 단어를 input으로 하여 한 글자씩 줄여 나가며 종료하는 재귀를 생각했으나,
이것을 구현하려면 결국 등비수열 방식을 생각해야 했다. 따라서,해당 단어에 도달할 때까지 재귀적으로
사전을 직접 만드는 방식으로 선회했다.
정리한 논리 흐름은 다음과 같다.
find_word(current_word)
count를 1 증가시킨다 (새로운 단어 방문).
만약 current_word가 target과 같다면:
    지금까지의 count를 정답으로 확정하고 모든 재귀를 종료한다.
만약 current_word의 길이가 5라면:
    더 이상 탐색할 수 없으므로 이전 상태로 복귀한다.
모음 리스트 ['A', 'E', 'I', 'O', 'U']에서 문자 char를 하나씩 꺼낸다.
    find_word(current_word + char)를 호출한다.
    (만약 정답을 찾았다면 즉시 루프를 멈추고 탈출한다.)
이를 해결하기 위해서는 가장 처음 호출시에도(공백) +1이 되므로 count를 -1에서 시작하는 trick이 필요했다.
또한, max len에 도달했을때 불가능하면 False를, 정답을 찾은 경우는 True를 반환하도록 하며,
정답을 못 찾은 경우 계속 내려가다, False 혹은 True를 그대로 반환하게 된다.
이 코드는 다시 확인할 필요가 있다.
'''
def solution(word):
    count = -1
    answer = 0
    vowel = ["A", "E", "I", "O", "U"]
    def make_word(w):
        nonlocal count, answer
        count+=1
        if w == word:
            return True
        if len(w) == 5:
            return False
        for c in vowel:
            result = make_word(w+c)
            if result: #앞에서 잘 찾은경우
                return True
    if make_word(""):
        return count

#Tree 성질을 이용한 등비수열의 합 공식을 적용한 최초 답안
def solution(word):
    F_h = [(5**(h+1) - 1) /4 for h in range(5)]
    alpha_map = {'A':0, "E":1, "I":2, "O":3, "U":4}
    answer = 0
    for i, c in enumerate(word):
        answer += ((alpha_map[c] * F_h[5-1-i]) + 1)
    return answer