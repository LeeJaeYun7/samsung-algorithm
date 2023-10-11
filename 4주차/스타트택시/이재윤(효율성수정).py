from collections import deque 

N, M, gas = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

board = [] 
people = [] 

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
tx, ty = map(int, input().split())
tx -= 1 
ty -= 1 

for i in range(M):
    a, b, c, d = map(int, input().split())
    people.append([a-1, b-1, c-1, d-1])
    
    
    


def getMinimumDistance():
    
    global tx, ty
    visited = [[False]*N for _ in range(N)]
    
    q = deque() 
    q.append([tx, ty, 0])
    visited[tx][ty] = True 
    distInfo = []
    
    
    while q:
        
        x, y, dist = q.popleft()
        
        for i in range(len(people)):
            if x == people[i][0] and y == people[i][1]:
                distInfo.append([i, x, y, dist])
                
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
    
            if 0<=nx and nx<N and 0<=ny and ny<N and visited[nx][ny] == False and board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append([nx, ny, dist+1])
            
            
    ## print(distInfo)            
    
    if len(distInfo) == 0:
        return None
    else:
        distInfo.sort(key=lambda x:[x[3], x[1], x[2]])
        ## print(distInfo) 
        return distInfo[0]
    
    
## N*N 시간 복잡도 
## = 400번 
def moveToDestination(sx, sy, ex, ey):
    
    visited = [[False]*N for _ in range(N)]
    
    q = deque()
    q.append([sx, sy, 0])
    visited[sx][sy] = True
    
    
    while q:
        
        x, y, dist = q.popleft()
        
        if x == ex and y == ey:
            return dist
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
    
            if 0<=nx and nx<N and 0<=ny and ny<N and visited[nx][ny] == False and board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append([nx, ny, dist+1])
    
    
    return -1 
    
    

allArrived = True    
cnt = 0     


## 최대 M번
## = 400번*(160000+400) 
## = 6400만 
while True:
    
    
    minDistInfo = getMinimumDistance()

    if minDistInfo == None: 
        allArrived = False         
        break
    
    
    dist = minDistInfo[3]
    
    if gas < dist:
        allArrived = False
        break 
    
    num = minDistInfo[0]
    tx = minDistInfo[1]
    ty = minDistInfo[2]
    gas -= dist
    
    ex = people[num][2]
    ey = people[num][3]
    
    ## print(tx, ty, gas)
    
    
    arriveDist = moveToDestination(tx, ty, ex, ey)
    
    if arriveDist == -1 or gas < arriveDist:
        allArrived = False
        break 
    
    
    tx = ex
    ty = ey 
    
    gas -= arriveDist 
    gas += 2*arriveDist
    people.pop(num)
    
    cnt += 1 
    
    if cnt == M:
        break 
    
    

if allArrived == False:
    print(-1)
else:
    print(gas)
    







    
    
    
    
    
    
