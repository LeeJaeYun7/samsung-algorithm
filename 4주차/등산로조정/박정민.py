from collections import deque

test_case = int(input())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


#
def dfs(x, y, cnt):
    global maxLen, visited
    maxLen = max(maxLen, visited[x][y])

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
            continue
        if board[x][y] > board[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, cnt)
            visited[nx][ny] = 0
        elif cnt and board[nx][ny] - K < board[x][y]:
            temp = board[nx][ny]
            board[nx][ny] = board[x][y] - 1


            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, cnt - 1)

            visited[nx][ny] = 0
            board[nx][ny] = temp







for test in range(1, test_case + 1):
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    maxH = 0
    for i in range(N):
        for j in range(N):
            maxH = max(maxH, board[i][j])

    maxLen = 0
    start_pos=[]
    for i in range(N):
        for j in range(N):
            if board[i][j]==maxH:
                start_pos.append((i,j))
    visited = [[0] * N for _ in range(N)]

    for i,j in start_pos:

        visited[i][j] = 1
        dfs(i, j, 1)
        visited[i][j] = 0

    print("#{} {}".format(test, maxLen))
