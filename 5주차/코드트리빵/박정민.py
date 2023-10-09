from collections import deque

def bfs(x,y,cx,cy):
    global v
    q=deque()

    lst=[]
    q.append((x,y,lst))
    vvisited=[[False]*N for _ in range(N)]
    vvisited[x][y]=True

    dx=[-1,0,0,1]
    dy=[0,-1,1,0]
    t=0

    while q:
        t+=1
        x,y,l=q.popleft()

        if x==cx and y==cy:


            return l[0][0],l[0][1]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if vvisited[nx][ny]==False and v[nx][ny]==False:
                    q.append((nx,ny,l+[[nx,ny]]))
                    vvisited[nx][ny]=True
def find_base(ip):
    global v
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    x,y=conv[ip][0],conv[ip][1]
    q=deque()
    q.append((x,y))

    visited=[[0]*N for _ in range(N)]
    visited[x][y]=1

    while q:

        x,y=q.popleft()
        if board[x][y]==1:
            v[x][y]=True
            return x,y,
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N and v[nx][ny]==False and visited[nx][ny]==False:
                q.append((nx,ny))
                visited[nx][ny]=True


N,M=map(int,input().split())
board=[list(map(int,input().split()))for _ in range(N)]

conv=[]
for i in range(M):
    x,y=map(int,input().split())
    conv.append([x-1,y-1])

v=[[False]*N for _ in range(N)]


time=0
people=[[-1,-1] for _ in range(M)]

while True:

    time+=1

    for i in range(M):

        x,y=people[i][0],people[i][1]
        if x==-2 and y==-2:
            continue
        elif x!= -1 and y != -1:

            cx,cy=conv[i][0],conv[i][1]

            people[i][0],people[i][1]=bfs(x,y,cx,cy)

            if people[i][0]==cx and people[i][1]==cy:
                v[people[i][0]][people[i][1]]=True
                people[i][0]=-2
                people[i][1]=-2



    if time<=M:

        cx,cy=find_base(time-1)
        people[time-1][0]=cx
        people[time-1][1]=cy


    flag=True

    for i in range(M):
        if people[i][0]!= -2 and people[i][1]!=-2:
            flag=False

    if flag:
        print(time)
        break


