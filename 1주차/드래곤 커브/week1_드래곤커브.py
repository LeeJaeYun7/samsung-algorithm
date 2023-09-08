
n = int(input())

info = []
for _ in range(n):
    info.append(list(map(int, input().split()))) # x와 y는 시작 좌표, d는 시작 방향, g는 세대

def draw(x,y,d,g):
    dirs = [d] # 모든 세대들의 방향 정보를 저장할 리스트
    board[x][y] = 1 # 시작점 

    dy = [0,-1,0,1]
    dx = [1,0,-1,0]

    for i in range(g):
        tmp = []
        for j in range(len(dirs)):
            # 방향 순환 규칙 찾기
            # 이전 세대들을 돌면서 뒤에서부터 방향에 1씩 더하고 4로 나누기
            tmp.append((dirs[-j-1]+1)%4)
        dirs.extend(tmp)

    for i in dirs: # 계산한 방향에 따라 한칸씩 이동하면서 표시
        nx = x + dx[i]
        ny = y + dy[i]
        board[nx][ny] = 1
        x,y = nx,ny   

board = [[0]*101 for _ in range(101)]

for i in range(len(info)):
    x,y,d,g = info[i]

    draw(x,y,d,g)

ans = 0
# 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수 
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            ans += 1 

print(ans)