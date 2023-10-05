import copy 


N, K = map(int, input().split())

A = [[0]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


C = list(map(int, input().split()))

for i in range(len(C)):
    A[0][i] = C[i]



def printMap():
    
    for i in range(N):
        for j in range(N):
            print(A[i][j], end=' ')
        print('', end='\n')
    print('', end='\n')



def doFirst():
    
    minFish = int(1e9)
    
    for i in range(N):
        if A[0][i] <= minFish:
            minFish = A[0][i]
            
    
    for i in range(N):
        if A[0][i] == minFish:
            A[0][i] += 1 

    

def doSecond():
        
        
    curr = 0 
    height = 0 
        
    while True:
        
        if curr == 0:
            A[0][curr], A[1][curr+1] = A[1][curr+1], A[0][curr]
            
            height += 1 
            curr += 1
            
        else:
            
            
            if curr+height+1 >= N:
                break
            
            r = 1
            c = height + 1 
            
            ## print("curr, height는?")
            ## print(curr, height)
            ## print("r, c는?")
            ## print(r, c)
            ## print("", end='\n')
            
            dist = 0 
            finalDist = 0 
            
            for i in range(height, -1, -1):
                
                initR = 1
                initC = c 
                targetC = curr+c
                
                ## print("initR, initC, targetC는?")
                ## print(initR, initC, targetC)
                
                for j in range(curr, -1, -1):
                    
                    
                    if A[i][j] != 0:
                        dist += 1 
                        A[i][j], A[initR][targetC] = A[initR][targetC], A[i][j]
                        initR += 1 
                    
                    else:
                        if finalDist == 0:
                            finalDist = dist
                        
                r += 1
                c -= 1 
                
            curr += (height+1)
            height = finalDist
            

    
    
    

def doThird():
    
    global A 
    
    tmpA = copy.deepcopy(A)
    
    
    for i in range(N):
        for j in range(N):
            
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                
                if 0<=ni and ni < N and 0<=nj and nj < N and A[i][j] != 0 and A[ni][nj] != 0 and A[i][j] < A[ni][nj]:
                    gap = A[ni][nj]-A[i][j]
                    d = gap // 5 
                    tmpA[i][j] += d
                    tmpA[ni][nj] -= d 
            
            
    
    A = copy.deepcopy(tmpA)




def doFourth(): 
    
    global A 
    
    C = []
    
    for j in range(N):
        for i in range(N):
          if A[i][j] != 0:
              C.append(A[i][j])
              
            
    
    tmpA = [[0]*N for _ in range(N)]
    
    for i in range(len(C)):
        tmpA[0][i] = C[i]
        
        
    A = copy.deepcopy(tmpA)
    
    
    
def doFifth(): 
    
    global A 
    
    c = 1 
    
    for i in range(0, 1):
        for j in range(N//2-1, -1, -1):
          A[i][j], A[i+1][j+c] = A[i+1][j+c], A[i][j]
          c += 2
          
    
    colStart = N // 2 + N // 4 -1 
    colEnd = N // 2 -1
    
    r = 1
    c = 1 
    
    for i in range(1, -1, -1):
        c = 1 
        
        for j in range(colStart, colEnd, -1):
            A[i][j], A[i+r][j+c] = A[i+r][j+c], A[i][j]
            c += 2
    
        r += 2
    

def doSix():
    
    maxFish = -int(1e9)
    minFish = int(1e9)
    
    for j in range(0, N):
        if A[0][j] > maxFish:
            maxFish = A[0][j]
        
        if A[0][j] < minFish:
            minFish = A[0][j]
            
        
    
    return maxFish-minFish 
    
    

cnt = 0     


while True: 
    
    cnt += 1 
    
    doFirst() 
    
    ## printMap()
    
    doSecond()
    
    ## printMap()
    
    doThird() 
    
    ## printMap()

    doFourth()
    
    ## printMap()
    
    doFifth() 
    
    ## printMap()
    
    doThird()
    
    ## printMap()
    
    doFourth()
    
    ## printMap()
    
   
    gap = doSix() 
        
    if gap <= K:
        break 
    
    
    
print(cnt) 
