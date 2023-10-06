# M명의 승객 N*N 격자
# 가장 최단거리가 가장 짧은 승객
# 연료는 한 칸 이동할 때마다 1만큼 소모된다. 
# 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전

from collections import deque 

N,M,power = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

taxiX, taxiY = map(int, input().split())
taxiX -= 1
taxiY -= 1

src = []
dst = []
for _ in range(M): # 각 승객의 출발지의 행과 열 번호, 목적지의 행과 열 번호
    srcX, srcY, dstX, dstY = map(int, input().split())
    src.append([srcX-1, srcY-1])
    dst.append([dstX-1, dstY-1])


def bfs(taxiX, taxiY):
    # 현재 택시위치에서 모든 칸에 대해서 BFS탐색으로 dist 배열 갱신
    dist = [[-1]*N for _ in range(N)]
    dist[taxiX][taxiY] = 0 # 택시 위치

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append([taxiX, taxiY])

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and dist[nx][ny] == -1 and board[nx][ny] == 0: # 범위 내에 있고 방문하지 않았고 빈칸이라면 
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])
    return dist

# 1. 현재 택시의 위치에서 가장 최단거리가 짧은 승객을 고른다. 
def getCustomer(taxiX, taxiY, src): 
    dist = bfs(taxiX, taxiY)
    minDist = float('inf')
    minX, minY = 0, 0
    minNum = None
    
    
    for i in range(len(src)):
        if dist[src[i][0]][src[i][1]] == -1:
            continue # 도착할 수 없는 손님

        print(i,"번째 손님")
        print("거리 ", dist[src[i][0]][src[i][1]])
        if dist[src[i][0]][src[i][1]] > minDist: 
            continue

        # dist[src[i][0]][src[i][1]] <= minDist: 
        # dist 최소 거리보다 같거나 작은 경우만 남는다
        if dist[src[i][0]][src[i][1]] == minDist: # 같을 때 행 번호가 더 크면
            if src[i][0] > minX:
                continue
            
            # 행번호도 같거나 작을 때
            if src[i][0] == minX and src[i][1] > minY:
                continue

        minX, minY, minNum = src[i][0], src[i][1], i
        minDist = dist[src[i][0]][src[i][1]]

    if minNum is None: # 도착할 수 있는 손님이 아무도 없으면
        return [None, None, None, None]

    return [minX, minY, minDist, minNum]

def moveToDst(taxiX, taxiY, dstNum, dst):
    dist = bfs(taxiX, taxiY) 
    # 손님의 출발지 (택시 현재 위치)에서 손님의 목적지까지 최단 거리
    dstX, dstY = dst[dstNum][0], dst[dstNum][1]
    return [dstX, dstY, dist[dstX][dstY]] # 손님의 목적지 좌표, 주행거리
    

powerOff = False

while True:
    # 최단거리 손님 정보 가져오기
    minX, minY, minDist, minNum = getCustomer(taxiX, taxiY, src)
    if minX is None:
        powerOff = True
        break

    power -= minDist
    print("최단거리 손님정보 가져오기")
    print(minX, minY, minDist, minNum)
    if power < 0:
        powerOff = True
        break
    print("승객 픽업 완료")
    # 주행거리
    dstX, dstY, moveDist = moveToDst(minX, minY, minNum, dst)
    print("승객 도착지 정보", [dstX, dstY, moveDist])
    power -= moveDist
    if power < 0:
        powerOff = True
        break
    print("남은 연료: ",power)
    
    # 택시의 좌표값 업데이트 & 도착한 손님 제거
    taxiX, taxiY = dstX, dstY
    power += 2*moveDist
    print("충전된 연료: ",power)
    print("택시의 현재 위치",(taxiX, taxiY))
    del src[minNum]
    del dst[minNum]

    if not src: # 손님이 더이상 없으면
        break

if src or powerOff: 
    print(-1)
else:
    print(power)




# M명의 승객 N*N 격자
# 가장 최단거리가 가장 짧은 승객
# 연료는 한 칸 이동할 때마다 1만큼 소모된다. 
# 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전

from collections import deque 

N,M,power = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

taxiX, taxiY = map(int, input().split())
taxiX -= 1
taxiY -= 1

src = []
dst = []
for _ in range(M): # 각 승객의 출발지의 행과 열 번호, 목적지의 행과 열 번호
    srcX, srcY, dstX, dstY = map(int, input().split())
    src.append([srcX-1, srcY-1])
    dst.append([dstX-1, dstY-1])


def bfs(taxiX, taxiY):
    # 현재 택시위치에서 모든 칸에 대해서 BFS탐색으로 dist 배열 갱신
    dist = [[-1]*N for _ in range(N)]
    dist[taxiX][taxiY] = 0 # 택시 위치

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append([taxiX, taxiY])

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and dist[nx][ny] == -1 and board[nx][ny] == 0: # 범위 내에 있고 방문하지 않았고 빈칸이라면 
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])
    return dist

# 현재 택시의 위치에서 가장 최단거리가 짧은 승객을 고른다. 
def getCustomer(taxiX, taxiY, src): 
    dist = bfs(taxiX, taxiY)
    minDist = float('inf')
    minX, minY = 0, 0
    minNum = None
    
    
    for i in range(len(src)):
        if dist[src[i][0]][src[i][1]] == -1:
            return [None, None, None, None] # 도착할 수 없는 손님
        
        if dist[src[i][0]][src[i][1]] > minDist: 
            continue

        # dist 최소 거리보다 같거나 작은 경우만 남는다
        if dist[src[i][0]][src[i][1]] == minDist: # 같을 때 행 번호가 더 크면
            if src[i][0] > minX:
                continue
            
            # 행번호도 같거나 작을 때
            if src[i][0] == minX and src[i][1] > minY:
                continue

        minX, minY, minNum = src[i][0], src[i][1], i
        minDist = dist[src[i][0]][src[i][1]]

    if minNum is None: # 도착할 수 있는 손님이 아무도 없으면
        return [None, None, None, None]

    return [minX, minY, minDist, minNum]

def moveToDst(taxiX, taxiY, dstNum, dst):
    dist = bfs(taxiX, taxiY) 
    # 손님의 출발지 (택시 현재 위치)에서 손님의 목적지까지 최단 거리
    dstX, dstY = dst[dstNum][0], dst[dstNum][1]
    return [dstX, dstY, dist[dstX][dstY]] # 손님의 목적지 좌표, 주행거리
    

powerOff = False

while True:
    # 최단거리 손님 정보 가져오기
    minX, minY, minDist, minNum = getCustomer(taxiX, taxiY, src)
    if minX is None:
        powerOff = True
        break

    power -= minDist
    if power < 0:
        powerOff = True
        break
    
    # 주행거리
    dstX, dstY, moveDist = moveToDst(minX, minY, minNum, dst)
    power -= moveDist
    if power < 0:
        powerOff = True
        break
    
    # 택시의 좌표값 업데이트 & 도착한 손님 제거
    taxiX, taxiY = dstX, dstY
    power += 2*moveDist
    del src[minNum]
    del dst[minNum]

    if not src: # 손님이 더이상 없으면
        break

if src or powerOff: 
    print(-1)
else:
    print(power)
