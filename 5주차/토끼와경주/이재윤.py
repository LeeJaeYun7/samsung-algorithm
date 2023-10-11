Q = int(input())

N = 0
M = 0 

rabbitInfo = [] 

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


ans = 0 


def moveRabbit(r, c, d):
    
    
    
    
    moveInfo = [] 
    
    
    for i in range(4):
        
        cd = d 
        
        if i == 0 or i == 2:
            cd %= 2*(N-1)
        elif i == 1 or i == 3:
            cd %= 2*(M-1)
        
        
        sr = r
        sc = c
        dir = i 
        
    
      
        while True:
            
            
            if dir == 0 and sr == 1:
                dir = 2 
                continue
            elif dir == 1 and sc == M:
                dir = 3
                continue
            elif dir == 2 and sr == N:
                dir = 0
                continue
            elif dir == 3 and sc == 1:
                dir = 1
                continue
            
            nextMove = 0 
            
            if dir == 0:
                nextMove += (sr-1)
                
                if nextMove < cd: 
                    sr = 1
                    cd -= nextMove
                    dir = 2 
                else:
                    sr -= cd 
                    break 
        
            elif dir == 1:
                nextMove += (M-sc)
                
                if nextMove < cd:
                    sc = M
                    cd -= nextMove
                    dir = 3
                else:
                    sc += cd
                    break 
                    
            elif dir == 2:
                
                nextMove += (N-sr)
                
                
                if nextMove < cd:
                    sr = N
                    cd -= nextMove
                    dir = 0
                else:
                    sr += cd
                    break 
                
            elif dir == 3:
                
                nextMove += (sc-1)
                
                if nextMove < cd:
                    
                    sc = 1 
                    cd -= nextMove
                    dir = 1 
                
                else:
                    
                    sc -= cd
                    break 
                    
        
        
        moveInfo.append([sr, sc])
    
    
    
    moveInfo.sort(key=lambda x:[-(x[0]+x[1]), -x[0], -x[1]])
    
    
    return moveInfo[0]
    



## 4000번

for i in range(Q):
    
    command = list(map(int, input().split()))
    
    if command[0] == 100:
        
        N = command[1]
        M = command[2]
        P = command[3] 
        
        for j in range(P):
            rabbit = [command[2*j+4], command[2*j+5], 1, 1, 0, 0]
            rabbitInfo.append(rabbit)
        
        
    elif command[0] == 200:
        
        K = command[1]
        S = command[2] 
        
        
        ## 최대 100번 
        for j in range(K):
            
            rabbitInfo.sort(key=lambda x:[x[4], x[2]+x[3], x[2], x[3], x[0]])
            
            selectedRabbit = rabbitInfo[0]
            r = selectedRabbit[2]
            c = selectedRabbit[3]
            d = selectedRabbit[1]
            
            
            ## 최대 80만 
            fr, fc = moveRabbit(r, c, d)
            rabbitInfo[0][2] = fr
            rabbitInfo[0][3] = fc
            rabbitInfo[0][4] += 1 
            
            point = fr+fc
            
            for k in range(1, P):
                rabbitInfo[k][5] += point 
                
            
            
        
        rabbitInfo.sort(key=lambda x:[-(x[2]+x[3]), -x[2], -x[3], -x[0]])
        rabbitInfo[0][5] += S
        
    
    elif command[0] == 300:
    
        pid = command[1]
        L = command[2] 
        
        for i in range(len(rabbitInfo)):
            if rabbitInfo[i][0] == pid:
                rabbitInfo[i][1] *= L
                rabbitInfo[i][1] %= 1000000000
                
    
    
    elif command[0] == 400:
        
        for i in range(len(rabbitInfo)):
            ans = max(ans, rabbitInfo[i][5])
            
            
            
print(ans)
