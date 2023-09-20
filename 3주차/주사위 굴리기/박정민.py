# 주사위는 지도위에 윗면이 1이고,
from collections import deque

N, M, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


dice = [1, 6, 3, 4, 5, 2]


dice = [1, 6, 3, 4, 5, 2]


def roll(dir):
    right = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]
    left = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
    up = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
    down = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]

    direction = [right, down, left, up]

    return direction[dir]


def score(sx, sy):
    v = [[False] * M for _ in range(N)]
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = True

    current = board[sx][sy]


    sum = 0

    while q:
        x, y = q.popleft()
        sum+=current


        for i in range(4):
            qx = x + dx[i]
            qy = y + dy[i]

            if 0 <= qx < N and 0 <= qy < M:
                if v[qx][qy] == False and current == board[qx][qy]:
                    q.append((qx, qy))

                    v[qx][qy] = True


    return sum




# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = 0
answer = 0
sx, sy = 0, 0
nx, ny = 0, 0
for i in range(K):
    #print("nx,ny", nx, ny)
    nx = nx + dx[dir]
    ny = ny + dy[dir]

    # print(dx[dir],dy[dir])
    while True:

        if 0 <= nx < N and 0 <= ny < M:
            dice = roll(dir)
            answer += score(nx, ny)
            #answer+=score(nx,ny)

            if dice[1] > board[nx][ny]:
                dir = (dir + 1) % 4
            elif dice[1] < board[nx][ny]:

                dir -= 1
                if dir == -1:
                    dir = 3


            break
        else:

            nx = nx - dx[dir]
            ny = ny - dy[dir]

            dir = (dir + 2) % 4

            nx = nx + dx[dir]
            ny = ny + dy[dir]

print(answer)
