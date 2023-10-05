from collections import deque

N,M,fuel=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]

sx,sy=map(int,input().split())
taxi=[sx-1,sy-1]

start=[]
end=[]
for _ in range(M):
    x,y,p,q=map(int,input().split())
    start.append([x-1,y-1])
    end.append([p-1,q-1])



dx=[0,0,-1,1]
dy=[-1,1,0,0]

def find_person(taxi):
    q=deque()
    q.append(taxi)
    visited=[[0]*N for _ in range(N)]
    minNum= 1e9
    answer=[]

    while q:
        x,y=q.popleft()

        if visited[x][y] > minNum:
            break
        if [x, y] in start:  # 최단 경로 손님 찾기
            minNum = visited[x][y]
            answer.append([x, y])
        else:
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<N and 0<=ny<N:
                    if board[nx][ny]!=1 and visited[nx][ny]==0:
                        visited[nx][ny]=visited[x][y]+1
                        q.append((nx,ny))
    if answer:
        answer.sort()
        return visited[answer[0][0]][answer[0][1]], answer[0][0], answer[0][1]
    else:
        return -1, -1, -1


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

    d,px,py=find_person(taxi)
    if d==-1 or fuel-d<0:
        fuel=-1
        break

    fuel-=d

    idx=start.index([px,py])

    start[idx]=[-1,-1]

    #d2,ex,ey=find_des([px,py],end[idx])
    d2, py2, px2 = find_des([py, px], end[idx])  # 손님의 목적지로 가는 함수
    if [px2,py2] != end[idx] or fuel-d <0:
        fuel=-1
        break

    fuel+=d2
    taxi=[px2,py2]


print(fuel)
