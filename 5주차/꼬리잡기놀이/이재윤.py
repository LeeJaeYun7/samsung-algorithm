from collections import deque 

N, M, K = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dx2 = [0, -1, 0, 1]
dy2 = [1, 0, -1, 0]

teamInfo = [] 

board = [] 

point = 0 
round = 1 


for i in range(N):
    row = list(map(int, input().split()))
    board.append(row) 




def makeTeam(x, y):
    
    visited = [[False]*N for _ in range(N)]
    
    team = []
    q = deque() 
    team.append([x, y, 1])
    q.append([x,y])
    visited[x][y] = True
    
    firstFind = False
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<N and 0<=ny and ny<N and visited[nx][ny] == False and board[nx][ny] == 2:
                visited[nx][ny] = True
                q.append([nx,ny])
                team.append([nx, ny, board[nx][ny]])
                firstFind = True
                
        if firstFind == True:
            break 
    
    while q:
        
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<N and 0<=ny and ny<N and visited[nx][ny] == False and (board[nx][ny] == 2 or board[nx][ny] == 3):
                visited[nx][ny] = True
                q.append([nx,ny])
                team.append([nx, ny, board[nx][ny]])
                
                
    teamInfo.append(team)    
        



def initialize():
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                makeTeam(i, j)
    
    
    
    
def move(team):
    
    
    
    cx = 0
    cy = 0 
    
    for i in range(len(team)):
        
        x = team[i][0]
        y = team[i][1]
        num = team[i][2] 
        
        
        if i == 0:
            
            cx = x
            cy = y
            
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                
                if 0<=nx and nx < N and 0<=ny and ny<N and (board[nx][ny] == 3 or board[nx][ny] == 4):
                    team[i][0] = nx
                    team[i][1] = ny
            
       
        else:
           
           sx = team[i][0]
           sy = team[i][1]
           
           team[i][0] = cx
           team[i][1] = cy
           
           cx = sx
           cy = sy 
           
           
    
    
    
def moveAll(): 
    
    
    for i in range(M):
        team = teamInfo[i]
        move(team)
    
    
def update(team):
    
    for x,y,num in team:
        board[x][y] = num 
    
    
def updateBoard(): 
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 3:
                board[i][j] = 4
                
                
    for i in range(M):
        team = teamInfo[i]
        update(team)
        
    
def updateBoardAfterReverse(num):
    
    for i in range(M):
        if i == num:
            team = teamInfo[i]
            update(team)
    
    
def printBoard(): 
    
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=' ')
        print('', end='\n')
    print('', end='\n')
    
    
def throwBall(sx, sy, dir):
    
    
    while True:
        
        if 1<=board[sx][sy] and board[sx][sy]<=3:
            return sx, sy
        else:
            nx = sx + dx2[dir]
            ny = sy + dy2[dir]
            
            if 0<=nx and nx<N and 0<=ny and ny<N:
                sx = nx
                sy = ny
            else:
                break
            
    
    return -1, -1 
    
    
    
def findStartPoint():
    
    global round 
    ## print("Round는?")
    ## print(round)
    
    curr = round % (N*4)
    
    sx = 0
    sy = 0
    dir = 0 
    
    
    if 1<=curr and curr<=N:
        sx = 0
        sy = 0
        dir = 0 
        gap = curr-1
        sx += gap
        
        
    elif (N+1)<=curr and curr<=2*N:
        
        sx = N-1
        sy = 0
        dir = 1 
        gap = curr-(N+1)
        sy += gap 
        
    elif 2*N+1<=curr and curr<=3*N:
        
        sx = N-1
        sy = N-1
        dir = 2 
        gap = curr-(2*N+1)
        sx -= gap
        
        
    elif curr == 0 or (3*N+1<=curr and curr<=4*N-1):
        
        if curr == 0:
            sx = 0
            sy = 0
            dir = 3
        else:
            sx = 0
            sy = N-1
            dir = 3 
            gap = curr-(3*N+1)
            sy -= gap 
    
    
    return sx, sy, dir
    
    
    
def findOrder(fx, fy):
    
    ## print(fx, fy)
    
    teamNum = 0
    order = 0 
    
    
    for i in range(len(teamInfo)):
        team = teamInfo[i]
        
        for j in range(len(team)):
            x = team[j][0]
            y = team[j][1] 
            
            if x == fx and y == fy:
                teamNum = i
                order = j+1
    
    
    return teamNum, order
    
    
def reverseTeam(num):
    
    for i in range(len(teamInfo)):
        if i == num:
            teamLen = len(teamInfo[i])
            teamInfo[i] = teamInfo[i][::-1]
            teamInfo[i][0][2] = 1
            teamInfo[i][teamLen-1][2] = 3
            break
    
    
initialize()


while True:
     
    moveAll()
    
    updateBoard()
    
    sx, sy, dir = findStartPoint()
    fx, fy = throwBall(sx, sy, dir)
    
    if not (fx == -1 and fy == -1):
        num, order = findOrder(fx, fy)
        point += order*order
        reverseTeam(num)
        updateBoardAfterReverse(num)
        
    if round == K:
        break
    else:
        round += 1


print(point)
