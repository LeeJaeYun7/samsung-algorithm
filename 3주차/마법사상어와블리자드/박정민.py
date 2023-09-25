from collections import deque

N,M=map(int,input().split())
score=[0]*3
board=[list(map(int,input().split())) for _ in range(N)]
cmd=[]
for i in range(M):
    x,y=map(int,input().split())
    cmd.append([x,y])
board_index=deque()
def check():
    nx = N // 2
    ny = N // 2

    dx=[0,1,0,-1]
    dy=[-1,0,1,0]

    d=0



    while True:

        for i in range(4):

            if i%2==0:
                d+=1

            for j in range(d):
                nx+=dx[j]
                ny+=dy[j]

                board_index.append((nx,ny))
                if nx==0 and ny==0:
                    break



def magic(d,dist):

    x=N//2
    y=N//2
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    for i in range(dist):

        nx=x+dx[d]
        ny=y+dy[d]
        if 0<=nx<N and 0<=ny<N:
            board[nx][ny]=0

    blank()




def blank():
    blankIdx=deque()

    for x,y in board_index:
        if board[x][y]==0:
            blankIdx.append((x,y))

        elif board[x][y]>0 and blankIdx:
            nx,ny=blankIdx.popleft()
            board[nx][ny]=board[x][y]
            board[x][y]=0
            blankIdx.append((x,y))

def bomb():
    v=deque()
    cnt=1

    num=board_index[0][0]

    for x,y in board_index:

        if x== N//2 and y==(N//2)-1:
            continue

        if num==board[x][y]:
            v.append((x,y))
            cnt+=1
        else:
            if cnt>=4:
                score[num-1]+=cnt

            while v:
                nx,ny=v.popleft()
                if cnt>=4:
                    board[nx][ny]=0


            num=board[x][y]
            cnt=1














check()

for x,y in cmd:
    magic(x,y)

