import copy 

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

maxSum = 0

board = [] 

for i in range(4):
    row = list(map(int, input().split()))
    inputRow = [] 
    
    for j in range(4):
        inputRow.append([row[2*j], row[2*j+1]-1])
        
    board.append(inputRow)



    
        


def findFish(board, num):
    
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == num:
                return (i, j)
                
        
    return None


    

    
    



def moveFish(board, sx, sy): 
    
    
    for num in range(1, 17):
        
        fish = findFish(board, num)
        
        if fish != None: 
                
            i, j = fish 
            dir = board[i][j][1] 
            
            for d in range(8):
                
                nx = i+dx[dir]
                ny = j+dy[dir]
                
                if 0<=nx and nx < 4 and 0<=ny and ny < 4 and (nx, ny) != (sx, sy):
                    
                    board[i][j][1] = dir
                    board[nx][ny], board[i][j] = board[i][j], board[nx][ny]
                    break
                
                dir = (dir+1)%8
                    
                    
        
      
def sharkMove(board, sx, sy):
    
    arr = [] 
    dir = board[sx][sy][1]
    
    for _ in range(4):
        
        sx = sx + dx[dir]
        sy = sy + dy[dir]
        
        if 0<=sx and sx<4 and 0<=sy and sy<4 and board[sx][sy][0] != -1:
            arr.append([sx, sy])
            
    
    return arr
        
    
    
    




    
    
    


def dfs(x, y, sum):
    
    global board
    global maxSum 
    
    beforeBoard = copy.deepcopy(board)
    
    sum += board[x][y][0]
    board[x][y][0] = -1 
    
    moveFish(board, x, y)
    
    arr = sharkMove(board, x, y)
    
    
    if len(arr) == 0:
        board = copy.deepcopy(beforeBoard)
        maxSum = max(maxSum, sum)
        return 
    
    for nx, ny in arr:
        dfs(nx, ny, sum)
        
    board = copy.deepcopy(beforeBoard)



dfs(0, 0, 0)



print(maxSum)



