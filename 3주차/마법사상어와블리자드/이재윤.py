import copy 

N, M = map(int, input().split())

board = [] 

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)

arr = [] 
arr.append(-1)
magics = []

point = 0 

for i in range(M):
    d, s = map(int, input().split())
    magics.append([d, s])


sx = N // 2 
sy = N // 2 

time = 0

for i in range(2*N-1):
    
    d = i % 4
    
    if d == 0 or d == 2:
        time += 1 
    
    reachEnd = False    
    
    for j in range(time):
        nx = sx + dx[d]
        ny = sy + dy[d]
        
        if ny < 0 or board[nx][ny] == 0:
            reachEnd = True
            break
        
        arr.append(board[nx][ny])
        sx = nx
        sy = ny 
        
    
    if reachEnd == True:
        break 
        
        
        
def explodeMarbles():
    
    global point 
    
    
    while True:
        
        explodeCnt = 0 
    
        arrLen = len(arr)
        curr = arr[arrLen-1]
        cnt = 1
    
    
        for i in range(arrLen-2, -1, -1):
        
            if curr == arr[i]:
                cnt += 1 
            else:
                if cnt >= 4:
                    explodeCnt += 1 
                    point += cnt*curr 
                    for j in range(i+cnt, i, -1):
                        arr.pop(j)
                    
                curr = arr[i]
                cnt = 1 
            
    
    
        
        if explodeCnt == 0:
            break 
        
    
    
    
    
    
def updateMarbles(): 
    
    global arr 
    
    print(len(arr))
    
    if len(arr) == 1:
        return 
    
    newArr = [] 
    newArr.append(-1)
    
    curr = arr[1]
    cnt = 1 
    
    for i in range(2, len(arr)):
        
        if curr == arr[i]:
            cnt += 1 
        else:
            
            newArr.append(cnt)
            newArr.append(curr)
            
            curr = arr[i]
            cnt = 1 
            
            
    newArr.append(cnt)
    newArr.append(curr)
    if len(newArr) > N*N:
        newArr = newArr[0:N*N]
    
    
    arr = copy.deepcopy(newArr)
        
    
    
    
    
    
    
    



def breakMarbles(dIdx):
    
    dLen = len(dIdx)
    
    for i in range(dLen-1, -1, -1):
        if dIdx[i] <= len(arr)-1:
            arr.pop(dIdx[i])
        
        




for d, s in magics:
    
    curr = 0
    gap = 0 
    
    dIdx = [] 
    
    if d == 1:
        curr = 7
        gap = 7 
    elif d == 2:
        curr = 3
        gap = 3
    elif d == 3:
        curr = 1
        gap = 1 
    elif d == 4:
        curr = 5
        gap = 5 
        
    
    dIdx.append(curr)
    
    for i in range(s-1):
        gap += 8
        curr += gap
        dIdx.append(curr)
        
        
    breakMarbles(dIdx)
    
    explodeMarbles()


    updateMarbles() 



print(point)









