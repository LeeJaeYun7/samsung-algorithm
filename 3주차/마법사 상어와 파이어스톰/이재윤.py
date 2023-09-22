N, Q = map(int, input().split())

board = [] 

for i in range(2**N):
    row = list(map(int, input().split()))
    board.append(row)
    
magics = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate(sx, sy, divideLen):
    
    
    cnt = divideLen // 2 
    
    tmpBoard = [[0]*2**N for _ in range(2**N)]
    
    
    for i in range(cnt):
    
        x = sx + i
        y = sy + i 
        dir = 1 
        
    
        while True:
            
            nx = x + dx[dir]
            ny = y + dy[dir]
            
            if sx+i<=nx and nx<sx+i+(divideLen//(i+1)) and sy+i<=ny and ny<sy+i+(divideLen//(i+1)):
                tmpBoard[nx][ny] = board[x][y]
                x = nx
                y = ny 
            else:
                dir = (dir+1) % 4
                
                nx = x + dx[dir]
                ny = y + dy[dir]
                
                tmpBoard[nx][ny] = board[x][y]
        
                x = nx
                y = ny 
                    
            if x == (sx+i) and y == (sy+i):
                break
            
    
        
    for i in range(sx, sx+divideLen):
        for j in range(sy, sy+divideLen):
            board[i][j] = tmpBoard[i][j]
    
    
def melt():
    
    tmpBoard = [[0]*2**N for _ in range(2**N)]
    
    
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
                tmpBoard[i][j] = ice - 1 
                
    for i in range(0, 2**N):
        for j in range(0, 2**N):
            board[i][j] = tmpBoard[i][j]
            
            
            
def getIceSum():
    
    sum = 0 
    
    for i in range(0, 2**N):
        for j in range(0, 2**N):
            sum += board[i][j] 
            
            
    return sum 
    



def divide(x, y, boardLen, divideLen):
    
    
    if boardLen == divideLen:
        rotate(x, y, divideLen)
        return 
    
    
    divide(x, y, boardLen//2, divideLen)
    divide(x+boardLen//2, y, boardLen//2, divideLen)
    divide(x, y+boardLen//2, boardLen//2, divideLen)
    divide(x+boardLen//2, y+boardLen//2, boardLen//2, divideLen)
    


for L in magics:
    print("이전")
    
    for i in range(2**N):
        for j in range(2**N):
            print(board[i][j], end=' ')
        print('', end='\n')
    print('', end='\n')
    
    if L != 0:
        divide(0, 0, 2**N, 2**L)    
        
    
    print("이후")
    
    for i in range(2**N):
        for j in range(2**N):
            print(board[i][j], end=' ')
        print('', end='\n')
    print('', end='\n')
        
    
    melt()
    
     
    print("녹은 이후")
    
    for i in range(2**N):
        for j in range(2**N):
            print(board[i][j], end=' ')
        print('', end='\n')
    print('', end='\n')
    
    
    total = getIceSum()
    
    print("total은?")
    print(total)
    

for i in range(2**N):
    for j in range(2**N):
        print(board[i][j], end=' ')
    print('', end='\n')
    
    
    
total = getIceSum()
    
print(total) 



