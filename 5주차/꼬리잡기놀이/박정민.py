import copy
from collections import deque
N,M,K=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]



dx=[0,0,-1,1]
dy=[-1,1,0,0]
def in_range(x,y):

    if 0<=x<N and 0<=y<N:
        return True
    return False
def find_tail(pos):

    q=deque()
    q.append(pos)
    tv=[[False]*N for _ in range(N)]

    while q:

        x,y=q.popleft()

        tv[x][y]=True

        if board[x][y]==3:
            return x,y

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if in_range(nx,ny) and board[nx][ny]!=0 and tv[nx][ny]==False:
                tv[nx][ny]=True
                q.append((nx,ny))

def move():

    global board

    #print("move 안의",team_order)
    new_board=copy.deepcopy(board)

    for idx in range(M):

        hx,hy= team[idx][0]
        tx,ty= team[idx][1]

        for i in range(4):
            nx=hx+dx[i]
            ny=hy+dy[i]

            if in_range(nx,ny) and board[nx][ny]==4:
                board[nx][ny]=1
                board[hx][hy]=2
                break
            elif in_range(nx,ny) and board[nx][ny]==3:
                board[nx][ny]=1
                board[hx][hy]=2
                break
        # tail
        # print("move안에서 머리 움직임")
        # for i in board:
        #     print(i)
        # print()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if in_range(nx, ny) and  (board[nx][ny]==2) and ([nx,ny]==team_order[idx][-2]):
                #print(nx,ny)
                board[nx][ny]=3

                if board[tx][ty]==1:
                    board[tx][ty]=1
                elif board[tx][ty]==3:
                    board[tx][ty]=4
                break

                # new_board[nx][ny]=3
                #
                # if new_board[tx][ty]==1:
                #     new_board[tx][ty]=1
                # elif new_board[tx][ty]==3:
                #     new_board[tx][ty]=4
                #
                # break

                # if board[nx][ny]==2:
                #     new_board[nx][ny]=3
                #     if new_board[tx][ty]==1:
                #         new_board[tx][ty]=1
                #     else:
                #         new_board[tx][ty]=4
                #     break

                #
                # if board[nx][ny] ==2:
                #     new_board[nx][ny]=3
                #
                #     if new_board[tx][ty]==1:
                #         break
                #
                #     elif new_board[tx][ty]==3:
                #         new_board[tx][ty]=4
                #         break




# 머리 꼬리 찾기
def find_head_tail():
    team = [[] for _ in range(M)]
    visited=[[False]*N for _ in range(N)]

    idx=0
    for i in range(N):
        for j in range(N):
            if visited[i][j]==False and board[i][j]==1:
                #print(i,j)
                team[idx].append([i,j])

                # 꼬리찾기

                ti,tj=find_tail((i,j))
                team[idx].append([ti,tj])
                idx+=1

    return team

def order():

    t=[[] for _ in range(M)]
    for i in range(M):

        # 머리
        x,y=team[i][0]
        tx,ty=team[i][1]

        t[i].append([x,y])

        q=deque()
        vo=[[False]*N for _ in range(N)]

        q.append((x,y))
        vo[x][y]=True

        while q:

            x,y=q.popleft()

            for ia in range(4):

                nx=x+dx[ia]
                ny=y+dy[ia]

                if in_range(nx,ny) and vo[nx][ny]==False and board[nx][ny]!=0 and board[nx][ny]!=4 and board[nx][ny]!=3:
                    q.append((nx,ny))
                    vo[nx][ny]=True
                    t[i].append([nx,ny])
                    break
        t[i].append([tx,ty])
    return t


def change_dir(p):
    global board
    temp=[]
    for i in range(len(p)-1,-1,-1):
        temp.append(p[i])

    aidx=0
    for x,y in temp:
        if aidx==0:
            board[x][y]=1
            aidx+=1

        elif aidx==len(temp)-1:
            board[x][y]=3

        else:
            board[x][y]=2
            aidx+=1

    return temp

def ball_right(r):
    # r = 1~7
    #flag=False
    for i in range(N):
        if board[r-1][i]!=0 and board[r-1][i]!=4:
            pos=[r-1,i]


            for j in range(M):

                if pos in team_order[j]:
                    #print(pos)
                    pos_idx=team_order[j].index(pos)
                    score[j]+=(pos_idx+1)*(pos_idx+1)
                    #flag=True

                    too=change_dir(team_order[j])
                    team_order[j]=too
                    #
                    return
            #if flag:
                #break
def ball_up(r):
    # r= 1~7
    for i in range(N):
        flag = False
        if board[N-1-i][r-1] != 0 and board[N-1-i][r-1] != 4:

            pos = [N-1-i,r-1]
            #print(pos)
            for j in range(M):

                if pos in team_order[j]:
                    pos_idx = team_order[j].index(pos)
                    #p#rint(team_order[j])
                    #print(pos_idx)
                    score[j] += (pos_idx + 1) * (pos_idx + 1)

                    too = change_dir(team_order[j])
                    team_order[j] = too

                    return
def ball_left(r):
    # r 1~7
    for i in range(N):
        #print(N)
        #print(r)

        #print(N-r,N-1-i)
        if board[N-r][N-1-i] != 0 and board[N-r][N-1-i] != 4:
            pos =[N-r,N-1-i]

            for j in range(M):

                if pos in team_order[j]:
                    pos_idx = team_order[j].index(pos)
                    score[j] += (pos_idx + 1) * (pos_idx + 1)

                    #print(pos)

                    too = change_dir(team_order[j])
                    team_order[j] = too

                    return
def ball_down(r):
    # r 1~7
    for i in range(N):

        if board[i][N-r] != 0 and board[i][N-r] != 4:

            pos = [i,N-r]

            for j in range(M):

                if pos in team_order[j]:
                    pos_idx = team_order[j].index(pos)
                    score[j] += (pos_idx + 1) * (pos_idx + 1)

                   # print(pos)

                    too = change_dir(team_order[j])
                    team_order[j] = too

                    return


score=[0]*M
#
count=0
for round in range(1,K+1):
    round=round%(4*N)
    if round==0:
        round=4*N

    #print(round,"round")
    #
    # print("move 전")
    # for i in board:
    #     print(i)
    # print()
    team=find_head_tail() # 머리 꼬리만
    team_order=order()

    move()
    team=find_head_tail()
    team_order=order()


    # print("move 후")
    # for i in board:
    #
    #     print(i)
    # print()
    if 1<=round<=N:
        r=round%N
        if r==0:
            r=N
        count+=1
        ball_right(r)

    elif N+1<=round<=2*N:
        r=round%N
        if r==0:
            r=N
        count+=1
        ball_up(r)

    elif (2*N)+1 <= round <=3*N:
        r=round%N
        if r==0:
            r=N
        count+=1
        ball_left(r)

    elif (3*N)+1 <= round <= 4*N:
        r=round%N
        if r==0:
            r=N
        count+=1
        ball_down(r)

    team = find_head_tail()
    team_order = order()
    # print("볼 맞으면 방향 바굼")
    # for i in board:
    #     print(i)
    # print()
    #
    # print("머리,꼬리",team)
    # print("팀 순서")

    # for i in team_order:
    #     print(i)
    # print(score)
    # print()
    # print()
    # print()
    # print()



print(sum(score))
#print(count)
