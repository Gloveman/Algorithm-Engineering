'''
문제 발상: '어디서부터' 회전을 시작할것인가?
반복문으로 한 경우 주어진 케이스는 통과했어나 제출 시 하나도 통과하지 못했다.
문제점을 확인해 보자.
'높은 곳'에서 '낮은 곳'으로 가는 것은 잘 구현했으나, '낮은 곳'에서 '높은 곳'으로 가는 로직에 문제가 있어 보인다.
반복문에서 틀린 이유는 '대입하는 값은 곧 사라질 값이어야만 한다'라는 것을 생각하지 않았기 때문이다.
행을 고정하고, 열을 작은 순에서 큰 순서로 탐색하는 것 자체가 이미 시계 방향이 아니다. 이 경우 앞 순서에서 덮어씌워진 값이
그 다음에 또 영향을 미쳐 버린다. 따라서, 항상 대입의 흐름이 시계 방향이 되어야 하는 것이다.
즉, 매번 어떻게 값이 대입되는지 직접 해보기만 했어도 빠르게 수정이 가능한 문제였다.
또한, y에서의 이동은 열 이동이므로 list slicing도 적용 가능하다. 이 경우 처음에 temp로 저장할 필요도 없다.
'''
def solution(rows, columns, queries):
    Grid = [[(j+1)+columns * i for j in range(columns)] for i in range(rows)] #Grid 구축
    answer = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1 # 0 index 맞춤
        min_val = temp = Grid[x1][y1]
        #row = x2 -> x1, col = y1
        for x in range(x1, x2):
            min_val = min(min_val, Grid[x+1][y1])
            Grid[x][y1] = Grid[x+1][y1]
        #row = x2, col = y2 -> y1
        for y in range(y1, y2):
            min_val = min(min_val, Grid[x2][y+1])
            Grid[x2][y] = Grid[x2][y+1]
        #row = x1 -> x2, col = y2
        for x in range(x2, x1, -1):
            min_val = min(min_val, Grid[x-1][y2])
            Grid[x][y2] = Grid[x-1][y2]
        #row = x1, col = y1+1 -> y2
        for y in range(y2, y1+1, -1):
            min_val = min(min_val, Grid[x1][y-1])
            Grid[x1][y] = Grid[x1][y-1]
        # 마지막에 x1, y1 자리 값 옮기기
        Grid[x1][y1+1] = temp
        answer.append(min_val)
    return answer

def solution(rows, columns, queries):
    Grid = [[(j+1)+columns * i for j in range(columns)] for i in range(rows)] #Grid 구축
    answer = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1 # 0 index 맞춤
        up_row, down_row = Grid[x1][y1:y2], Grid[x2][y1+1:y2+1]
        min_val = min(up_row+down_row)
        #row = x2 -> x1, col = y1
        for x in range(x1, x2):
            
            Grid[x][y1] = Grid[x+1][y1]
            min_val = min(min_val, Grid[x+1][y1])
        #row = x1 -> x2, col = y2
        for x in range(x2, x1, -1):
            min_val = min(min_val, Grid[x-1][y2])
            Grid[x][y2] = Grid[x-1][y2]
        Grid[x1][y1+1:y2+1], Grid[x2][y1:y2] = up_row, down_row
        answer.append(min_val)
    return answer