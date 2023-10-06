from collections import deque 

N, M, gas = map(int, input().split())

board = [] 

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
tx, ty = map(int, input().split())
tx -= 1 
ty -= 1 

taxi = [] 
arrived = [False]*M

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(M):
    row = list(map(int, input().split()))
    taxi.append([row[0]-1, row[1]-1, row[2]-1, row[3]-1])
    
    
    
target = len(taxi)

def getTaxiDistance(target): 
    
    visited = [[False]*N for _ in range(N)]
    
    q = deque()
    q.append((tx, ty, 0))
    
    distInfo = [] 
    
    
    while q:
        
        x, y, dist = q.popleft()
        
        for i in range(len(taxi)):
            if arrived[i] == False and x == taxi[i][0] and y == taxi[i][1]:
                distInfo.append([i, x, y, dist])
        
        if len(distInfo) == target:
            break 
                    
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny, dist+1))
                
    
    return distInfo 



def selectTaxi(distInfo):
    
    
    
    minDist = int(1e9)
    
    for i in range(len(distInfo)):
        if distInfo[i][3] < minDist:
            minDist = distInfo[i][3] 
            
            
    
    minDistTaxis = [] 
    
    for i in range(len(distInfo)):
        if distInfo[i][3] == minDist:
            minDistTaxis.append(distInfo[i])
            
    
    if len(minDistTaxis) == 1:
        return minDistTaxis[0]
        
        
    elif len(minDistTaxis) >= 2:
        minRowTaxis = [] 
        minRow = int(1e9)
        
        for i in range(len(minDistTaxis)):
            if minDistTaxis[i][1] < minRow:
                minRow = minDistTaxis[i][1] 
                
        
        for i in range(len(minDistTaxis)):
            if minRow == minDistTaxis[i][1]:
                minRowTaxis.append(minDistTaxis[i])
                
                
                
        if len(minRowTaxis) == 1:
            return minRowTaxis[0]
            
        
        elif len(minRowTaxis) >= 2:
            minColTaxi = [] 
            minCol = int(1e9)
            
            for i in range(len(minRowTaxis)):
                if minRowTaxis[i][2] < minCol:
                    minCol = minRowTaxis[i][2] 
                    
            
            for i in range(len(minRowTaxis)):
                if minCol == minRowTaxis[i][2]:
                    minColTaxi.append(minRowTaxis[i])
                    
                    
            
            return minColTaxi[0]
                    
            
            
        
    


def moveToDestination(sx, sy, ex, ey):


    visited = [[False]*N for _ in range(N)]
    
    q = deque()
    q.append((sx, sy, 0))
    visited[sx][sy] = True 
    
    
    while q:
        
        x, y, dist = q.popleft() 
        
        if x == ex and y == ey:
            return dist 
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny, dist+1))
    
    
    
    return -1
    



allArrival = True 
cnt = 0 

while True: 
    
    distInfo = getTaxiDistance(target) 
    if len(distInfo) == 0:
        allArrival = False
        break
    
    selectedTaxi = selectTaxi(distInfo)
    
    if gas < selectedTaxi[3]:
        allArrival = False 
        break
    
    gas -= selectedTaxi[3]
    tx = selectedTaxi[1]
    ty = selectedTaxi[2] 
    pos = selectedTaxi[0]
    
    
    dist = moveToDestination(tx, ty, taxi[pos][2], taxi[pos][3])
    
    
    if gas < dist or dist == -1:
        allArrival = False
        break
    
    gas -= dist 
    tx = taxi[pos][2]
    ty = taxi[pos][3] 
    gas += dist*2 
    arrived[pos] = True 
    
    
    cnt += 1 
    target -= 1 
    
    if cnt == len(taxi):
        break 
    
    
    
if allArrival == False:
    print(-1)
else:
    print(gas)







