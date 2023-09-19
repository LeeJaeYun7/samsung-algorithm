import copy 

N, M, K = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dice = [[0]*3 for _ in range(4)]


dice[0][1] = 2
dice[1][0] = 4
dice[1][1] = 1
dice[1][2] = 3
dice[2][1] = 5
dice[3][1] = 6

board = [] 

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
x = 0
y = 0 
dir = 1 
totalPoint = 0     

count = 0 


def changeDice(dir):
    
    global dice
    
    tmpDice = [[0]*3 for _ in range(4)]
  
    
    if dir == 0:
        tmpDice[0][1] = dice[1][1]
        tmpDice[1][0] = dice[1][0]
        tmpDice[1][1] = dice[2][1]
        tmpDice[1][2] = dice[1][2]
        tmpDice[2][1] = dice[3][1]
        tmpDice[3][1] = dice[0][1]
        
    elif dir == 1:
        tmpDice[0][1] = dice[0][1]
        tmpDice[1][0] = dice[3][1]
        tmpDice[1][1] = dice[1][0]
        tmpDice[1][2] = dice[1][1]
        tmpDice[2][1] = dice[2][1]
        tmpDice[3][1] = dice[1][2]
        
    elif dir == 2:
        tmpDice[0][1] = dice[3][1]
        tmpDice[1][0] = dice[1][0]
        tmpDice[1][1] = dice[0][1]
        tmpDice[1][2] = dice[1][2]
        tmpDice[2][1] = dice[1][1]
        tmpDice[3][1] = dice[2][1]
    
    elif dir == 3:
        
        tmpDice[0][1] = dice[0][1]
        tmpDice[1][0] = dice[1][1]
        tmpDice[1][1] = dice[1][2]
        tmpDice[1][2] = dice[3][1]
        tmpDice[2][1] = dice[2][1]
        tmpDice[3][1] = dice[1][0]
        
      
    
    dice = copy.deepcopy(tmpDice) 

      
      
def dfs(num, x, y, visited):
    
    global count
    
    visited[x][y] = True
    count += 1 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx and nx<N and 0<=ny and ny<M and board[nx][ny] == num and visited[nx][ny] == False:
            dfs(num, nx, ny, visited)
    
    
    
    
for i in range(K):
    
    
    
    nx = x + dx[dir]
    ny = y + dy[dir] 
    
    
    if not (0<=nx and nx < N and 0<=ny and ny < M):
        
        nx -= dx[dir]
        ny -= dy[dir]
        
        if dir == 0:
            dir = 2
        elif dir == 1:
            dir = 3
        elif dir == 2:
            dir = 0
        elif dir == 3:
            dir = 1 
            
        
        nx += dx[dir]
        ny += dy[dir]
    
        
    changeDice(dir)
    

    A = dice[3][1]
    B = board[nx][ny] 
    
    
    point = B
    count = 0 
    visited = [[False]*M for _ in range(N)]
    
    dfs(B, nx, ny, visited)
    
    
    point *= count
    
    totalPoint += point
    
    
    if A > B:
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 3
        elif dir == 3:
            dir = 0 
        
    elif A < B:
    
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 1
        elif dir == 3:
            dir = 2 
            
            
    
    x = nx
    y = ny 
    
    
    
print(totalPoint)
    
    
    




