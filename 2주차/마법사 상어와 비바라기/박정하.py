n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

moves = []
for _ in range(m):
    moves.append(list(map(int, input().split())))

clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]] # 처음 구름 위치

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

def moveCloud(d,s): # 모든 구름이 d_i 방향으로 s_i칸 이동한다. 
    for i in range(len(clouds)):
        # 구름의 위치 좌표
        x,y = clouds[i][0], clouds[i][1]
        clouds[i][0] = (x + dx[d]*s)%n
        clouds[i][1] = (y + dy[d]*s)%n
    
def rain(): # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for cloud in clouds:
        x,y = cloud[0], cloud[1]
        graph[x][y] += 1
        visited[x][y] = 1 # 사라지는 구름 좌표 표시

def magic(): # 4. 물이 증가한 칸 (r, c)에 물복사버그 마법
    for cloud in clouds:
        x,y = cloud[0], cloud[1]
        for i in [1,3,5,7]: # 대각선 방향으로 거리가 1인 칸
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] > 0: # 물이 있는 바구니
                graph[x][y] += 1 # 물이 양이 증가

def makeCloud(): # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    global clouds
    new_clouds = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 2 and [x,y] and not visited[x][y]: # 3에서 구름이 사라진 칸이 아니어야 한다
                new_clouds.append([x,y])
                graph[x][y] -= 2
    clouds = new_clouds

for i in range(m):
    d,s = moves[i]
    visited = [[0]*n for _ in range(n)]
    moveCloud(d-1, s) #  cloud 정보 update
    rain() # cloud에 따라 graph 업데이트, cloud 초기화
    magic()
    makeCloud()
#    print(graph)

ans = 0
for x in range(n):
    for y in range(n):
        ans += graph[x][y]
print(ans)
