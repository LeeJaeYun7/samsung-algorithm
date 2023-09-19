import copy

r, c, k = map(int, input().split())

board = [] 

for i in range(3):
    
    row = list(map(int, input().split()))
    board.append(row) 
    
    
    
    
time = 0 


def sortRow(R, C):
    
    global board 

    tmpBoard = [] 
    maxLen = -int(1e9)
    
    for i in range(R): 
        
        count = [0]*101
        info = []
        row = [] 
        
        for j in range(C):
            num = board[i][j]
            count[num] += 1
            
        
        for j in range(1, 101):
            if count[j] != 0:
                info.append([j, count[j]])
                
        info.sort(key=lambda x: [x[1], x[0]])
        
        for x, y in info:
            row.append(x)
            row.append(y)
            
            if len(row) == 100:
                break
            
        maxLen = max(maxLen, len(row))
        tmpBoard.append(row) 
        
    
    for i in range(R):
        tmpRow = tmpBoard[i]
        
        gap = maxLen - len(tmpRow)
        
        for j in range(gap):
            tmpBoard[i].append(0)
            
    
    
    board = copy.deepcopy(tmpBoard)
        
    


def sortCol(R, C):
    
    global board
    
    tmpBoard = [] 
    tmpBoard2 = [] 
    maxLen = -int(1e9)
    
    for j in range(C):
        
        count = [0]*101
        info = []
        col = [] 
        
        for i in range(R):
            num = board[i][j] 
            count[num] += 1 
            
    
        for j in range(1, 101):
            if count[j] != 0:
                info.append([j, count[j]])
                
        info.sort(key=lambda x: [x[1], x[0]])
        
        for x, y in info:
            col.append(x)
            col.append(y)
            
            if len(col) == 100:
                break 
            
        maxLen = max(maxLen , len(col))
        tmpBoard.append(col)
        
        
    for j in range(C):
        tmpCol = tmpBoard[j]
        gap = maxLen - len(tmpCol)
        
        for i in range(gap):
            tmpBoard[j].append(0)
            
    rr = len(tmpBoard)
    cc = len(tmpBoard[0])


    for j in range(cc):
        col = [] 
        for i in range(rr):
            col.append(tmpBoard[i][j])
        
        tmpBoard2.append(col)
        
        
        
        
    board = copy.deepcopy(tmpBoard2) 
        



while True: 
    
    
    R = len(board)
    C = len(board[0])
    
    if 0<=r-1 and r-1<R and 0<=c-1 and c-1<C and board[r-1][c-1] == k or time == 101:
        break
    
    
    
    if R >= C:
        sortRow(R, C)
    else:
        sortCol(R, C)
    
    
    R2 = len(board)
    C2 = len(board[0])
    time += 1 
        
if time != 101:
    print(time)
else:
    print(-1)
        
        
        
        
