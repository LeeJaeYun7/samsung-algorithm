N, M, K = map(int, input().split())


gunsBoard = [[[] for _ in range(N)] for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [] 
players = [] 

points = [0]*M

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            gunsBoard[i][j].append(board[i][j])
        
    
    
for i in range(M):
    x, y, d, s = map(int, input().split())
    players.append([x-1, y-1, d, s, 0])
    
    



def move(num, player):
    
    
    x = player[0]
    y = player[1]
    d = player[2] 
    
    
    nx = x + dx[d]
    ny = y + dy[d]
    
    
    if not (0<=nx and nx<N and 0<=ny and ny<N):
        nx -= dx[d]
        ny -= dy[d] 
        
        if d == 0:
            d = 2
        elif d == 1:
            d = 3
        elif d == 2:
            d = 0
        elif d == 3:
            d = 1
            
        
        nx += dx[d]
        ny += dy[d] 
        player[2] = d
        
        
    player[0] = nx
    player[1] = ny 
        
    
    opponent = -1
    
    for i in range(M):
        if num != i:
            
            player2 = players[i]
            
            x2 = player2[0]
            y2 = player2[1]
            
            if player[0] == player2[0] and player[1] == player2[1]:
                opponent = i
                break
            
            
    
    return opponent 
    
    
        
        
def getGun(player):
    
    
    x = player[0]
    y = player[1]
    g = player[4] 
    
    
    gunsInfo = gunsBoard[x][y]
    
    infoLen = len(gunsInfo)
    
    if infoLen > 0:
    
        if g == 0:
            player[4] = gunsInfo[infoLen-1]
            gunsInfo = gunsInfo[0:infoLen-1]
        else:
            if g < gunsInfo[infoLen-1]:
                player[4] = gunsInfo[infoLen-1]
                gunsInfo = gunsInfo[0:infoLen-1]
                gunsInfo.append(g)
            
            gunsInfo.sort() 
            
        
    gunsBoard[x][y] = gunsInfo
    
    
    
def checkPlayer(num, x, y):
    
    
    for i in range(len(players)):
        if i!= num:
            if x == players[i][0] and y == players[i][1]:
                return True
                
                
    return False 
        
    
    

def moveLosePlayer(num, player):
    
    
    x = player[0]
    y = player[1]
    d = player[2]
    g = player[4]
    
    
    if g != 0:
        gunsBoard[x][y].append(g)
        gunsBoard[x][y].sort()
        player[4] = 0 
        
        
    cnt = 0 
    
    while cnt != 4:
        
        
        nx = x + dx[d]
        ny = y + dy[d]
        
        if (0<=nx and nx<N and 0<=ny and ny<N) and checkPlayer(num, nx, ny) == False:
            player[0] = nx
            player[1] = ny
            player[2] = d
            
            gunsInfo = gunsBoard[nx][ny] 
            infoLen = len(gunsInfo)
            
            if infoLen > 0:
                player[4] = gunsInfo[infoLen-1]
                gunsInfo = gunsInfo[0:infoLen-1]
                gunsBoard[nx][ny] = gunsInfo
                
            break
                
            
        else:
            d += 1 
            d %= 4
            cnt += 1 
        
    
            
    
    
        
    
def fight(num, player, num2, player2):
    
    
    attackSum = player[3] + player[4]
    attackSum2 = player2[3] + player2[4]
    
    initAttack = player[3]
    initAttack2 = player2[3] 
     
    if (attackSum > attackSum2) or ((attackSum == attackSum2) and (initAttack > initAttack2)):
        points[num] += (attackSum-attackSum2)
        
        moveLosePlayer(num2, player2)
        
        getGun(player)
    else:
        points[num2] += (attackSum2-attackSum)
    
        moveLosePlayer(num, player)
        
        getGun(player2)
    
    
    
    
    
round = 1


while True:
    
    
    if round == K+1:
        break 
    
    
    for i in range(M):
          
        player = players[i]
        opponent = move(i, player)
        
        
        if opponent == -1:
            getGun(player)
        else:
            fight(i, player, opponent, players[opponent])
        
    
    round += 1 
    
    
for i in range(M):
    print(points[i], end=' ')
    
    
    
