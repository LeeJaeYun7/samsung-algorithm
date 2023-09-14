N, M = map(int, input().split())

board = [] 
moves = [] 

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx2 = [1, 1, -1, -1]
dy2 = [1, -1, -1, 1]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
for i in range(M):
    d, s = map(int, input().split())
    moves.append((d,s))
    

clouds = [] 

clouds.append((N-2,0))
clouds.append((N-2,1))
clouds.append((N-1,0))
clouds.append((N-1,1))


for i in range(M):
    
    d, s = moves[i][0], moves[i][1] 
    movedClouds = [] 
    nextClouds = [] 
    
    
    for x, y in clouds: 
        
        nx = 0
        ny = 0 
        
        for j in range(s):
            nx = x + dx[d-1]
            ny = y + dy[d-1]
            
            if nx == -1:
                nx += N 
            if nx == N:
                nx = 0 
            if ny == -1:
                ny += N
            if ny == N:
                ny = 0 
                
            x = nx
            y = ny 
            
        
        movedClouds.append((x,y))
        
    
    for x, y in movedClouds:
        board[x][y] += 1
        
        
        
    for x, y in movedClouds:
        
        for j in range(4):
            nx = x + dx2[j]
            ny = y + dy2[j]
            
            if 0<=nx and nx < N and 0<=ny and ny < N and board[nx][ny] >= 1:
                board[x][y] += 1 
        
        
    for j in range(N):
        for k in range(N):
            if board[j][k] >= 2:
                if (j, k) in movedClouds:
                    continue
                else:
                    board[j][k] -= 2 
                    nextClouds.append((j, k))            
        
    clouds.clear()
    
    for x, y in nextClouds:
        clouds.append((x,y))
        
      

sum = 0

for i in range(N):
    for j in range(N):
        sum += board[i][j]
        
        
print(sum)





