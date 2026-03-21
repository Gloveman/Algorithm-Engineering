'''
연산 수식이 주어졌을 때, 연산자의 우선순위를 재정의하여 얻을 수 있는 결과의 최대 절댓값을 구함.

1. 수식 파싱(Parsing) 전략
   - 정규표현식(re.split)을 활용하여 숫자와 연산자를 분리하되, 연산자까지 리스트에 포함되도록 구성.
   - 단순 split이 아닌 캡처 그룹을 사용하여 ['100', '-', '200', '*', '300'] 형태의 리스트 확보.

2. 연산자 우선순위 생성
   - '+', '-', '*' 세 종류의 연산자로 만들 수 있는 모든 순열(3! = 6가지)을 생성.
   - 각 순위 조합에 대해 독립적인 수식 계산을 진행.

3. 리스트 기반 순차 계산 로직
   - 높은 우선순위의 연산자부터 전체 수식을 순회하며 계산.
   - 스택(Stack) 혹은 인덱스 조작을 통해 연산자 양옆의 피연산자를 계산된 결과값으로 치환.
   - 이때, 기존 수식을 보존하기 위해 각 케이스마다 슬라이싱([:])을 통한 깊은 복사 수행.

4. 결과 최적화
   - 최종 계산 결과에 abs()를 적용하여 절댓값을 취하고, 
     모든 우선순위 케이스 중 최댓값을 갱신하며 최종 우승 상금 산출.
'''

from itertools import permutations
import re

def solution(expression):
    operands = re.split(r'(\D)', expression) #숫자, 연산자 분리
    
    operators = ['+', '-', '*']
    priorities = list(permutations(operators)) #가능한 연산자 조합 생성
    
    max_reward = 0
    
    for priority in priorities:
        temp_expression = operands[:]
        
        # 우선순위가 높은 연산자부터 하나씩 처리
        for op in priority:
            stack = []
            i = 0
            while i < len(temp_expression):
                if temp_expression[i] == op: #연산자를 찾은 경우
                    # 스택에 마지막으로 담긴 이전 계산 결과와 연산자 다음 숫자를 꺼내 계산
                    prev_num = stack.pop()
                    next_num = temp_expression[i+1]
                    
                    if op == "+":
                        result = prev_num + next_num
                    elif op == '-':
                        result = prev_num - next_num
                    else:
                        result = prev_num * next_num
                    stack.append(result)
                    i += 2 # 연산자와 다음 숫자는 건너뜀
                else:
                    stack.append(temp_expression[i])
                    i += 1
            temp_expression = stack # 계산된 결과로 리스트 갱신
            
        # 모든 연산이 끝난 후 최종 결과의 절댓값 비교
        res = abs(int(temp_expression[0]))
        if res > max_reward:
            max_reward = res
            
    return max_reward