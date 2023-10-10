N, M, K = map(int, input().split())

gunBoard = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] > 0:
            gunBoard[i][j].append(row[j])

playersList = []
playersBoard = [[-1]*N for _ in range(N)]
for i in range(M):
    x, y, d, s = map(int, input().split())
    playersList.append([x - 1, y - 1, d, s, 0]) # x, y, 방향, 초기능력치
    playersBoard[x - 1][y - 1] = i

##################################################################################

scores = [0 for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def isVaild(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def getMove(idx):
    x, y = playersList[idx][0], playersList[idx][1]
    nx, ny = x + dx[playersList[idx][2]], y + dy[playersList[idx][2]]
    if not isVaild(nx,ny): # 격자를 벗어나는 경우에는 정반대 방향
        playersList[idx][2] = (playersList[idx][2] + 2)%4
        nx, ny = x + dx[playersList[idx][2]], y + dy[playersList[idx][2]]
    return nx, ny

def move(idx, nx, ny): # playersBoard와 playersList 정보 업데이트
    playersBoard[playersList[idx][0]][playersList[idx][1]] = -1
    playersList[idx][0], playersList[idx][1] = nx, ny
    playersBoard[nx][ny] = idx

def getGun(idx, nx, ny):
    maxGun = max(gunBoard[nx][ny]) # 제일 쎈 총
    if playersList[idx][4] == 0: # 플레이어가 가진 총이 없으면
        playersList[idx][4] = maxGun
        gunBoard[nx][ny].remove(maxGun)
    else: # 플레이어가 가진 총과 공격력 비교해서 쎈거 가짐
        playerGun = playersList[idx][4]
        if playerGun < maxGun:
            playersList[idx][4] = maxGun
            gunBoard[nx][ny].remove(maxGun)
            gunBoard[nx][ny].append(playerGun)


def fight(idx1, idx2): # 싸울 두 플레이어의 인덱스 
    s1, p1 = playersList[idx1][3], playersList[idx1][4]
    s2, p2 = playersList[idx2][3], playersList[idx2][4]
    if s1+p1 > s2+p2: 
        return idx1, idx2, abs(s1+p1-(s2+p2))
    elif s1+p1 < s2+p2:
        return idx2, idx1, abs(s1+p1-(s2+p2))
    else:
        if s1 > s2:
            return idx1, idx2, abs(s1+p1-(s2+p2))
        else:
            return idx2, idx1, abs(s1+p1-(s2+p2))

def getLoserMove(idx): # 진 플레이어가 이동할 수 있는 위치 찾기
    x,y = playersList[idx][0], playersList[idx][1]
    nx, ny = x + dx[playersList[idx][2]], y + dy[playersList[idx][2]]
    while not isVaild(nx,ny) or playersBoard[nx][ny] != -1: # 범위를 벗어났거나, 다른 플레이어가 있으면 
        playersList[idx][2] = (playersList[idx][2]+1)%4 # 오른쪽으로 90도 이동
        nx, ny = x + dx[playersList[idx][2]], y + dy[playersList[idx][2]]
    return nx,ny

def play():
    for i in range(M): # 각 M명의 플레이어에 대해서
        nx, ny = getMove(i) # i번째 플레이어가 이동할 칸 찾기
        
        if playersBoard[nx][ny] == -1: # 이동할 칸에 아무도 없다면
            move(i, nx, ny)
            if len(gunBoard[nx][ny]) != 0: # 이동할 칸에 총이 있다면
                getGun(i, nx, ny)
            
        else: # 이동할 칸에 다른 플레이어가 있다면 싸움
            winnerIdx, loserIdx, diff = fight(i, playersBoard[nx][ny])
            scores[winnerIdx] += diff
            move(i, nx, ny)

            # 진 플레이어
            gunBoard[nx][ny].append(playersList[loserIdx][4])
            playersList[loserIdx][4] = 0

            lx, ly = getLoserMove(loserIdx) # 진 플레이어가 이동할 칸
            move(loserIdx, lx, ly) # 진 플레이어 이동
            if len(gunBoard[lx][ly]) != 0: # 이동할 칸에 총이 있다면
                getGun(loserIdx, lx, ly)
            
            # 이긴 플레이어 총 교체
            getGun(winnerIdx, nx, ny) 
            playersBoard[nx][ny] = winnerIdx

for _ in range(K):
    play()

for i in scores:
    print(i, end=" ")
