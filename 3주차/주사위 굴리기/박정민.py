# 주사위는 지도위에 윗면이 1이고,
from collections import deque

N,M,K=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]


    # 위 아래 동  서 남 북
dice=[1,6,   3, 4, 5,2]

#
#dice=[
dice=[1,6,3,4,5,2]


right=[dice[3],dice[2],dice[0],dice[1],dice[4],dice[5]]

left=[dice[2],dice[3],dice[1],dice[0],dice[4],dice[5]]


up=[dice[4],dice[5],dice[3],dice[2],dice[1],dice[0]]

down=[dice[5],dice[4],dice[3],dice[2],dice[0],dice[1]]

direction=[right,down,left,up]
# 동 남 서 북
dx=[0,1,0,-1]
dy=[1,0,-1,0]

dir=0
sx,sy=0,0

def score(sx,sy):
    sum=0
    q=deque()

    current=board[sx][sy]
    q.append((sx,sy))
    v=[[False]*M for _ in range(N)]
    v[sx][sy]=True

    sum+=current
    while q:
        x,y=q.popleft()

        v[x][y]=True

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if v[nx][ny]==False and current==board[nx][ny]:
                    q.append((nx,ny))
                    sum+=board[nx][ny]
                    v[nx][ny]=True
    return sum

answer=0
for i in range(K):

    #print(dir)
    while True:

        sx+=dx[dir]
        sy+=dy[dir]
        #print(dir)
        print("dir", dir, " ", sx, sy)
        dice=direction[dir]
        if 0<=sx<N and 0<=sx <M:
            if dice[1]> board[sx][sy]:
                #print("@")
                dir=(dir+1)%4

            # 동 남 서 북
            # 0 1  2  3
            elif dice[1]<board[sx][sy]:
                dir=(dir+3)%4
                dir=dir-1
                if dir==-1:
                    dir=3
                print("sdad")
            answer+=score(sx,sy)
            print("dice", dice[1], "board", board[sx][sy])
            break
        else:
            print("@)")
            if dir==0:
                dir=1
            elif dir==1:
                dir=0
            elif dir==2:
                dir=3
            elif dir==3:
                dir=2

            print(dir,sx,sy)
            break

print(answer)







