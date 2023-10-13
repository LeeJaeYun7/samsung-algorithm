N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

time = [[0]*M for _ in range(N)] # 각 포탑의 공격 시점 정보 


def select():
    temp = [] # 살아남은 포탑들 정렬할 리스트
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0: # 부서지지 않은 포탑들
                temp.append((board[i][j], time[i][j], i+j, j, i)) # 공격력, 공격 시점, 행+열, 열

    # 공격력이 작은 순, 공격 시점이 큰 순, 행과 열이 큰 순, 열이 큰 순 -> 가장 약한 포탑
    temp.sort(key= lambda x: (x[0], -x[1], -x[2], -x[3]))

    _, _, _, weakY, weakX = temp[0] # 가장 약한 포탑
    _, _, _, strongY, strongX = temp[-1] # 가장 강한 포탑

    return weakX, weakY, strongX, strongY



from collections import deque

def bfs(sx, sy, tx, ty): # (sx, sy) ~ (tx, ty) 까지의 최단 경로 찾기
    dx = [0, 1, 0, -1] # 우/하/좌/상의 우선순위
    dy = [1, 0, -1, 0]
    visited = [[0]*M for _ in range(N)]

    q = deque()
    q.append((sx, sy, [(sx, sy)])) # 시작할 점과 경로

    while q:
        x, y, path = q.popleft()

        if (x, y) == (tx, ty): # 목적지에 도달한다면
            return path
        
        for i in range(4): # 상하좌우의 4개의 방향으로
            nx = (x + dx[i])%N
            ny = (y + dy[i])%M

            if board[nx][ny] > 0 and not visited[nx][ny]: # 부서지지 않았고 아직 방문하지 않은 칸
                visited[nx][ny] = 1
                q.append((nx, ny, path+[(nx, ny)]))

    return None # q가 비었는데 목적지에 도달하지 못했다면 

# 각 Attack함수: board[i][j]의 공격력 감소 , related list 갱신
# lazerAttack 함수: 레이저 공격이 가능하면 True 아니면 False
# lazerAttack() == False면 bombAttack 함수 호출

def lazerAttack(weakX, weakY, strongX, strongY):
    path = bfs(weakX, weakY, strongX, strongY) # (weakX, weakY)~(strongX, strongY) 최단 경로 존재하면 path list, 없으면 None

    if path == None: # 레이저 공격 불가능
        return False

    # 레이저 공격이 가능하면 (path != None 이면) 
    for x,y in path: 

        related.append((x,y)) # 공격에 관련된 포탑 추가
        
        if (x,y) == (weakX, weakY):
            continue

        # 공격력 감소
        if (x,y) == (strongX, strongY):
            board[x][y] -= board[weakX][weakY] # 공격 대상은 공격자 공격력만큼 감소
        else:    
            board[x][y] -= (board[weakX][weakY]) // 2 # 경로에 있는 포탑은 공격자 공격력의 절반 만큼 감소
    
    return True

def bombAttack(weakX, weakY, strongX, strongY): # 포탄 공격
    board[strongX][strongY] -= board[weakX][weakY] # 공격 대상은 공격자 공격력만큼 감소
    related.append((strongX, strongY))
    related.append((weakX, weakY))

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8): # 공격 대상 주위 8개의 방향에 있는 포탑
        nx = (strongX + dx[i])%N
        ny = (strongY + dy[i])%M
        if board[nx][ny] > 0 and (nx, ny) != (weakX, weakY): # 부서진 포탑이 아니고 공격자가 아니라면
            board[nx][ny] -= (board[weakX][weakY]) // 2 
            related.append((nx, ny))

def broken(): # 공격력이 0 이하가 된 포탑은 부서짐 
    for i in range(N):
        for j in range(M):
            if board[i][j] <= 0:
                board[i][j] = 0

def improve():
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and (i,j) not in related: # 부서지지 않은 포탑 중 공격과 무관했던 포탑
                board[i][j] += 1 # 공격력이 1씩 증가


def stop():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0: # 부서지지 않은 포탑 
                cnt += 1
    return cnt <= 1

for t in range(1, K+1): # K 번의 턴
    if stop():
        break

    related = [] # 각 턴마다 공격에 관련되어있는 포탑 list 보존 

    # 가장 약한 포탑과 가장 강한 포탑의 인덱스 선정
    weakX, weakY, strongX, strongY = select()

    time[weakX][weakY] = t # 공격자의 공격 시점 정보 업데이트 

    board[weakX][weakY] += (N+M) # 가장 약한 포탑의 공격력 N+M만큼 증가

    if not lazerAttack(weakX, weakY, strongX, strongY): # 레이저 공격이 안 된다면 (False)
        bombAttack(weakX, weakY, strongX, strongY) # 포탄 공격

    broken()
    improve()

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, board[i][j])

print(ans)
