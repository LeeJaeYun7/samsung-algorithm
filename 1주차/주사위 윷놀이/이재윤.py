

arr = [0,0,0,0]

dices = list(map(int, input().split()))
points = 0 
maxPoints = 0 

dir1 = 0
dir2 = 0 
tmpCnt = 0

def move(cnt, startCnt, arrPos, num, beforeNum):
    
    global dir 
    global points
    global tmpCnt
    
    if cnt == 0 or num == 100:
        arr[arrPos] = num 
        
        if num != 100:
            points += arr[arrPos]
            
        if num == 100:
            tmpCnt = startCnt - cnt 
        
        return 
    
    nextNum = 0 
    
    if num == 0 or num == 2 or num == 4 or num == 6 or num == 8:
        nextNum = num + 2 
    elif num == 10 and cnt == startCnt:
        nextNum = num + 3 
    elif num == 10 and cnt != startCnt:
        nextNum = num + 2 
    elif num == 12 or num == 14 or num == 16 or num == 18:
        nextNum = num + 2 
    elif num == 13 or num == 16:
        nextNum = num + 3
    elif num == 19:
        nextNum = num + 6 
    elif num == 20 or num == 22:
        nextNum = num + 2 
    elif num == 24 and cnt == (startCnt - 2):
        nextNum = num + 1
    elif num == 24 and cnt != (startCnt - 2):
        nextNum = num + 2
    elif num == 26 and cnt == (startCnt - 3):
        nextNum = num - 1
    elif num == 26 and cnt != (startCnt - 3):
        nextNum = num + 2
    elif num == 28 and cnt == (startCnt - 1):
        nextNum = num - 1
    elif num == 28 and cnt != (startCnt - 1):
        nextNum = num + 2
    elif num == 30 and cnt == startCnt and beforeNum != 25:
        nextNum = num - 2 
    elif num == 30 and cnt != startCnt and beforeNum != 25:
        nextNum = num + 2
    elif num == 27:
        nextNum = num - 1
    elif num == 25 and beforeNum == 19:
        nextNum = num + 5 
        dir1 = 0 
    elif num == 25 and beforeNum == 24:
        nextNum = num + 5 
        dir1 = 1 
    elif num == 25 and beforeNum == 26:
        nextNum = num + 5 
        dir1 = 2 
    elif num == 30 and beforeNum == 25:
        nextNum = num + 5 
    elif num == 35:
        nextNum = num + 5 
    elif num == 40 and beforeNum == 35:
        nextNum = 100
        dir2 = 0
    elif num == 40 and beforeNum == 38:
        nextNum = 100
        dir2 = 1 
    elif num == 32 or num == 34 or num == 36 or num == 38:
        nextNum == num + 2 
    
    
    move(cnt-1, startCnt, arrPos, nextNum, num)
    
    
    
    
    
    
def unmove(cnt, startCnt, arrPos, num, beforeNum):
    
    global dir 
    if cnt == 0:
        arr[arrPos] = num
        return 
    
    nextNum = 0 
    
    if num == 2 or num == 4 or num == 6 or num == 8 or num == 10 or num == 12 or num == 14:
        nextNum = num - 2 
    elif num == 13:
        nextNum = num - 3
    elif num == 16 and startCnt == 2:
        nextNum = num - 3 
    elif num == 16 and startCnt == 3:
        nextNum = num - 2 
    elif num == 18 or num == 20 or num == 22 or num == 24:
        nextNum = num - 2
    elif num == 26 and beforeNum == 25:
        nextNum = num + 1
    elif num == 26 and beforeNum == 28:
        nextNum = num - 2
    elif num == 27:
        nextNum = num + 1
    elif num == 28 and beforeNum == 27:
        nextNum = num + 2
    elif num == 28 and beforeNum == 30:
        nextNum = num - 2 
    elif num == 30 and beforeNum == 35:
        nextNum = num - 5
    elif num == 30 and beforeNum == 32:
        nextNum = num - 2 
    elif num == 25 and dir1 == 0:
        nextNum = num - 6
    elif num == 25 and dir1 == 1:
        nextNum = num - 1
    elif num == 25 and dir1 == 2:
        nextNum = num + 1 
    elif num == 32 and num == 34 and num == 36 and num == 38:
        nextNum = num - 2 
    elif num == 40 and dir2 == 0:
        nextNum = num - 5
    elif num == 40 and dir2 == 1:
        nextNum = num - 2 
    elif num == 100:
        nextNum = 40 
    
    
    unmove(cnt-1, startCnt, arrPos, nextNum, num)
    
    
    
    
def dfs(pos):
    
    global points
    global maxPoints
    
    
    if pos == 4:
        print(arr)
        print(points)
        maxPoints = max(maxPoints, points)
        return 
    
    
    for i in range(4):
        if arr[i] == 100:
            continue
        
        cnt = dices[pos]
        
        move(cnt, cnt, i, arr[i], -1)
        print(pos, i, arr[i])
        pos += 1 
        dfs(pos)
        pos -= 1 
        if arr[i] == 100:
            unmove(tmpCnt, cnt, i, arr[i], -1)
        else:
            points -= arr[i]
            unmove(cnt, cnt, i, arr[i], -1)


pos = 0 


for i in range(4):
    move(dices[pos], dices[pos], i, arr[i], -1)
    print(pos, i, arr[i])
    pos += 1 
    dfs(pos)
    pos -= 1
    if arr[i] == 100:
        unmove(tmpCnt, tmpCnt, i, arr[i], -1)
    else:
        points -= arr[i]
        unmove(dices[pos], dices[pos], i, arr[i], -1)


print(maxPoints)




