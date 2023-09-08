N, M = map(int, input().split())

board = []
cctvs = []
cctvCnt = 0 
cctvDirs = []
minInvisible = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3 or board[i][j] == 4 or board[i][j] == 5:
            cctvs.append((i,j))
            cctvCnt += 1 
        

def activate(x, y, dir, visited):
    
    visited[x][y] = True
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if 0<=nx and nx<N and 0<=ny and ny<M and board[nx][ny] != 6:
        activate(nx, ny, dir, visited)
    
    
            
            
def activateCCTV():
    
    global minInvisible
    
    pos = 0 
    visited = [[False]*M for _ in range(N)]
    invisible = 0  
    
    for cctv in cctvs:
        x, y = cctv[0], cctv[1]
        type = board[x][y]
        dir = cctvDirs[pos]
        pos += 1 
        
        if type == 1:
            
            activate(x, y, dir, visited)
            
            
        elif type == 2:
            if dir == 0 or dir == 2:
                activate(x, y, 0, visited)
                activate(x, y, 2, visited)
            else:
                activate(x, y, 1, visited)
                activate(x, y, 3, visited)
            
        elif type == 3:
            if dir == 0:
                activate(x, y, 0, visited)
                activate(x, y, 1, visited)
            elif dir == 1:
                activate(x, y, 1, visited)
                activate(x, y, 2, visited)
            elif dir == 2:
                activate(x, y, 2, visited)
                activate(x, y, 3, visited)
            else:
                activate(x, y, 3, visited)
                activate(x, y, 0, visited)
    
        elif type == 4:
            if dir == 0:
                activate(x, y, 0, visited)
                activate(x, y, 1, visited)
                activate(x, y, 3, visited)
            elif dir == 1:
                activate(x, y, 0, visited)
                activate(x, y, 1, visited)
                activate(x, y, 2, visited)
            elif dir == 2:
                activate(x, y, 1, visited)
                activate(x, y, 2, visited)
                activate(x, y, 3, visited)
            else:
                activate(x, y, 3, visited)
                activate(x, y, 0, visited)
                activate(x, y, 2, visited)
        
        elif type == 5:
                activate(x, y, 0, visited)
                activate(x, y, 1, visited)
                activate(x, y, 2, visited)
                activate(x, y, 3, visited)
        
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and board[i][j] == 0:
                invisible += 1 
                
    ## print(invisible)
    minInvisible = min(minInvisible, invisible)
    
    
    
            
            
            
            
def dfs(cnt):
    
    if cctvCnt == cnt:
        ## print(cctvDirs)
        activateCCTV()
        return 
    
    
    
    for i in range(4):
        cctvDirs.append(i)
        dfs(cnt+1)
        cctvDirs.pop(len(cctvDirs)-1)
    
            
dfs(0)

print(minInvisible)



