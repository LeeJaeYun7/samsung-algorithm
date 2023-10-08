from collections import deque

T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def findAble(type):
    
    if type == 1:
        return [0, 1, 2, 3]
    elif type == 2:
        return [0, 2]
    elif type == 3:
        return [1, 3]
    elif type == 4:
        return [0, 1]
    elif type == 5:
        return [1, 2]
    elif type == 6:
        return [2, 3]
    
    
    return [0, 3]
    
    
    


def bfs(N, M, R, C, L, board, visited):
    
    cnt = 0 
    
    visited[R][C] = True
    cnt += 1 
    q = deque()
    q.append([R, C, 1])
    
    
    while q:
        
        x, y, time = q.popleft()
        
        if time == L:
            continue 
        
        
        type = board[x][y]
        
        able = findAble(type)
        
        for i in range(4):
            if i in able:
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx and nx<N and 0<=ny and ny<M and board[nx][ny] != 0 and visited[nx][ny] == False:
                    if i == 0 and (board[nx][ny] == 1 or board[nx][ny] == 2 or board[nx][ny] == 5 or board[nx][ny] == 6):
                        visited[nx][ny] = True
                        cnt += 1 
                        q.append([nx, ny, time+1])
                    elif i == 1 and (board[nx][ny] == 1 or board[nx][ny] == 3 or board[nx][ny] == 6 or board[nx][ny] == 7):
                        visited[nx][ny] = True
                        cnt += 1 
                        q.append([nx, ny, time+1])
                    elif i == 2 and (board[nx][ny] == 1 or board[nx][ny] == 2 or board[nx][ny] == 4 or board[nx][ny] == 7):
                        visited[nx][ny] = True
                        cnt += 1 
                        q.append([nx, ny, time+1])
                    elif i == 3 and (board[nx][ny] == 1 or board[nx][ny] == 3 or board[nx][ny] == 4 or board[nx][ny] == 5):
                        visited[nx][ny] = True
                        cnt += 1 
                        q.append([nx, ny, time+1])
    
        
        
        
    return cnt 
    

for i in range(T):
    
    N, M, R, C, L = map(int, input().split())
    
    visited = [[False]*M for _ in range(N)]
    
    board = [] 
    
    for j in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        

    ans = bfs(N, M, R, C, L, board, visited)

    print("#" + str(i+1) + " " + str(ans)) 
