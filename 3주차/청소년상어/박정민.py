import copy

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]


board=[]
for i in range(4):
    t=list(map(int,input().split()))
    temp=[]

    for j in range(0,8,2):
        temp.append([t[j],t[j+1]-1])
    board.append(temp)

result=0

def find_fish(idx, board):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == idx:
                return (i, j)
    return None


def move_fish(board,sx,sy):

    for num in range(1,17):

        fish=find_fish(num,board)

        if fish !=None:

            i,j=fish
            dir=board[i][j][1]

            for d in range(8):

                nx=i+dx[dir]
                ny=j+dy[dir]

                if 0<=nx<4 and 0<=ny<4 and (nx,ny)!=(sx,sy):

                    board[i][j][1]=dir

                    board[nx][ny],board[i][j]=board[i][j],board[nx][ny]
                    break
                dir=(dir+1)%8

def shark_move(board,sx,sy):
    arr=[]
    dir=board[sx][sy][1]

    for _ in range(4):

        sx =sx+dx[dir]
        sy= sy+dy[dir]

        if 0<=sx<4 and 0<=sy<4 and board[sx][sy][0]!=-1:
            arr.append((sx,sy))
    return arr

def dfs(board,x,y,sum):
    global result

    board = copy.deepcopy(board)
    sum+=board[x][y][0]

    board[x][y][0]=-1

    move_fish(board,x,y)


    # for i in board:
    #     print(i)
    # print()
    # #return
    arr = shark_move(board,x,y)

    if len(arr)==0:
        result = max(result,sum)

    for nx,ny in arr:
        dfs(board,nx,ny,sum)

dfs(board,0,0,0)
print(result)
# board[0][0][0]=-1
# move_fish(board,0,0)
# for i in board:
#     print(i)
# print()


