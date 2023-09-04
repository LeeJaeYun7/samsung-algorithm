// 푸는 중 

N, M, T = map(int, input().split())

board = []

zeroRow = [0]*M
board.append(zeroRow)


for i in range(N):
    
    row = list(map(int, input().split()))
    board.append(row)

print(board)
    
rotations = []

for i in range(T):
    info = list(map(int, input().split()))
    rotations.append(info)
    
    
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
            
            if j == 0:
                a = M-1
                b = 0
            else:    
                a = j-1
                b = j
                
            
            if board[i][a] == board[i][b]:
                deleteBoard[i][a] = True
                deleteBoard[i][b] = True
                
                
    
    for j in range(M):
        for i in range(1, N):
            if board[i][j] == board[i+1][j]:
                deleteBoard[i][j] = True
                deleteBoard[i+1][j] = True
                
                
    for i in range(1, N+1):
        for j in range(M):
            if deleteBoard[i][j] == False:
                sum += board[i][j]
                
    
    return sum 
        
            
for data in rotations:
    
    x = data[0]
    d = data[1]
    k = data[2] 
    
    for i in range(1, N+1):
        if i % x == 0:
            rotate(board[i], d, k)
            
            
    sum = check(board)
    for i in range(1, N+1):
        print(board[i])
    
    
    print(sum)
