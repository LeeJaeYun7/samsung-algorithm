from collections import deque 
import copy 

N, M, K = map(int, input().split())


board = [] 

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0] 

dx2 = [0, -1, -1, -1, 0, 1, 1, 1]
dy2 = [1, 1, 0, -1, -1, -1, 0, 1]


def isInside(x, y):
    if 0<=x and x<N and 0<=y and y<M:
        return True
    else:
        return False


for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
towers = [] 

for i in range(N):
    for j in range(M):
        if board[i][j] >= 1:
            towers.append([i, j, board[i][j], 0])
            

def printBoard():
    
    for i in range(N):
        for j in range(M):
            print(board[i][j], end=' ')
        print('', end='\n')
    print('', end='\n')
            
        
def chooseAttacker(time):
    
    towers.sort(key=lambda x:[x[2], -x[3], -(x[0]+x[1]), -x[1]])
    
    attackTower = towers[0]
    
    x = attackTower[0]
    y = attackTower[1]
    
    board[x][y] += (M+N)
    towers[0][2] += (M+N)
    towers[0][3] = time 
    
    ## print("Attacker 선정")    
    ## printBoard()
    ## print(towers)
    
            
    return x,y, towers[0][2] 
    
    
    

def chooseAttacked(time):
    
    
    towers.sort(key=lambda x:[-x[2], x[3], x[0]+x[1], x[1]])
    
    attackedTower = [] 
    
    for i in range(len(towers)):
        if towers[i][3] == time:
            continue
        else:
            attackedTower = towers[i]
            break
        
    
    ## print(attackedTower)
    return attackedTower[0], attackedTower[1]
            


def razorAttack(sx, sy, ex, ey):
    
    visited = [[False]*M for _ in range(N)]
    
    path = [] 
    q = deque()
    q.append([sx, sy, path])
    visited[sx][sy] = True 
    
    
    while q:
        
        x, y, currPath = q.popleft()
        
        if x == ex and y == ey:
            return currPath 
            
        
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            
            if isInside(nx, ny):
                if visited[nx][ny] == False and board[nx][ny] >= 1:
                    visited[nx][ny] = True
                    nextPath = copy.deepcopy(currPath)
                    nextPath.append([nx, ny])
                    q.append([nx, ny, nextPath])
            else:
                if nx == -1:
                    nx += N
                elif nx == N:
                    nx -= N
                    
                if ny == -1:
                    ny += M
                elif ny == M:
                    ny -= M 
                    
                
                if visited[nx][ny] == False and board[nx][ny] >= 1:
                    visited[nx][ny] = True
                    nextPath = copy.deepcopy(currPath)
                    nextPath.append([nx, ny])
                    q.append([nx, ny, nextPath])            
        
        
    return None 
    
    
    
    
    
def bombAttack(attackerX, attackerY, sx, sy, attack):
    
    
    bombedTowers = [] 
    bombedTowers.append([sx, sy])
    
    board[sx][sy] -= attack
    
    for i in range(len(towers)):
        if towers[i][0] == sx and towers[i][1] == sy:
            towers[i][2] -= attack
            break
    
    
    ## print("bombAttack의 attackerX, attackerY")
    ## print(attackerX, attackerY)
        
    
    for i in range(8):
        nx = sx + dx2[i]
        ny = sy + dy2[i]
        
        if nx == attackerX and ny == attackerY:
            continue 
        
        if isInside(nx, ny):
            if board[nx][ny] >= 1:
                board[nx][ny] -= (attack // 2)
                bombedTowers.append([nx, ny])
                
                for j in range(len(towers)):
                    if towers[j][0] == nx and towers[j][1] == ny:
                        towers[j][2] -= (attack // 2)
            
            
        else:
            if nx == -1:
                nx += N
            elif nx == N:
                nx -= N
                    
            if ny == -1:
                ny += M
            elif ny == M:
                ny -= M
                
                
            if nx == attackerX and ny == attackerY:
                continue 
            
            
            if board[nx][ny] >= 1:
                board[nx][ny] -= (attack // 2)
                bombedTowers.append([nx, ny])
                
                for j in range(len(towers)):
                    if towers[j][0] == nx and towers[j][1] == ny:
                        towers[j][2] -= (attack // 2)
    
    ## print("bombedTowers는?")
    ## print(bombedTowers)
            
    
    return bombedTowers        
    
    
    


def razorDecrease(path, attack):
    
    
    pathLen = len(path)
    
    
    for i in range(pathLen):
        
        x = path[i][0]
        y = path[i][1] 
        
        
        if i == pathLen-1:
            board[x][y] -= attack
            
            for j in range(len(towers)):
                if towers[j][0] == x and towers[j][1] == y:
                    towers[j][2] -= attack
                    break
        else:
            
            board[x][y] -= (attack//2)
            
            for j in range(len(towers)):
                if towers[j][0] == x and towers[j][1] == y:
                    towers[j][2] -= (attack // 2)
                    break
    



def breakTower():
    
    for i in range(N):
        for j in range(M):
            if board[i][j] <= 0:
                board[i][j] = 0 
                
                
    for i in range(len(towers)-1, -1, -1):
        if towers[i][2] <= 0:
            towers.pop(i)



def repairTower(attackerX, attackerY, attackedTowers):
    
    ## print("attackedTowers는?")
    ## print(attackedTowers)
    
    
    for i in range(N):
        for j in range(M):
            if i == attackerX and j == attackerY:
                continue 
            
            if board[i][j] >= 1 and [i, j] not in attackedTowers:
                board[i][j] += 1
                
                for k in range(len(towers)):
                    if towers[k][0] == i and towers[k][1] == j:
                        towers[k][2] += 1 
                        break 
    


def getStrongestTower():
    
    maxTower = 0
    
    for i in range(N):
        for j in range(M):
            maxTower = max(maxTower, board[i][j])



    return maxTower     
    


def getTowersCnt():
    
    cnt = 0 
    
    for i in range(N):
        for j in range(M):
            if board[i][j] >= 1:
                cnt += 1 
                
                
    return cnt 



time = 1 


while True:
    
    
    ## 700번
    attackerX, attackerY, attack = chooseAttacker(time) 

    ## 800번 
    attackedX, attackedY = chooseAttacked(time)
    
    ## print(attackerX, attackerY, attack, attackedX, attackedY)
    
    
    razorPath = razorAttack(attackerX, attackerY, attackedX, attackedY)
    
    if razorPath != None:
        ## print(razorPath)
        razorDecrease(razorPath, attack)
        breakTower()
        
        ## print("Repair 이전")
        ## printBoard() 
        
        repairTower(attackerX, attackerY, razorPath)
        
    else:
        bombedTowers = bombAttack(attackerX, attackerY, attackedX, attackedY, attack)
        breakTower() 
        repairTower(attackerX, attackerY, bombedTowers)
    
    
    ## print(str(time) + "결과!")
    ## printBoard() 
    ## print(towers)
    
    cnt = getTowersCnt()
    
    
    time += 1 
    
    if cnt == 1 or time == K+1:
        break 


ans = getStrongestTower() 
print(ans)
