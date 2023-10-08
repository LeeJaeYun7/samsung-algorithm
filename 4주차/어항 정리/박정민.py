# 어항 n개
import copy
from collections import deque


# 1. 물고기의 수가 가장 적은 어항에 물고기 한마리 넣음
# (여러개면 다 한마리씩 넣음)
# 2. 어항 쌓음 ( 가장 왼쪽에있는걸 오른쪽 위에다가)
# 3.
def rotate():

    while True:

        idx=-1

        temp_list=[]
        for i in range(N-1,-1,-1):
            temp=[]
            for j in range(N):
                if board[j][i]!=0:
                    temp.append(board[j][i])
            if len(temp)>1:
                temp.reverse()
                temp_list.append(temp)
                idx=max(idx,i)
        #print(temp_list,idx)

        #print("비교",len(temp_list[0]),N-1-idx)
        if len(temp_list[0])>N-1-idx:
            flag=True
            #print("종료")
            break
        for i in range(len(temp_list)):
            l=temp_list[i]
            #print("l=",i,l)
            for j in range(len(l)):

                board[N-2-i][idx+1+j]=l[j]

        for i in range(N):
            for j in range(0,idx+1):
                board[i][j]=0

        # for ia in board:
        #     print(ia)
        # print()

N,K=map(int,input().split())

bowl=list(map(int,input().split()))

board=[[0]*N for _ in range(N-1)]
board.append(bowl)

def cal():

    new_board=copy.deepcopy(board)

    #print("new_board")
    #for i in new_board:
    #    print(i)
    #print()
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]

    visted=[[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):


            if board[i][j]>=1:

                for d in range(4):

                    nx=i+dx[d]
                    ny=j+dy[d]

                    if 0<=nx<N and 0<=ny<N:
                        #print("@@@",nx,ny)
                        if board[nx][ny]!=0 and visted[nx][ny]!=True:
                            #print(board[i][j],"일떄",board[nx][ny])
                            sum=abs(board[nx][ny]-board[i][j])
                            #print("차",sum)

                            if sum//5>=1:

                                fish=sum//5
                                #print(board[i][j],board[nx][ny])
                                #print("d",fish)
                                if board[nx][ny]>board[i][j]:
                                    new_board[i][j]+=fish
                                    new_board[nx][ny]-=fish
                                elif board[nx][ny]<board[i][j]:
                                    new_board[nx][ny] += fish
                                    new_board[i][j] -= fish
                                #print("new_board",new_board[i][j],new_board[nx][ny])
                visted[i][j]=True
    return new_board
def plus():
    minFish=min(board[-1])

    for i in range(N):
        if minFish==board[-1][i]:
            board[-1][i]+=1
def lineup():

    answer=[]
    for i in range(N):
        temp=[]
        for j in range(N):
            if board[j][i]!=0:
                #temp.reverse()
                temp.append(board[j][i])
        temp.reverse()
        answer.append(temp)
    #print(answer)

    line=[]
    for i in answer:

        for j in i:
            line.append(j)
    return line
def rotate2():

    # n//2 단계

    n=N//2
    answer=[]

    temp=lines[:n]
    temp.reverse()
    answer.append(temp)
    answer.append(lines[n:])
    #print(answer)

    n=n//2

    # 1 2 3 4 5 6
    aa=[]
    for i in range(2):
        t=[]
        for j in range(n):
            t.append(answer[i][j])
            #del answer[i][0]
        t.reverse()
        aa.append(t)

    #print("aa",aa)

    ans=[]
    for i in range(len(answer)):
        t=answer[i][n:]
        ans.append(t)
    #print(ans)

    aa.reverse()


    tt=aa+ans

    e=[]
    for i in aa:
        e.append(i)
    for i in ans:
        e.append(i)

    #print(e)
    ans_e=cal2(e)

    #print(ans_e)

    final_ans=[]

    for i in range(len(ans_e[0])):
        at=[]
        for j in range(len(ans_e)):
            at.append(ans_e[j][i])
        at.reverse()
        final_ans+=at
    return final_ans


def cal2(e):

    new_e = copy.deepcopy(e)


    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visted = [[False] * N for _ in range(N)]
    #print("@",len(e[0]),len(e))
    for i in range(len(e)):
        for j in range(len(e[0])):
            #print(i,j)
            if e[i][j] >= 1:

                for d in range(4):

                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0 <= nx < len(e) and 0 <= ny < len(e[0]):
                        # print("@@@",nx,ny)
                        if e[nx][ny] != 0 and visted[nx][ny] != True:
                            #print(e[i][j],"일떄",e[nx][ny])
                            sum = abs(e[nx][ny] - e[i][j])
                            #print("차",sum)

                            if sum // 5 >= 1:

                                fish = sum // 5
                                #print(board[i][j],board[nx][ny])
                                #print("d",fish)
                                if e[nx][ny] > e[i][j]:
                                    new_e[i][j] += fish
                                    new_e[nx][ny] -= fish
                                elif e[nx][ny] < e[i][j]:
                                    new_e[nx][ny] += fish
                                    new_e[i][j] -= fish
                                # print("new_board",new_board[i][j],new_board[nx][ny])
                visted[i][j] = True
    # for i in new_e:
    #     print(i)
    # print()
    return new_e





cnt=0
while True:
    # for i in board:
    #     print(i)
    # print()
    plus()

    board[N-2][1]=board[N-1][0]
    board[N-1][0]=0

    # for i in board:
    #     print(i)
    # print("@")

    rotate()
    board=cal()
    # for i in board:
    #     print(i)

    #print("line")

    lines=lineup()
    #print(lines)

    a=rotate2()
    cnt+=1

    if abs(min(a)-max(a))<=K:
        break

    board=[[0]*N for _ in range(N-1)]
    board.append(a)

    # for i in board:
    #     print(i)
    # print()

print(cnt)
