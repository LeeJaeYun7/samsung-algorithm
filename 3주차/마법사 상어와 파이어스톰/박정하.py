# 2^N × 2^N인 격자, (r, c)는 격자의 r행 c열
# A[r][c]는 (r, c)에 있는 얼음의 양

# 파이어스톰: 단계 L 
# 1. 격자를 2L × 2L 크기의 부분 격자로 나눈다
# 2. 모든 부분 격자를 시계 방향으로 90도 회전
# 3. 얼음 칸 3개 이상과 인접하지 않은 칸은 얼음 1 줄어듬

# 파이어스톰 총 Q번 시전한 후
# 1. 남아있는 얼음 A[r][c]의 합
# 2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수

from collections import deque
N, Q = map(int,input().split())
A = []
for _ in range(2**N):
    A.append(list(map(int,input().split())))

L = list(map(int,input().split()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def rotate(submatrix):
    n = len(submatrix)
    ret = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            ret[y][n-1-x] = submatrix[x][y]
    return ret

def decrease_ice(submatrix):
    n = len(submatrix)
    for x in range(n):
        for y in range(n):
            cnt = 0 # 모든 칸에 대해서 인접한 얼음 칸 개수 count
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n and submatrix[nx][ny]: # 범위 안에 있고 얼음이 있다면
                    cnt += 1
            if cnt < 3:
                submatrix[x][y] -= 1 # 얼음 양 1 감소
    return submatrix

def printt(m):
    for r in m:
        print(r)

for l in L:
    for n in range(0, 2**N, 2**l): # 전체 격자를 2**L x 2**L 부분 격자로 나누기
        submatrix = [r[n:n+2**l] for r in A[n:n+2**l]] # 부분 격자 
        submatrix = rotate(submatrix) 

        ii = 0 # 전체 격자에 수정된 부분 격자 반영
        for i in range(n, n+2**l): # 0 1
            jj = 0
            for j in range(n, n+2**l): # 0 1
                A[i][j] = submatrix[ii][jj]
                jj += 1
            ii += 1

ice = 0
visited = [[0]*2**N for _ in range(2**N)]
maxIce = 0

for x in range(2**N):
    for y in range(2**N):
        currIce = 0
        if visited[x][y] or A[x][y] == 0:
            continue

        q = deque()
        q.append((x,y))
        visited[x][y] = 1

        while q:
            cx, cy = q.popleft()
            ice += A[cx][cy]
            currIce += 1
                    
            for i in range(4): # 인접 칸 확인
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0<=nx<2**N and 0<=ny<2**N and visited[nx][ny]==0 and A[nx][ny]: 
                    visited[nx][ny] = 1
                    q.append((nx,ny))

        maxIce = max(maxIce, currIce)

print(ice)
print(maxIce)
