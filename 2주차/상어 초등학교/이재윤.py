N = int(input())

friends = [[] for _ in range(N*N+1)]
order = [] 

board = [[0]*(N+1) for _ in range(N+1)]

for i in range(N*N):
    row = list(map(int, input().split()))
    order.append(row[0])
    friends[row[0]].append(row[1])
    friends[row[0]].append(row[2])
    friends[row[0]].append(row[3])
    friends[row[0]].append(row[4])
    


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

condition1 = []
condition2 = [] 

def condition1Check(num):
    
    condition1.clear()
    
    friend = friends[num]
    maxCnt = -int(1e9)
    
    check1 = [[0]*(N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 0:
                cnt = 0 
                
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                
                    if 1<=nx and nx<=N and 1<=ny and ny<=N:
                        if board[nx][ny] in friend:
                            cnt += 1
                            
                check1[i][j] = cnt                        
                maxCnt = max(maxCnt, cnt)    


    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 0 and check1[i][j] == maxCnt:
                condition1.append((i,j))
                
                
    if len(condition1) == 1:
        x = condition1[0][0]
        y = condition1[0][1]
        board[x][y] = num
        return True
    
    
    return False
                


def condition2Check(num):
    
    
    condition2.clear()
    
    maxCnt = -int(1e9)
    
    
    check2 = [[0]*(N+1) for _ in range(N+1)]
    
    
    for x, y in condition1:
        
        cnt = 0 
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 1<=nx and nx<=N and 1<=ny and ny<=N and board[nx][ny] == 0:
                cnt += 1 
        
        check2[x][y] = cnt 
        maxCnt = max(maxCnt, cnt)
    
    
    for x, y in condition1:
        if board[x][y] == 0 and check2[x][y] == maxCnt:
            condition2.append((x,y))
            
    
    if len(condition2) == 1:
        x = condition2[0][0]
        y = condition2[0][1]
        board[x][y] = num
        return True    
    
    return False
    
    
    
def condition3Check(num):
    
    x = condition2[0][0]
    y = condition2[0][1]
    
    board[x][y] = num
    


def satisfaction():
    
    point = 0 
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            
            num = board[i][j]
            cnt = 0 
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if 1<=nx and nx<=N and 1<=ny and ny<=N:
                    if board[nx][ny] in friends[num]:
                        cnt += 1 
            
            if cnt == 0:
                point += 0
            elif cnt == 1:
                point += 1
            elif cnt == 2:
                point += 10
            elif cnt == 3:
                point += 100
            elif cnt == 4:
                point += 1000
                
                
    print(point)
            
    



for i in range(0, len(order)): 
    
    num = order[i]
    
    res1 = condition1Check(num)
    
    if res1 == True:
        continue
    
    
    res2 = condition2Check(num)
    
    
    if res2 == True:
        continue
    
    res3 = condition3Check(num)
    
    
   
satisfaction()

   



