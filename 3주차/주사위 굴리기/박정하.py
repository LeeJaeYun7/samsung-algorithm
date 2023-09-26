
n,m,x,y,k = map(int, input().split())
map_info = []
for _ in range(n):
    map_info.append(list(map(int, input().split())))
orders = list(map(int, input().split())) # 이동하는 명령 (동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4)

def move_dice(dir): 
    global x,y
    dx = [0,0,-1,1] # 동 서 북 남
    dy = [1,-1,0,0]
    nx = x + dx[dir-1] # 이동할 칸
    ny = y + dy[dir-1] 
    if 0 <= nx < n and 0 <= ny < m: # 지도 범위 내
        x, y = nx, ny # 주사위 위치 이동
        
        if dir == 1: # 동
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif dir == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif dir == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        
        if map_info[nx][ny]: # 이동한 칸에 쓰여 있는 수가 0이 아니면
            dice[5] = map_info[nx][ny] # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
            map_info[nx][ny] = 0 # 칸에 쓰여 있는 수는 0
        else: # 0이면 바닥면에 쓰여 있는 수가 칸에 복사
            map_info[nx][ny] = dice[5]  

        return True
    else:
        return False

dice = [0,0,0,0,0,0] # 처음에 주사위에는 모든 면에 0 
for order in orders:
    moved = move_dice(order)
    if moved:
        print(dice[0])
