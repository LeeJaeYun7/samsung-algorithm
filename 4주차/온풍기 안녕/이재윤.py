from collections import deque 

R, C, K = map(int, input().split())

tempBoard = [[0]*C for _ in range(R)]
board = [] 
walls = [ [[[False]*C for _ in range(R)] for _ in range(C)] for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def isInside(x, y):
    if 0<=x and x<R and 0<=y and y<C:
        return True
    else:
        return False 


for i in range(R):
    row = list(map(int, input().split()))
    board.append(row)
    
    
conditioners = []
checkPoints = [] 


for i in range(R):
    for j in range(C):
        if 1<=board[i][j] and board[i][j] <= 4:
            conditioners.append([i, j, board[i][j]])
        elif board[i][j] == 5:
            checkPoints.append([i, j])
            
            
W = int(input())

for i in range(W):
    x, y, t = map(int, input().split())
    x -= 1 
    y -= 1 
    
    if t == 0:
        walls[x][y][x-1][y] = True
        walls[x-1][y][x][y] = True
    elif t == 1:
        walls[x][y][x][y+1] = True
        walls[x][y+1][x][y] = True 
        
        


def movablePoints(x, y, dir):
    
    
    points = [] 
    
    
    if dir == 0:
        
        nx1 = x + dx[dir]
        ny1 = y + dy[dir]
        
        if isInside(nx1, ny1) and walls[x][y][nx1][ny1] == False:
            points.append([nx1, ny1])

        
        nx21 = x-1
        ny21 = y
        
        nx22 = x-1
        ny22 = y+1 
        
        if isInside(nx21, ny21) and isInside(nx22, ny22) and walls[x][y][nx21][ny21] == False and walls[nx21][ny21][nx22][ny22] == False:
            points.append([nx22, ny22])
        
        
        nx31 = x+1
        ny31 = y
        
        nx32 = x+1
        ny32 = y+1 
        
        
        if isInside(nx31, ny31) and isInside(nx32, ny32) and walls[x][y][nx31][ny31] == False and walls[nx31][ny31][nx32][ny32] == False:
            points.append([nx32, ny32])
        
    
    elif dir == 1:
        
        nx1 = x + dx[dir]
        ny1 = y + dy[dir]
        
        if isInside(nx1, ny1) and walls[x][y][nx1][ny1] == False:
            points.append([nx1, ny1])

        
        nx21 = x-1
        ny21 = y
        
        nx22 = x-1
        ny22 = y-1 
        
        if isInside(nx21, ny21) and isInside(nx22, ny22) and walls[x][y][nx21][ny21] == False and walls[nx21][ny21][nx22][ny22] == False:
            points.append([nx22, ny22])
        
        
        nx31 = x+1
        ny31 = y
        
        nx32 = x+1
        ny32 = y-1 
        
        
        if isInside(nx31, ny31) and isInside(nx32, ny32) and walls[x][y][nx31][ny31] == False and walls[nx31][ny31][nx32][ny32] == False:
            points.append([nx32, ny32])
            
            
    elif dir == 2: 
        
        nx1 = x + dx[dir]
        ny1 = y + dy[dir]
        
        if isInside(nx1, ny1) and walls[x][y][nx1][ny1] == False:
            points.append([nx1, ny1])

        
        nx21 = x
        ny21 = y-1
        
        nx22 = x-1
        ny22 = y-1 
        
        if isInside(nx21, ny21) and isInside(nx22, ny22) and walls[x][y][nx21][ny21] == False and walls[nx21][ny21][nx22][ny22] == False:
            points.append([nx22, ny22])
        
        
        nx31 = x
        ny31 = y+1
        
        nx32 = x-1
        ny32 = y+1 
        
        
        if isInside(nx31, ny31) and isInside(nx32, ny32) and walls[x][y][nx31][ny31] == False and walls[nx31][ny31][nx32][ny32] == False:
            points.append([nx32, ny32])
            
        
    elif dir == 3: 
        
        nx1 = x + dx[dir]
        ny1 = y + dy[dir]
        
        if isInside(nx1, ny1) and walls[x][y][nx1][ny1] == False:
            points.append([nx1, ny1])

        
        nx21 = x
        ny21 = y-1
        
        nx22 = x+1
        ny22 = y-1 
        
        if isInside(nx21, ny21) and isInside(nx22, ny22) and walls[x][y][nx21][ny21] == False and walls[nx21][ny21][nx22][ny22] == False:
            points.append([nx22, ny22])
        
        
        nx31 = x
        ny31 = y+1
        
        nx32 = x+1
        ny32 = y+1 
        
        
        if isInside(nx31, ny31) and isInside(nx32, ny32) and walls[x][y][nx31][ny31] == False and walls[nx31][ny31][nx32][ny32] == False:
            points.append([nx32, ny32])
    
    
    
    
    return points    

        
    
    
    
    
def printBoard(board):
    
    for i in range(R):
        for j in range(C):
            print(board[i][j], end=' ')
        print('', end='\n')
    print('', end='\n')





def bfs(x, y, dir):
    
    
    tmpBoard = [[0]*C for _ in range(R)]
    
    q = deque() 
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    tmpBoard[nx][ny] = 5
    q.append([nx, ny, 5])
    
    
    while q:
        
        x, y, temp = q.popleft()
        
        if temp == 1:
            continue 
        
        points = movablePoints(x, y, dir)
        
        for x, y in points:
            if tmpBoard[x][y] == 0:
                tmpBoard[x][y] = temp-1
                q.append([x, y, temp-1])



    for i in range(R):
        for j in range(C):
            tempBoard[i][j] += tmpBoard[i][j]
    
    
    
    

def changeTemp(): 
    
    tmpBoard = [[0]*C for _ in range(R)]
    
    
    for i in range(R):
        for j in range(C):
            
            temp = tempBoard[i][j]
            
            cnt = 0 
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if isInside(nx, ny) and temp > tempBoard[nx][ny] and walls[i][j][nx][ny] == False:
                    tmpBoard[nx][ny] += ((temp-tempBoard[nx][ny]) // 4)
                    tmpBoard[i][j] -= ((temp-tempBoard[nx][ny]) // 4)
    
    
    for i in range(R):
        for j in range(C):
            tempBoard[i][j] += tmpBoard[i][j]
            
            
  


def decreaseTemp():
    
    
    for i in range(R):
        for j in range(C):
            if i == 0 or i == R-1 or j == 0 or j == C-1:
                if tempBoard[i][j] >= 1:
                    tempBoard[i][j] -= 1 
                
            
  
def checkTemp():
    
    for x, y in checkPoints:
        if tempBoard[x][y] < K:
            return False
            
            
    return True 
    
    
        
        
chocolate = 0 


while True:
    
    
    for x, y, dir in conditioners:
        bfs(x, y, dir-1)




    changeTemp() 
    
    decreaseTemp() 

    chocolate += 1 
    
    res = checkTemp() 
    
    if res == True or chocolate >= 101:
        break




print(chocolate)







    
    
    
    
    
