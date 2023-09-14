N = int(input())


tx = N // 2
ty = N // 2 

board = [] 
dx = [0, 1, 0, -1]
dy = [-1,0, 1, 0]


dx20 = [0, 1, -1, 0, 1, -1, 2, -2, 1, -1]
dy20 = [-1, -1, -1, -2, 0, 0, 0, 0, 1, 1]

dx21 = [1, 1, 1, 2, 0, 0, 0, 0, -1, -1]
dy21 = [0, -1, 1, 0, 1, -1, 2, -2, -1, 1]

dx22 = [0, -1, 1, 0, 1, -1, 2, -2, 1, -1]
dy22 = [1, 1, 1, 2, 0, 0, 0, 0, -1, -1]

dx23 = [-1,  -1, -1, -2, 0, 0, 0, 0, 1, 1]
dy23 = [0, -1, 1, 0, -1, 1, -2, 2, -1, 1] 

percent = [0.55, 0.1, 0.1, 0.05, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
moves = 1 
stage = 0 
direction = 0 

outSands = 0 




def moveSands(x, y, direction):
    
    
    global outSands
    
    print(x, y, outSands)
    
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print('', end='\n')
        
    print('', end='\n')
    
    
    sands = board[x][y]
    
    allMoveSands = 0 
    
    if direction == 0:
        for i in range(1, 10):
        
            nx = x + dx20[i]
            ny = y + dy20[i]
            
            moveSand = int(sands*percent[i])
            
            if moveSand == 0:
                continue
            
            allMoveSands += moveSand 
            
            if 0<=nx and nx<N and 0<=ny and ny<N:
                board[nx][ny] += moveSand
            else:
                outSands += moveSand
        
        board[x][y] = 0 
        if 0<=x+dx20[0] and x+dx20[0] < N and 0<=y+dy20[0] and y+dy20[0]< N:
            board[x+dx20[0]][y+dy20[0]] = sands-allMoveSands

        

    elif direction == 1:
        for i in range(1, 10):
        
            nx = x + dx21[i]
            ny = y + dy21[i]
        
        
            moveSand = int(sands*percent[i])
            
            if moveSand == 0:
                continue
            
            allMoveSands += moveSand 
            
            if 0<=nx and nx<N and 0<=ny and ny<N:
                board[nx][ny] += moveSand
            else:
                outSands += moveSand
        
        board[x][y] = 0
        if 0<=x+dx21[0] and x+dx21[0] < N and 0<=y+dy21[0] and y+dy21[0]< N:
            board[x+dx21[0]][y+dy21[0]] = sands-allMoveSands
        
        
    elif direction == 2:
        
        for i in range(1, 10):
            
            nx = x + dx22[i]
            ny = y + dy22[i]
            
            
            moveSand = int(sands*percent[i])
            
            if moveSand == 0:
                continue
            
            allMoveSands += moveSand 
            
            if 0<=nx and nx<N and 0<=ny and ny<N:
                board[nx][ny] += moveSand
            else:
                outSands += moveSand
        
        board[x][y] = 0
        if 0<=x+dx22[0] and x+dx22[0] < N and 0<=y+dy22[0] and y+dy22[0]< N:
            board[x+dx22[0]][y+dy22[0]] = sands-allMoveSands
        
    
    elif direction == 3:
        
        for i in range(10):
            
            nx = x + dx23[i]
            ny = y + dy23[i]
            
            
            moveSand = int(sands*percent[i])
            
            if moveSand == 0:
                continue
            
            allMoveSands += moveSand 
            
            if 0<=nx and nx<N and 0<=ny and ny<N:
                board[nx][ny] += moveSand
            else:
                outSands += moveSand
        
        board[x][y] = 0
        
        if 0<=x+dx23[0] and x+dx23[0] < N and 0<=y+dy23[0] and y+dy23[0]< N:
            board[x+dx23[0]][y+dy23[0]] = sands-allMoveSands







while True: 
    
    if tx == 0 and ty == 0:
        break 
    
    
    for i in range(moves):
        tx += dx[direction]
        ty += dy[direction]
    
        if board[tx][ty] != 0:
            print(tx, ty)
            moveSands(tx, ty, direction)
    
    if direction == 0:
        direction = 1
    elif direction == 1:
        direction = 2
    elif direction == 2:
        direction = 3
    elif direction == 3:
        direction = 0 
        
    if stage == 0:
        stage += 1 
        continue
    else:
        if moves <= N-2:
            moves += 1 
        stage = 0 
    
    
    
    
    
print(outSands)
    
    
    








    
    
    
    
    
