from collections import deque

N,M=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]

command=[]
for i in range(M):
    d,s=map(int,input().split())
    command.append([d,s])

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

q=deque()
q.append((N-2,0))
q.append((N-2,1))
q.append((N-1,0))
q.append((N-1,1))



sx=[-1,-1,1,1]
sy=[-1,1,-1,1]


for d,s in command:

    visited=[[False]*N for _ in range(N)]


    while q:
        x,y=q.popleft()

        for i in range(s):
            x += dx[d-1]
            y += dy[d-1]
        x=(x+N)%N
        y=(y+N)%N

        visited[x][y]=True

        board[x][y]+=1




    for i in range(N):
        for j in range(N):
            cnt = 0

            if visited[i][j]:
                for n in range(4):
                    qx=i+sx[n]
                    qy=j+sy[n]

                    if 0<=qx <N and 0<=qy<N:
                        if board[qx][qy]>=1:
                            cnt+=1
                board[i][j]+=cnt


    for i in range(N):
        for j in range(N):
            if visited[i][j]==False and board[i][j]>=2:
                q.append([i,j])
                board[i][j]-=2





answer=0
for i in range(N):
    for j in range(N):
        answer+=board[i][j]

print(answer)







