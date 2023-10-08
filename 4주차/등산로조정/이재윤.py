import copy 

T = int(input())
maxLen = 0 
totalMaxLen = 0 

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

def dfs(x, y, N, K, board, len, visited, pave, path):
    
    global maxLen
    
    maxLen = max(maxLen, len)
    
    curr = board[x][y]
    
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx and nx<N and 0<=ny and ny<N and visited[nx][ny] == False:
            
            if curr > board[nx][ny]:
                visited[nx][ny] = True
                path.append([nx, ny, board[nx][ny]])
                dfs(nx, ny, N, K, board, len+1, visited, pave, path)
                path.pop()
                visited[nx][ny] = False
                
            elif curr <= board[nx][ny] and pave == False:
                target = curr-1
                gap = board[nx][ny]-target
                origin = board[nx][ny]
                if K>=gap:
                    for j in range(K, gap-1, -1):
                        board[nx][ny] -= j
                        visited[nx][ny] = True
                        path.append([nx, ny, board[nx][ny]])
                        dfs(nx, ny, N, K, board, len+1, visited, True, path)
                        path.pop()
                        board[nx][ny] = origin 
                        visited[nx][ny] = False 
                    
                    
                
                
                
                
            
    
    


for i in range(T):
    
    totalMaxLen = 0 
    N, K = map(int, input().split())
    
    board = [] 
    
    for j in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        
        
    arr = [] 
    maxHeight = 0 
    
    for j in range(N):
        for k in range(N):
            if board[j][k] > maxHeight: 
                maxHeight = board[j][k] 
                
    
    for j in range(N):
        for k in range(N):
            if board[j][k] == maxHeight:
                arr.append((j, k))
    
    
    for x,y in arr:
        
        tmpBoard = copy.deepcopy(board)
        maxLen = 0 
        visited = [[False]*N for _ in range(N)]
        
        visited[x][y] = True 
        pave = False
        path = []
        path.append([x,y, tmpBoard[x][y]])
        dfs(x, y, N, K, tmpBoard, 1, visited, pave, path)
        totalMaxLen = max(totalMaxLen, maxLen)
    
    print("#" + str(i)+" " + str(totalMaxLen))
