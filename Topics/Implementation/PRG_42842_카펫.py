'''
X, Y를 각각 yellow 부분의 두 변으로 두었다.
brown과 yellow의 조건이 주어질 때  이것을 X와 Y에 대한 식으로 둔다.
이러면 가로 + 세로와 가로*세로에 대한 값을 brown과 yellow로 표현 가능하다.
이제 x를 증가시키며 곱이 만족하는 경우를 찾는다.

'''
def solution(brown, yellow):
    #2(가로세로합)+4 = brown
    #가로 * 세로 = yellow
    #가로가 항상 길거나 같음
    sum_xy = int((brown-4)/2)
    x = y = 0
    for x in range(1,sum_xy):
        y = sum_xy - x
        if x * y == yellow:
            break
    return [max(x,y)+2,min(x,y)+2]