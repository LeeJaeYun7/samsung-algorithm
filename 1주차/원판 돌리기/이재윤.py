N, M, T = map(int, input().split())

board = []

zeroRow = [0]*M
board.append(zeroRow)


for i in range(N):
    
    row = list(map(int, input().split()))
    board.append(row)

## print(board)
    
rotations = []

for i in range(T):
    info = list(map(int, input().split()))
    rotations.append(info)
    
    
## 원판 row를 d방향으로 k만큼 회전시킨다 
def rotate(row, d, k):
    
    tmpRow = [0]*M
    
    for i in range(M):
        num = row[i]
        pos = 0 
        
        if d == 0:
            pos = (i+k)%M
        elif d == 1:
            nextPos = i-k
            
            if i-k<0:
                nextPos += M
            pos = nextPos
    
        tmpRow[pos] = num
        
        
    for i in range(M):
        row[i] = tmpRow[i]
        


def check(board):
    
    sum = 0 
    deleteBoard = [[False]*M for _ in range(N+1)]
    
    
    for i in range(1, N+1):
        for j in range(M):
            if board[i][j] == -1000:
                deleteBoard[i][j] = True
    
    cnt = 0 
    
    ## 같은 원판 내에서 인접한 것을 찾아서 True 처리한다 
    for i in range(1, N+1):
        for j in range(M):
            
            if j == 0:
                a = M-1
                b = 0
            else:    
                a = j-1
                b = j
                
            
            if board[i][a] == board[i][b] and board[i][a] != -1000 and board[i][b] != -1000:
                cnt += 2
                deleteBoard[i][a] = True
                deleteBoard[i][b] = True
                
    ## 인접한 원판에서 인접한 것을 찾아서 True 처리한다. 
    for j in range(M):
        for i in range(1, N):
            if board[i][j] == board[i+1][j] and board[i][j] != -1000 and board[i+1][j] != -1000:
                cnt += 2
                deleteBoard[i][j] = True
                deleteBoard[i+1][j] = True
    
    
    valid = 0 
    
    if cnt == 0:
        for i in range(1, N+1):
            for j in range(M):
                if deleteBoard[i][j] == False:
                    sum += board[i][j]
                    valid += 1 
                    
        if valid != 0:
            avg = sum / valid
        
            for i in range(1, N+1):
                for j in range(M):
                    if deleteBoard[i][j] == False:
                        if board[i][j] < avg:
                            board[i][j] += 1 
                        elif board[i][j] > avg:
                            board[i][j] -= 1 
    
        
    sum = 0 
    
    ## deleteBoard에서 False인것들만을 더해준다. 
    for i in range(1, N+1):
        for j in range(M):
            if deleteBoard[i][j] == False:
                sum += board[i][j]
            else:
                board[i][j] = -1000
                
    
    return sum 
        
            
for data in rotations:
    
    x = data[0]
    d = data[1]
    k = data[2] 
    
    ## x의 배수인 원판을 d방향으로 k만큼 회전시킨다 
    for i in range(1, N+1):
        if i % x == 0:
            rotate(board[i], d, k)
            
    ## for i in range(1, N+1):
    ##    print(board[i])
            
    ## board의 전체 합을 구한다         
    sum = check(board)
    ##print("체크 후")
    ##for i in range(1, N+1):
    ##    print(board[i])
    
    
    
print(sum)
