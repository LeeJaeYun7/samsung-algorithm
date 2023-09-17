from collections import deque
import sys

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

now_x, now_y = 0,0
now_size = 2

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x,now_y = i,j
            array[i][j] = 0

def bfs():
    q = deque()
    q.append((now_x,now_y))
    dist = [[-1]*n for _ in range(n)]
    dist[now_x][now_y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and dist[nx][ny]==-1 and array[nx][ny]<=now_size:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx,ny))
    
    return dist

def find(dist):
    min_dist = sys.maxsize
    x,y = 0,0
    for i in range(n):
        for j in range(n):
            if dist[i][j]!=-1 and 0<array[i][j]<now_size:
                if min_dist>dist[i][j]:
                    x,y = i,j
                    min_dist = dist[i][j]
    if min_dist == sys.maxsize:
        return None
    else:
        return x,y,min_dist

result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0],value[1]
        result += value[2]
        ate+=1
        array[now_x][now_y] = 0
        if ate==now_size:
            now_size+=1
            ate = 0
