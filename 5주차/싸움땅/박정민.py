EMPTY=0
N,M,K=map(int,input().split())

guns=[
    [[] for _ in range(N)] for _ in range(N)
]
for i in range(N):
    t=list(map(int,input().split()))
    for j in range(N):
        if t[j]!=0:
            guns[i][j].append(t[j])

players=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(M):

    x,y,d,s=map(int,input().split())
    players.append([i,x-1,y-1,d,s,0])

#
def in_range(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False


def get_next_pos(x,y,dir):


    nx=x+dx[dir]
    ny=y+dy[dir]

    if in_range(nx,ny):
        return nx,ny,dir
    else:
        nx=x+dx[(dir+2)%4]
        ny=y+dy[(dir+2)%4]

        return nx,ny,dir


def find_player(nx,ny):

    for i in range(len(players)):
        if players[i][1] == nx and players[i][2]==ny:
            return players[i]
    return EMPTY



def update(p):

    for i in range(len(players)):
        if players[i][0]==p[0]:
            players[i]=p
def move(player,pos):
    num,x,y,ndir,s,a=player
    nx,ny=pos

    guns[nx][ny].append(a)
    guns[nx][ny].sort(reverse=True)
    a=guns[nx][ny][0]
    guns[nx][ny].pop(0)

    p=[num,nx,ny,ndir,s,a]
    #print("p",p)
    update(p)


def loser_move(player):

    num,x,y,d,s,a=player

    guns[x][y].append(a)
    a=0
    new_x,new_y,new_d=0,0,0
    for i in range(4):
        nx=x+dx[(d+i)%4]
        ny=y+dy[(d+i)%4]

        if 0<=nx<N and 0<=ny<N and find_player(nx,ny)==EMPTY:
            new_x=nx
            new_y=ny
            new_d=(d+i)%4
            break
    p=[num,new_x,new_y,new_d,s,a]
    move(p,(new_x,new_y))




print(players)
print()
def duel(current,next,pos):

    player1=current
    player2=next
    print(player1)
    print(player2)
    p1_stat=player1[4]+player1[5]
    p2_stat=player2[4]+player2[5]
    print(p1_stat,p2_stat)
    if (p1_stat,player1[4]) > (p2_stat,player2[4]):
        score[player1[0]]+=(p1_stat-p2_stat)

        loser_move(player2)

        move(player1,pos)
    else:
        score[player2[0]]+=(p2_stat-p1_stat)

        loser_move(player1)

        move(player2,pos)


score=[0] * M

for kk in range(K):

    print(kk,"라운드")

    for i in range(M):

        num,x,y,dir,s,a=players[i]


        nx,ny,ndir=get_next_pos1(x,y,dir)

        next_player=find_player1(nx,ny)
        #print(next_player)
        current_player=[num,nx,ny,ndir,s,a]
        update(current_player)

        if next_player==EMPTY:
            #print(kk,players[i][0])
            move(current_player,(nx,ny))
            #print("next",players)

        else:
            duel(current_player,next_player,(nx,ny))
        print("num x y d s a")
        print(players)
        print(score)
        for i in guns:
            print(i)
        print()

print(score)

