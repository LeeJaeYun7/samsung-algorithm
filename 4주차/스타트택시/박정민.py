from collections import deque

N,M,fuel=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]

sx,sy=map(int,input().split())

taxi=[sx-1,sy-1]

start=[]
end=[]

for i in range(M):
    a,b,c,d=map(int,input().split())
    start.append([a-1,b-1])
    end.append([c-1,d-1])


def find_passenger(taxi):


    v=[[0]*N for _ in range(N)]
    minNum=1e9

    q=deque()
    q.append(taxi)

    answer=[]

    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    while q:

        x, y = q.popleft()

        if v[x][y]>minNum:
            break

        if [x,y] in start:
            minNum=v[x][y]
            answer.append([x,y])

        else:
            for idx in range(4):
                nx=x+dx[idx]
                ny=y+dy[idx]

                if 0<=nx <N and 0<=ny <N:
                    if board[nx][ny]!=1 and v[nx][ny]==0:
                        q.append((nx,ny))
                        v[nx][ny]=v[x][y]+1




    if answer:

        answer.sort()
        return v[answer[0][0]][answer[0][1]],answer[0][0],answer[0][1]

    else:
        return -1,-1,-1


def find_destination(start,end):

    q=deque()
    q.append(start)

    v=[[0]*N for _ in range(N)]

    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    while q:

        x, y = q.popleft()

        if [x,y] == end:
            break



        for idx in range(4):
            nx=x+dx[idx]
            ny=y+dy[idx]

            if 0<=nx <N and 0<=ny <N:
                if board[nx][ny]!=1 and v[nx][ny]==0:
                    q.append((nx,ny))
                    v[nx][ny]=v[x][y]+1

    return v[x][y],x,y


def find_des(start,end):
    q=deque()
    q.append(start)

    visited=[[0]*N for _ in range(N)]

    while q:
        x,y=q.popleft()

        if [x,y]==end:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return visited[x][y],x,y









for _ in range(M):

    d,px,py=find_passenger(taxi)


    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    if fuel-d <0 or d== -1:
        fuel=-1
        break

    fuel-=d

    idx=start.index([px,py])
   ###
    start[idx]=[-1,-1]

    d2,px2,py2=find_destination([px,py],end[idx])
    # if [px2, py2] != end[idx] or fuel - d < 0:
    #     fuel = -1
    #     break
    #print(d2,px2,py2)
    #print(fuel-d2)
    if [px2,py2]!=end[idx] or fuel-d2< 0:
        fuel=-1
        #print("a")
        break
    #print(px2,py2,d2)
    fuel+=d2
    taxi=[px2,py2]
print(fuel)

