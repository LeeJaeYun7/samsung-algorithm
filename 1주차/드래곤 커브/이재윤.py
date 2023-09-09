N = int(input())


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

board = [[False]*101 for _ in range(101)]

for i in range(N):
    x, y, d, g = map(int, input().split())
    
    
    board[x][y] = True 
    
    dList = [] 
    ndList = [] 
    dList.append(d)
    ndList.append(d)
    
    curr = 0
    
    
    while True:
        
            
        dListLen = len(dList)
        ndListLen = len(ndList)
    
    
        for i in range(ndListLen):
            
            d = ndList[i]
            
            nx = x + dx[d]
            ny = y + dy[d]
            
            board[nx][ny] = True
            x = nx
            y = ny 
            
        
        ndList.clear()
        
        for i in range(dListLen-1, -1, -1):
            
            d = dList[i]
            nd = 0 
            
            if d == 0:
                nd = 1
            elif d == 1:
                nd = 2
            elif d == 2:
                nd = 3
            elif d == 3:
                nd = 0
                
            ndList.append(nd)
        
        
        for d in ndList:
            dList.append(d)
            
        if curr == g:
            break
        else:
            curr += 1 
            
            
            
ans = 0 
            
for i in range(0, 100):
    for j in range(0, 100):
        if board[i][j] == True and board[i+1][j] == True and board[i][j+1] == True and board[i+1][j+1] == True:
            ans += 1 
        
    
print(ans)
    
    
    
    
    
    
    
    
    
    
