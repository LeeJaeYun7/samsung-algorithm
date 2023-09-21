dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1] # 1부터

board = []
fishes = {}
ans = 0

for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0,8,2):  
        fishes[row[j]] = [i,j//2,row[j+1]-1] # fishes[번호] = [x좌표, y좌표, 방향]
    board.append([row[i] for i in range(8) if i%2==0])

def moveFish(currX, currY, currDir):
    for fish in sorted(fishes): # 물고기 번호순
        fishX, fishY, fishDir = fishes[fish]

        for i in range(8): # 방향 이동하며 될때까지
            nx = fishX + dx[(fishDir)%8] 
            ny = fishY + dy[(fishDir)%8] 
            if nx<0 or nx>=4 or ny<0 or ny>=4 or (nx == currX and ny == currY):
                fishDir += 1
                continue
                
            else: 
                old = board[nx][ny] # 이동할 칸의 물고기 번호
                board[nx][ny] = board[fishX][fishY] # 현재 물고기 한칸 이동
                fishes[fish][0], fishes[fish][1] = nx,ny # 현재 물고기 정보 업데이트
                if old: # 그 칸에 물고기가 있으면 값 바꿔주기
                    board[fishX][fishY] = old
                    fishes[old][0], fishes[old][1] = fishX, fishY
                else: # 빈칸이면 현재 칸 비워줌
                    board[fishX][fishY] = 0 
                break # 한칸 이동후 중단
        fishes[fish][2] = fishDir%8
        print("이동완료")
        print(fishes)

def moveShark(currX, currY, currDir):
    cand = []
    for _ in range(3):
        nx = currX + dx[currDir]
        ny = currY + dy[currDir]
        if 0<=nx<4 and 0<=ny<4 and board[nx][ny]:
            cand.append((nx,ny))
    return cand


def dfs(x,y,eat,board):
    eat += board[x][y]
    currX, currY, currDir = x, y, fishes[board[x][y]][2]
    board[x][y] = -1

    moveFish(currX, currY, currDir)
    cand = moveShark(currX, currY, currDir)
    if cand:
        for nx,ny in cand:
            dfs(nx,ny,eat,board)
    else:
        ans = max(ans,eat)
        return 

dfs(0,0,0,board)
print(ans)
