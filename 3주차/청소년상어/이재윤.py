import copy 

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

fishes = [] 
eaten = [False]*20 

maxSum = 0

board = [] 

for i in range(4):
    row = list(map(int, input().split()))
    inputRow = [] 
    
    for j in range(4):
        inputRow.append([row[2*j], row[2*j+1]])
        
    board.append(inputRow)


for i in range(4):
    for j in range(4):
        fishes.append([i, j, board[i][j][0], board[i][j][1]])


fishes.sort(key=lambda x: (x[2]))

eatenFishes = [] 
eatenFishes.append(board[0][0][0])
sum = board[0][0][0]
sd = board[0][0][1]
eaten[board[0][0][0]] = True 
board[0][0][0] = -1


def updateFish(s, d, x, y):
    
    
    for i in range(len(fishes)):
        
        fx, fy, fs, fd = fishes[i][0], fishes[i][1], fishes[i][2], fishes[i][3] 
        
        if eaten[fs] == True:
            continue
        
        
        if s == fs:
            fishes[i][0] = x
            fishes[i][1] = y 
            fishes[i][3] = d
            break 
        
        
        
    
    
    
    
def updateFish2(s, d, x, y, s2, x2, y2):
    
    
     for i in range(len(fishes)):
        
        fx, fy, fs, fd = fishes[i][0], fishes[i][1], fishes[i][2], fishes[i][3] 
        
        if eaten[fs] == True:
            continue
        
        if s == fs:
            fishes[i][0] = x
            fishes[i][1] = y 
            fishes[i][3] = d
            
        if s2 == fs:
            fishes[i][0] = x2
            fishes[i][1] = y2 
            
        
        


def moveFish(x, y, s, d):
    
    
    cnt = 0 
    
    while True: 
        
        if cnt == 8:
            break 
        
        nx = x + dx[d-1]
        ny = y + dy[d-1]
        
        
        if 0<=nx and nx<4 and 0<=ny and ny < 4 and board[nx][ny][0] != -1:
            
            if board[nx][ny][0] == 0:
                
                board[nx][ny][0] = s
                board[nx][ny][1] = d
                board[x][y][0] = 0
                board[x][y][1] = 0 
                
                updateFish(s, d, nx, ny)
            
            else:
                ns = board[nx][ny][0]
                nd = board[nx][ny][1]
                
                board[x][y][0] = ns
                board[x][y][1] = nd
                board[nx][ny][0] = s
                board[nx][ny][1] = d 
            
                updateFish2(s, d, nx, ny, ns, x, y)
            
            break 
            
            
            
        else:
            d += 1 
            d %= 8
            cnt += 1 


    
    
    
    
    



def moveFishes(eatenFishes): 
    
    
    
    for i in range(len(fishes)):
        
        x, y, s, d = fishes[i][0], fishes[i][1], fishes[i][2], fishes[i][3] 
        
        if eaten[s] == True:
            continue
        
        
        
        moveFish(x, y, s, d)
        
        
      
        
        
    
    
    




    
    
    


def dfs(sx, sy, sd, sum, eatenFishes):
    
    global fishes
    global board
    global maxSum 
    
    maxSum = max(maxSum, sum)
    
    beforeBoard = copy.deepcopy(board)
    beforeFishes = copy.deepcopy(fishes) 
    moveFishes(eatenFishes)
    
    nextPos = []
    cnt = 1 
    
    while True:
        
        nx = sx + cnt*dx[sd-1]
        ny = sy + cnt*dy[sd-1]
        
        if 0<=nx and nx < 4 and 0<=ny and ny <4:
            nextPos.append([nx, ny])
            cnt += 1 
        else:
            break 
        
    
    if len(nextPos) == 0:
        fishes = copy.deepcopy(beforeFishes)
        board = copy.deepcopy(beforeBoard)
        return 
    
    for x, y in nextPos:
        
        s = board[x][y][0]
        d = board[x][y][1] 
        
        board[x][y][0] = -1
        board[x][y][1] = d 
        board[sx][sy][0] = 0
        board[sx][sy][1] = 0
        eaten[s] = True
        eatenFishes.append(s)
        dfs(x, y, d, sum+s, eatenFishes)
        eatenFishes.pop(len(eatenFishes)-1)
        eaten[s] = False
        board[sx][sy][0] = -1
        board[sx][sy][1] = sd
        board[x][y][0] = s
        board[x][y][1] = d 
        
    fishes = copy.deepcopy(beforeFishes) 
    board = copy.deepcopy(beforeBoard)





dfs(0, 0, sd, sum, eatenFishes)



print(maxSum)



