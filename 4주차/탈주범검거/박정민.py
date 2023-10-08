from collections import deque

test_case=int(input())

for test in range(1,test_case+1):


    N,M,R,C,L=map(int,input().split())

    board=[list(map(int,input().split())) for _ in range(N)]




    q=deque()
    q.append((R,C))

    # 위아래 왼쪽 오른쪽
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    visieted=[[0]*M for _ in range(N)]
    visieted[R][C]=1
    possible=[[2,3,]]
    while q:

        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny <M and board[nx][ny]!=0:
                if visieted[nx][ny]==0:
                    if i==0: # 위로갈때
                        if board[x][y] in [1,2,4,7]:
                            if board[nx][ny] in [1,2,5,6]:
                                visieted[nx][ny]=visieted[x][y]+1
                                q.append((nx,ny))
                    elif i==1: #아래로갈때
                        if board[x][y] in [1,2,5,6]:
                            if board[nx][ny] in [1,2,4,7]:
                                visieted[nx][ny]=visieted[x][y]+1
                                q.append((nx,ny))

                    elif i==2: #왼쪽으로갈때
                        if board[x][y] in [1,3,6,7]:
                            if board[nx][ny] in [1,3,4,5]:
                                visieted[nx][ny]=visieted[x][y]+1
                                q.append((nx,ny))

                    elif i==3: #오른쪽으로갈때
                        if board[x][y] in [1,3,4,5]:
                            if board[nx][ny] in [1,3,6,7]:
                                visieted[nx][ny]=visieted[x][y]+1
                                q.append((nx,ny))

    pos=0

    for i in range(N):
        for j in range(M):
            if 1<=visieted[i][j]<=L:

                pos+=1

    print("#{} {}".format(test,pos))
