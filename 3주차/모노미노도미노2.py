'''
t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
'''
N = int(input())
blocks = []
for _ in range(N):
    t,x,y = map(int, input().split())
    blocks.append([t,x,y])

blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]

def move_blue(t, x): # 블록 번호, 현재 행
    if t == 1 or t == 2: # 현재 행에서 열 끝까지 증가시켜서 이동 
        y = 0 # 이동시킬 열 
        for i in range(6):
            if blue[x][i] == 1: # 이미 차있는 열에 부딪히면
                break
            y += 1

        y -= 1 
        blue[x][y] = 1
        if t == 2:
            blue[x][y-1] = 1

    else: # 두 행에 대해서 이동
        y = 0
        for i in range(6):
            if blue[x][i] == 1 or blue[x+1][i] == 1: 
                break
            y += 1
        
        y -= 1
        blue[x][y], blue[x+1][y] = 1,1

def move_green(t, y): # 블록 번호, 현재 열
    if t == 1 or t == 3: # 현재 열에서 행 끝까지 증가시켜서 이동 
        x = 0 # 이동시킬 행
        for i in range(6):
            if green[i][y] == 1:
                break
            x += 1

        x -= 1
        green[x][y] = 1
        if t == 3:
            green[x-1][y] = 1

    else: # 두 열에 대해서 이동
        x = 0
        for i in range(6):
            if green[i][y] == 1 or green[i][y+1] == 1:
                break
            x += 1
        
        x -= 1
        green[x][y], green[x][y+1] = 1,1

def remove_blue(y): # 삭제할 열 인덱스
    for i in range(4): # 각 행에 대해서
    #    blue[i][y] = 0 # 그 열의 타일이 모두 사라짐
        for j in range(y, -1, -1): # 오른쪽으로 한 칸씩 이동
            if j == 0:
                blue[i][j] = 0
            else:
                blue[i][j] = blue[i][j-1]
    
def remove_green(x): # 삭제할 행 인덱스 x = 4
    for j in range(4): # 각 열에 대해서
        for i in range(x, -1, -1): # 아래로 한 칸씩 이동
            if i == 0:
                green[i][j] = 0
            else:
                green[i][j] = green[i-1][j]

score = 0
for block in blocks:
    t,x,y = block
    move_blue(t,x)
    move_green(t,y)

    for j in range(6): # Blue에서 가득 차있는 열 확인
        cnt = 0
        for i in range(4): # 행
            if blue[i][j] == 1 :
                cnt += 1
        if cnt == 4:
            score += 1
            remove_blue(j) # 현재 열 삭제
    
    for j in range(0,2): # 0, 1번 열에 블록이 있으면
        for i in range(4):
            if blue[i][j]: 
                remove_blue(5)
                break
    
    for i in range(6): # Green에서 가득 차있는 행 확인
        if sum(green[i]) == 4:
            score += 1
            remove_green(i) # 현재 행 삭제

    # 연한 칸에 블록이 있는 경우
    if sum(green[0]): # 0, 1번 행에 블록이 있으면
        remove_green(5) # 맨 아래 행 삭제
    if sum(green[1]):
        remove_green(5) 

print(score)
ans = 0
for i in range(6):
    for j in range(4):
        ans += blue[j][i]
        ans += green[i][j]
print(ans)
