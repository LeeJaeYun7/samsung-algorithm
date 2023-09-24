from collections import deque 
import copy

N, Q = map(int, input().split())

board = [] 

for i in range(2**N):
    row = list(map(int, input().split()))
    board.append(row)
    
magics = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

biggestIce = 0
iceCnt = 0 

visited = [[False]*(2**N) for _ in range(2**N)]


def rotate(sx, sy, divideLen, tmpBoard):
    
    
    cnt = divideLen // 2 
    
    
    for i in range(cnt):
    
        x = sx + i
        y = sy + i 
        dir1 = 1 
        
        len = divideLen-2*i
        cnt = divideLen-2*i-1
    
        csx = x
        csy = y 
        
    
        while True:
            
            move = 0 
            dir2 = dir1 
            
            cx = csx
            cy = csy 
            
            
            while move != cnt:
                
                nx = cx + dx[dir2]
                ny = cy + dy[dir2]
            
            
                if sx+i<=nx and nx<sx+i+len and sy+i<=ny and ny<sy+i+len:
                    cx = nx
                    cy = ny 
                else:
                    dir2 = (dir2+1) % 4
                
                    nx = cx + dx[dir2]
                    ny = cy + dy[dir2]
                
                    cx = nx
                    cy = ny 
                
                move +=1 
                
                
            tmpBoard[cx][cy] = board[csx][csy]
                
                    
            ncsx = csx + dx[dir1]
            ncsy = csy + dy[dir1]
            
            if sx+i<=ncsx and ncsx<sx+i+len and sy+i<=ncsy and ncsy<sy+i+len:
                csx = ncsx
                csy = ncsy 
            else:
                dir1 = (dir1+1) % 4
                ncsx = csx + dx[dir1]
                ncsy = csy + dy[dir1]
                
                csx = ncsx
                csy = ncsy
                
            if csx == x and csy == y:
                break
            
    
        
    for i in range(sx, sx+divideLen):
        for j in range(sy, sy+divideLen):
            board[i][j] = tmpBoard[i][j]
    
    
def melt(tmpBoard):
    
    global board
    
    
    for i in range(0, 2**N):
        for j in range(0, 2**N):
            ice = board[i][j] 
            cnt = 0 
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if 0<=nx and nx < 2**N and 0<=ny and ny<2**N:
                    if board[nx][ny] > 0:
                        cnt += 1 
                else:
                    continue
                
            
            if cnt >= 3:
                tmpBoard[i][j] = ice
                continue
            else:
                if ice >= 1:
                    tmpBoard[i][j] = ice - 1 
                
                
    board = copy.deepcopy(tmpBoard)
            
            
            
def getIceSum():
    
    sum = 0 
    
    for i in range(0, 2**N):
        for j in range(0, 2**N):
            sum += board[i][j] 
            
            
    return sum 
    



def divide(x, y, boardLen, divideLen, tmpBoard):
    
    
    if boardLen == divideLen:
        rotate(x, y, divideLen, tmpBoard)
        return 
    
    
    divide(x, y, boardLen//2, divideLen, tmpBoard)
    divide(x+boardLen//2, y, boardLen//2, divideLen, tmpBoard)
    divide(x, y+boardLen//2, boardLen//2, divideLen, tmpBoard)
    divide(x+boardLen//2, y+boardLen//2, boardLen//2, divideLen, tmpBoard)
    


for L in magics:
    
    
    if L != 0:
        tmpBoard = [[0]*(2**N) for _ in range(2**N)]
        divide(0, 0, 2**N, 2**L, tmpBoard)    
    
    tmpBoard = [[0]*(2**N) for _ in range(2**N)]    
    melt(tmpBoard)
    total = getIceSum()


    
total = getIceSum()


def bfs(x, y, visited):
    
    global iceCnt 
    
    visited[x][y] = True
    iceCnt += 1
    q = deque()
    q.append([x,y])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<2**N and 0<=ny and ny<2**N and board[nx][ny] != 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                iceCnt += 1 
                q.append([nx, ny])
    


for i in range(2**N):
    for j in range(2**N):
        if board[i][j] != 0 and visited[i][j] == False:
            iceCnt = 0 
            bfs(i, j, visited)
            biggestIce = max(biggestIce, iceCnt)


    
print(total) 
print(biggestIce)
