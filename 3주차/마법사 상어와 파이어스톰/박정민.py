import copy
from collections import deque

N,Q=map(int,input().split())

board=[]

for i in range(2**N):
    board.append(list(map(int,input().split())))

N=2**N

stage=list(map(int,input().split()))

def rotate(n):
    n=2**n

    new_board=[[0]*N for _ in range(N)]

    for i in range(0,N,n):
        for j in range(0,N,n):

            for x in range(n):
                for y in range(n):
                    new_board[i+y][j+n-1-x]=board[i+x][y+j]

    return new_board

def melt(board):

    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    new_board=copy.deepcopy(board)
    for i in range(N):
        for j in range(N):

            cnt=0

            for d in range(4):

                nx=i+dx[d]
                ny=j+dy[d]

                if 0<=nx<N and 0<=ny<N:
                    if board[nx][ny]>=1:
                        cnt+=1

            if cnt<=2:
                new_board[i][j]-=1

    return new_board


def bfs():

    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    maxCnt=0
    visited=[[False]*N for _ in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):

            if visited[i][j]==False and board[i][j]>0:
                q=deque()

                q.append((i,j))
                visited[i][j]=True

                cnt=1
                while q:
                    x,y=q.popleft()

                    for d in range(4):
                        nx=x+dx[d]
                        ny=y+dy[d]

                        if 0<=nx<N and 0<=ny<N:
                            if visited[nx][ny]==False and board[nx][ny]>=1:
                                visited[nx][ny]=True
                                q.append((nx,ny))
                                cnt+=1
            maxCnt=max(maxCnt,cnt)
    return maxCnt




for num in stage:

    board=rotate(num)
    board=melt(board)

answer=0
for i in range(N):
    for j in range(N):
        if board[i][j]>=1:
            answer+=board[i][j]
print(answer)
print(bfs())



