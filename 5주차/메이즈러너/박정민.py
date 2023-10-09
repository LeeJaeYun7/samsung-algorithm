# import copy
# from collections import deque

# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# cnt=0
# def move_people():
#     global cnt

#     for p in range(len(people)):

#         x=people[p][0]
#         y=people[p][1]
#         if x!=-5 and y!=-5:

#             # 행 다르면 행 이동

#             if ex!=x:
#                 nx,ny=x,y

#                 if ex>nx:
#                     nx+=1
#                 else:
#                     nx-=1

#                 if board[nx][ny]==0:
#                     people[p][0]=nx
#                     people[p][1]=ny
#                     cnt+=1
#                     continue
#             if ey != y:
#                 nx, ny = x, y

#                 if ey > ny:
#                     ny += 1
#                 else:
#                     ny -= 1

#                 if board[nx][ny] == 0:
#                     people[p][0] = nx
#                     people[p][1] = ny
#                     cnt+=1
#                     continue


#             #print(x,y)
#             # if x != -1 and y!=-1:



#                 # visieted=[[False]*N for _ in range(N)]
#                 # q=deque()
#                 # q.append((x,y,[]))
#                 # visieted[x][y]=True
#                 #
#                 # ans=[]
#                 # while q:
#                 #
#                 #     x,y,lst=q.popleft()
#                 #
#                 #     if x==ex and y==ey:
#                 #         #print(lst)
#                 #         ans.append(lst[0])
#                 #         break
#                 #     for i in range(4):
#                 #         nx=x+dx[i]
#                 #         ny=y+dy[i]
#                 #
#                 #         if 0<=nx<N and 0<=ny<N:
#                 #             if visieted[nx][ny]==False:
#                 #                 q.append((nx,ny,lst+[[nx,ny]]))
#                 #                 visieted[nx][ny]=True
#                 # ax,ay=ans[0][0],ans[0][1]
#                 #
#                 # if board[ax][ay]==0:
#                 #     people[p][0]=ax
#                 #     people[p][1]=ay

# def check_people(x1,x2,y1,y2):

#     ans=[]
#     for i in range(x1,x2+1):
#         for j in range(y1,y2+1):
#             if [i,j] in people:
#                 ans.append([i,j])

#     return ans



# def maze_rotate():
#     global people
#     global ex,ey

#     for idx in range(2,N+1):

#         for x1 in range(0,N-idx+1):
#             for y1 in range(0,N-idx+1):

#                 x2=x1+idx-1
#                 y2=y1+idx-1
#                 #print((x1,y1),(x2,y2))
#                 if x1<=ex<=x2 and y1<=ey<=y2:
#                     peoples=check_people(x1,x2,y1,y2)
#                     #print((x1,y1),(x2,y2))
#                     if len(peoples)>=1:
#                         #print(peoples)
#                         # 사람 넣기 -2  로
#                         temp_board=copy.deepcopy(board)
#                         for i in range(N):
#                             for j in range(N):
#                                 if [i,j] in peoples:
#                                     temp_board[i][j]=-2

#                         # 출구는 -3으로
#                         temp_board[ex][ey]=-3
#                         new_board=[]
#                         for i in range(x1,x2+1):
#                             t=[]
#                             for j in range(y1,y2+1):
#                                t.append(temp_board[i][j])
#                             new_board.append(t)

#                         rotate_board=copy.deepcopy(new_board)


#                         # rotate
#                         for i in range(len(new_board)):
#                             for j in range(len(new_board)):

#                                 rotate_board[j][i]=new_board[len(new_board)-1-i][j]

#                         # 벽 -1 일씩 해줌

#                         for i in range(len(rotate_board)):
#                             for j in range(len(rotate_board)):
#                                 if rotate_board[i][j]>=1:
#                                     rotate_board[i][j]-=1


#                         # 따로 뺴서 회전해준거 다시 넣어주기

#                         for i in range(x1,x2+1):
#                             for j in range(y1,y2+1):

#                                 board[i][j]=rotate_board[i-x1][j-y1]


#                         mp=[]

#                         for i in range(N):
#                             for j in range(N):
#                                 if board[i][j]==-3:
#                                     ex=i
#                                     ey=j
#                                     board[i][j]=0
#                                 elif board[i][j]==-2:
#                                     mp.append([i,j])
#                                     board[i][j]=0


#                         new_people=[]

#                         for p in people:
#                             if p not in peoples:
#                                 new_people.append(p)
#                         people= new_people+mp

#                         return
















# N,M,K=map(int,input().split())

# board=[list(map(int,input().split())) for _ in range(N)]

# people=[]

# for i in range(M):
#     x,y,=map(int,input().split())
#     people.append([x-1,y-1])

# ex,ey=map(int,input().split())
# ex-=1
# ey-=1
# time=0


# for tttime in range(K):

#     #print(tttime)
#     move_people()
#     # 사람들 움직이고
#    #


#     for i in range(len(people)):
#         x=people[i][0]
#         y=people[i][1]

#         if x==ex and y==ey:
#             x=-5
#             y=-5

#             people[i][0]=x
#             people[i][1]=y

#     flag=True

#     for x,y in people:
#         if x!=-5 and y!=-5:


#             flag=False

#     if flag:

#         break
# #
#     maze_rotate()
# #
# #



# print(cnt)
# print(ex + 1, ey + 1)
