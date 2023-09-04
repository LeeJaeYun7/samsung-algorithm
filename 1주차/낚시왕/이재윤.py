R, C, M = map(int, input().split())

shark = []
isCatched = [False]*(M+1)
shark.append((0, 0, 0, 0, 0))

for i in range(M):
    row = list(map(int, input().split()))
    shark.append(row)
    
    

board = [[0]*(C+1) for _ in range(R+1)]


for i in range(1, M+1):
    x, y = shark[i][0], shark[i][1]
    board[x][y] = i
    
    
    
ky = 1
total = 0


def catchShark(ky):
    
    global total
    
    for j in range(1, R+1):
        if board[j][ky] != 0:
            num = board[j][ky]
            isCatched[num] = True
            total += shark[num][4]
            board[j][ky] = 0 
            break


def moveShark():
    
    
    for i in range(1, M+1):
        if isCatched[i] == True:
            continue
        
        r = shark[i][0]
        c = shark[i][1]
        s = shark[i][2]
        d = shark[i][3]
        board[r][c] = 0 
        
        moveCnt = 0 
        target = 0 
        
        if d == 1 or d == 2:
            target = s % (2*(R-1))
        elif d == 3 or d == 4:
            target = s % (2*(C-1))
        
        while moveCnt != target:
            
            nr = 0
            nc = 0
            
            
            if d == 1:
                nr = r-1
                nc = c 
            elif d == 2:
                nr = r+1
                nc = c 
            elif d == 3:
                nr = r
                nc = c+1
            elif d == 4:
                nr = r 
                nc = c-1
                
            if 1<=nr and nr<=R and 1<=nc and nc<=C:
                r = nr
                c = nc
                moveCnt += 1 
                continue
            else:
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1 
                elif d == 3:
                    d = 4
                elif d == 4:
                    d = 3 
                    
                if d == 1:
                    nr = r-1
                    nc = c 
                elif d == 2:
                    nr = r+1
                    nc = c 
                elif d == 3:
                    nr = r
                    nc = c+1
                elif d == 4:
                    nr = r 
                    nc = c-1
                    
                r = nr
                c = nc
                moveCnt += 1 
                        
        shark[i][0] = r 
        shark[i][1] = c
        shark[i][3] = d
                    
                    
def eatShark():
    
    
    for i in range(1, M+1):
        if isCatched[i] == True:
            continue
        
        r = shark[i][0]
        c = shark[i][1] 
        z = shark[i][4] 
        
        if board[r][c] == 0:
            board[r][c] = i
        else:
            num = board[r][c] 
            
            if z < shark[num][4]:
                isCatched[i] = True
            else:
                board[r][c] = i
                isCatched[num] = True 
        
        
        
while ky != C+1:
    
    catchShark(ky)
    moveShark()
    eatShark()
    ky += 1 
    
    
print(total)




    
