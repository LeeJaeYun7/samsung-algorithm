from copy import deepcopy

N = int(input())
n = N
board = [list(map(int, input().split())) for _ in range(N)]
count = 0


# 8  2
# 0  4
# 0  4
# 2  2
def up(board):
    for j in range(N):
        ptr = 0

        for i in range(1, N):

            if board[i][j]:

                temp = board[i][j]
                board[i][j] = 0

                if board[ptr][j] == temp:
                    board[ptr][j] *= 2
                    ptr += 1

                elif board[ptr][j] == 0:
                    board[ptr][j] = temp

                else:

                    ptr += 1
                    board[ptr][j] = temp

    return board


def down(board):
    for i in range(N):
        ptr = N - 1

        for j in range(N - 2, -1, -1):

            if board[j][i]:

                temp = board[j][i]
                board[j][i] = 0

                if board[ptr][i] == temp:
                    board[ptr][i] *= 2
                    ptr -= 1

                elif board[ptr][i] == 0:
                    board[ptr][i] = temp

                else:

                    ptr -= 1
                    board[ptr][i] = temp


    return board

def left(board):
    for i in range(N):
        ptr = 0

        for j in range(1, N):

            if board[i][j]:

                temp = board[i][j]
                board[i][j] = 0

                if board[i][ptr] == temp:

                    board[i][ptr] *= 2
                    ptr += 1

                elif board[i][ptr] == 0:
                    board[i][ptr] = temp

                else:
                    ptr += 1
                    board[i][ptr] = temp

    return board

# 2 2 2 2
def right(board):
    for i in range(N):
        ptr = N - 1

        for j in range(N-2,-1,-1):

            if board[i][j]:

                temp = board[i][j]
                board[i][j] = 0

                if board[i][ptr] == temp:

                    board[i][ptr] *= 2
                    ptr -= 1

                elif board[i][ptr] == 0:
                    board[i][ptr] = temp

                else:
                    ptr -= 1
                    board[i][ptr] = temp

    return board


def dfs(board,count):
    if count == 5:
        maxNum = -1
        for i in range(N):
            for j in range(N):
                maxNum = max(maxNum, board[i][j])

        return maxNum

    return max(dfs(up(deepcopy(board)), count + 1), dfs(right(deepcopy(board)), count + 1),
               dfs(left(deepcopy(board)), count + 1), dfs(down(deepcopy(board)), count + 1))


print(dfs(board, 0))
