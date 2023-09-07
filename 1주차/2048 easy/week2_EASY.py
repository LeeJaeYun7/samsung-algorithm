
from copy import deepcopy

def merge(li, dir): # 이동 완료한 board에서 인접한 같은 값을 찾아서 합치기. 
    # 한번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없다!!
    # 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다. 

    if dir == 0 or dir == 2: # 위로 또는 좌로
        for i in range(len(li)-1): # li= [2,2,2,2] , i = 0,1,2
            if li[i] and li[i] == li[i+1]: 
                li[i] += li[i+1]
                li[i+1] = 0 # [4,0,2,2]

    elif dir == 1 or dir == 3: # [4,4] 
        for i in range(len(li)-1, 0, -1): # 1
            if li[i] and li[i] == li[i-1]:
                li[i] += li[i-1]
                li[i-1] = 0 
    return [x for x in li if x]


def move(board, dir): 
    if dir == 0 or dir == 1: # 상하 이동이면 -> 각 열에 대해서 처리 
        temp = [list(x) for x in zip(*board)] # transposed
        for i in range(n): 
            nonzero = [x for x in temp[i] if x]
            nonzero = merge(nonzero, dir)
            if dir == 0:
                temp[i] = nonzero + [0]*(n - len(nonzero))
            elif dir == 1:
                temp[i] = [0]*(n - len(nonzero)) + nonzero
        board = [list(x) for x in zip(*temp)] 

    elif dir == 2 or dir == 3: # 좌우 이동이면 -> 각 행에 대해서 처리 
        for i in range(n): 
            nonzero = [x for x in board[i] if x]
            if nonzero: 
                nonzero = merge(nonzero, dir)
            if dir == 2: 
                board[i] = nonzero + [0]*(n - len(nonzero))
            elif dir == 3:
                board[i] = [0]*(n - len(nonzero)) + nonzero
    return board
        

def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return 
    for i in range(4): # 상 하 좌 우 DFS 탐색
        tmp_board = move(deepcopy(board), i) # board의 원본은 그대로 유지하기 위해 deepcopy
        dfs(tmp_board, cnt + 1)

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

ans = 0
dfs(board, 0)
print(ans)