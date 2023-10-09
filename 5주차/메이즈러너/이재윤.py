import copy 

N, M, K = map(int, input().split())

board = [] 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
    
people = []
totalMove = 0 

exit = [False]*M 

for i in range(M):
    a, b = map(int, input().split())
    people.append([a-1, b-1])


ox, oy = map(int, input().split()) 
ox -= 1
oy -= 1 

def movePeople():
    
    
    global totalMove 
    
     
    
    for i in range(len(people)):
        if exit[i] == True:
            continue
        
        move = 0
        
        x = people[i][0]
        y = people[i][1] 
        
        currDist = abs(x-ox)+abs(y-oy)
        
        nextMove = False
        
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            
            if 0<=nx and nx < N and 0<=ny and ny<N and board[nx][ny] == 0:
                
                nextDist = abs(nx-ox)+abs(ny-oy)
                
                if nx == ox and ny == oy:
                    exit[i] = True
                    move = 1 
                    break
                
                if nextMove == False and currDist > nextDist:
                    people[i][0] = nx
                    people[i][1] = ny
                    move = 1 
                    nextMove = True

        
        totalMove += move 
        


def findSmallestSquare():
    

    
    
    
    for k in range(1, N+1):
        for i in range(0, N-k+1):
            for j in range(0, N-k+1):
                
                sx = i
                sy = j
                ex = i+k-1
                ey = j+k-1
                
                
                if sx<= ox and ox <=ex and sy<= oy and oy <= ey:
                    for l in range(len(people)):
                        if exit[l] == True:
                            continue
                        
                        x = people[l][0]
                        y = people[l][1] 
                    
                        if sx<= x and x <= ex and sy <= y and y <= ey:
                            return [sx, sy, ex, ey]
             
    
    
def rotate(square):
    
    
    ## print("square는?")
    ## print(square)
    
    
    tmpBoard = copy.deepcopy(board)
    
    sx = square[0]
    sy = square[1]
    ex = square[2]
    ey = square[3] 
    
    squareLen = ex-sx+1 
    col = ey 
    
    
    
    for i in range(sx, ex+1):
        
        row = board[i][sy:ey+1]
        pos = 0 
        
        for j in range(sx, ex+1):
            tmpBoard[j][col] = row[pos]
            pos += 1 
            
        col -= 1 
            
            
    
    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            board[i][j] = tmpBoard[i][j] 
            
            
  
    
    

def rotatePeopleAndOut(square):
    
    
    global ox
    global oy
    
    global people 
    
    tmpBoard = copy.deepcopy(board)
    initBoard = copy.deepcopy(board)
    
    sx = square[0]
    sy = square[1]
    ex = square[2]
    ey = square[3]
    
    
    
    for i in range(len(people)):
        if exit[i] == True:
            continue
        
        x = people[i][0]
        y = people[i][1] 
    
        if sx<= x and x <= ex and sy <= y and y<=ey:
            num = 100*(x+1)+y+1
            initBoard[x][y] = num

    oNum = 100*(ox+1)+oy+1
    initBoard[ox][oy] = oNum
    
    squareLen = ex-sx+1 
   
    col = ey 
    
    for i in range(sx, ex+1):
        
        row = initBoard[i][sy:ey+1]
        
        pos = 0 
        
        for j in range(sx, ex+1):
            tmpBoard[j][col] = row[pos]
            pos += 1 
            
        col -= 1 
   
   


    ## 10*10*10 = 최대 1000번   
    
    for i in range(len(people)):
        if exit[i] == True:
            continue 
        
        x = people[i][0]
        y = people[i][1]
        
        if sx<=x and x <= ex and sy<=y and y <= ey:
            num = 100*(x+1)+y+1 
            
            for j in range(0, N):
                for k in range(0, N):
                    if tmpBoard[j][k] == num:
                        people[i][0] = j
                        people[i][1] = k
    
    
    ## 10*10 = 최대 100번 
    for i in range(0, N):
        for j in range(0, N):
            if tmpBoard[i][j] == oNum:
                ox = i
                oy = j 
                
            
            
            
def breakWall(square):
    
    sx = square[0]
    sy = square[1]
    ex = square[2]
    ey = square[3]
    
    
    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            if board[i][j] > 0:
                board[i][j] -= 1 
    
    
            
    
time = 0 
    
while True:     
    
    time +=1 
    
    movePeople()     
    
    cnt = 0 
    
    for i in range(len(people)):
        if exit[i] == True:
            cnt += 1 
    
    if cnt == len(people):
        break 
    
                
    square = findSmallestSquare()
    
    rotate(square)
    
    rotatePeopleAndOut(square)
    
    
    breakWall(square) 
  
         
    if time == K:
        break
    
    
    
print(totalMove)
print(ox+1, oy+1)
    
    
    
