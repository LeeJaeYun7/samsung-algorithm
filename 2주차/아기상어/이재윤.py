from collections import deque

N = int(input())

babyShark = [] 

board = []
fishes = [] 


totalTime = 0 
babySharkEat = 0 

dx = [-1, 1, 0, 0]
dy = [0,0, -1, 1]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            babyShark.append([2, i, j])
            
        if 1<=board[i][j] and board[i][j]<=6:
            fishes.append([board[i][j], i, j])
            
eaten = [False]*len(fishes)
fishes.sort(key=lambda x:(x[0]))


babySharkMove = 0 

time = 0 

def moveBabyShark(babySharkSize, x, y, tx, ty):
    
    
    global babySharkMove
    
    visited = [[False]*N for _ in range(N)]
    q = deque()
    q.append((x,y,0))
    visited[x][y] = True
    
    
    while q:
        x, y, dist = q.popleft()
        
        if x == tx and y == ty:
            babySharkMove = dist
            return True
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<N and 0<=ny and ny<N:
                if visited[nx][ny] == False and babySharkSize >= board[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist+1))

    
    return False
    
  
    


def dfs():
    
    global totalTime
    global babySharkEat
    global babySharkMove
    
    able = [] 
    
    for i in range(len(fishes)):
        if eaten[i] == True:
            continue
        
        size = fishes[i][0]
        
        if babyShark[0][0] > size:
            able.append([i, fishes[i][0], fishes[i][1], fishes[i][2]])
            
            
            
    
    if len(able) == 1:
        
        babySharkMove = 0 
        reachable = moveBabyShark(babyShark[0][0], babyShark[0][1], babyShark[0][2], able[0][2], able[0][3])
        
        
        if reachable == True:
            board[babyShark[0][1]][babyShark[0][2]] = 0 
            babyShark[0][1] = able[0][2]
            babyShark[0][2] = able[0][3]
            babySharkEat += 1 
            
            if babyShark[0][0] == babySharkEat:
                babyShark[0][0] += 1 
                babySharkEat = 0 
        
            totalTime += babySharkMove
            eaten[able[0][0]] = True 
            board[able[0][2]][able[0][3]] = 9 
        
            dfs()
        else:
            return 
        
    elif len(able) >= 2:
        
        distInfo = []
        minMove = int(1e9)
        selectedAble = [] 
        
        for i in range(len(able)):
            
            babySharkMove = 0 
            reachable = moveBabyShark(babyShark[0][0], babyShark[0][1], babyShark[0][2], able[i][2], able[i][3])
            if reachable == True:
                minMove = min(minMove, babySharkMove)
                distInfo.append(babySharkMove)
            else:
                distInfo.append(-1)
                    
        if minMove == int(1e9):
            return 
        
        for i in range(len(able)):
            if distInfo[i] == minMove:
                selectedAble.append(able[i])
                
        selectedAble.sort(key = lambda x:(x[2], x[3]))
        
        babySharkMove = 0
        moveBabyShark(babyShark[0][0], babyShark[0][1], babyShark[0][2], selectedAble[0][2], selectedAble[0][3])
        
        
        board[babyShark[0][1]][babyShark[0][2]] = 0 
        babyShark[0][1] = selectedAble[0][2]
        babyShark[0][2] = selectedAble[0][3]
        babySharkEat += 1 
            
        if babyShark[0][0] == babySharkEat:
            babyShark[0][0] += 1 
            babySharkEat = 0 
        
        totalTime += babySharkMove
        eaten[selectedAble[0][0]] = True 
        board[selectedAble[0][2]][selectedAble[0][3]] = 9 
        
        dfs() 
        
        
  
dfs()


print(totalTime)

