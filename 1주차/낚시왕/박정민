r, c, m = map(int, input().split())


board = [[[] for _ in range(c)] for _ in range(r)]

# 방향 상, 하, 우, 좌
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    board[x-1][y-1] = [s, d, z]

def move_fish():
    new_board = [[[] for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y]:
                s, d, z = board[x][y]
                nx, ny = x, y
                for _ in range(s):
                    if 0 <= nx + dx[d] < r and 0 <= ny + dy[d] < c:
                        nx += dx[d]
                        ny += dy[d]
                    else:
                        d = (d + 1) % 4
                        nx += dx[d]
                        ny += dy[d]
                if not new_board[nx][ny] or new_board[nx][ny][2] < z:
                    new_board[nx][ny] = [s, d, z]
    return new_board

def catch_fish(col):
    for row in range(r):
        if board[row][col]:
            size = board[row][col][2]
            board[row][col] = []
            return size
    return 0

total_size = 0

for col in range(c):
    total_size += catch_fish(col)
    board = move_fish()

print(total_size)
