n, m = map(int, input().split())

array = []
cctv = []
type = [[], # 각 cctv 종류별로 가능한 방향 모두 
        [[0],[1],[2],[3]], # 1번 
        [[0,1], [2,3]], # 2번 
        [[0,2],[1,2],[1,3],[0,3]], # 3번 
        [[0,1,2],[0,1,3],[0,2,3],[1,2,3]], # 4번 
        [[0,1,2,3]]  # 5번 
        ]

for i in range(n): # 0은 빈 칸, 6은 벽, 1~5는 CCTV
    tmp = list(map(int, input().split()))
    array.append(tmp)
    for j in range(m): 
        if tmp[j] in [1,2,3,4,5]: # cctv 정보는 따로 저장
            cctv.append([tmp[j],i,j]) # [종류, x좌표, y좌표]

def draw(array, x,y, dirs): # 현재 위치, 감시방향 리스트 (1d)
    dx = [0,0,-1,1] # 오 왼 위 아래
    dy = [1,-1,0,0]
    for dir in dirs:
        nx, ny = x, y
        while True: # 현재 위치에서 벽에 닿거나 범위를 벗어날때까지 직진
            nx += dx[dir]
            ny += dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: 
                break # 벽이거나, 범위를 벗어나면
            if array[nx][ny] == 6:
                break

            elif array[nx][ny] == 0: # 빈칸이면 감시 영역 표시
                array[nx][ny] = 7 

def dfs(cctv_num, array):
    global ans
    if cctv_num == len(cctv): # DFS 탐색 종료 조건 
        cnt = 0
        for i in range(n):
            cnt += array[i].count(0) # 사각지대 개수 세기
        ans = min(ans, cnt) # 최소 개수 
        return
    
    t, x, y = cctv[cctv_num] 
    tmp = deepcopy(array)
    for i in type[t]: # when t = 3, [[0,2],[1,2],[1,3],[0,3]]
        draw(tmp, x,y, i)
        dfs(cctv_num + 1, tmp)
        tmp = deepcopy(array) 

import sys
from copy import deepcopy

ans = sys.maxsize
dfs(0, array)
print(ans)
