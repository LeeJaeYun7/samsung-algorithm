from copy import deepcopy

def stackBowl1(fishes, N):
    # 처음 회전 부분
    bowl = fishes[:]
    rot = [[bowl[0]], [bowl[1]]]

    # 앞에서 부터 h 만큼 잘라내기
    bowl = bowl[2:]

    # 첫번째 회전 이후
    while True:
        h = len(rot) # 높이
        w = len(rot[0]) # 밑변
        # 남은 길이 - 높이 >= 0
        if len(bowl) - h >= 0:
            # 회전 == 떼어내서 회전 >
            # 회전 배열 배열 > 밑변 높이 바뀜
            temp = [[0] * h for _ in range(w)]
            for i in range(0, w):
                for j in range(h):
                    temp[i][j] = rot[h - 1 - j][i]
            # 밑에 넣기
            rot = temp + [bowl[:h]]
            # 앞에서 부터 h 만큼 잘라내기
            bowl = bowl[h:]
        else:
            rot[-1] = rot[-1] + bowl
            break

    # 사각 행렬 만들게 -1 붙임 # 불가능한 곳
    for i in range(len(rot)-1):
        rot[i].extend([-1] * (len(rot[-1])-len(rot[i])))

    r = len(rot)
    c = len(rot[-1])
    temp = deepcopy(rot)
    for x in range(r):
        for y in range(c):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<r and 0<=ny<c and rot[nx][ny] != -1:
                    d = (rot[x][y] - rot[nx][ny])// 5
                    if d > 0:
                        if rot[x][y] < rot[nx][ny]:
                            temp[x][y] += d
                            temp[nx][ny] -= d
                        else:
                            temp[nx][ny] += d
                            temp[x][y] -= d
    rot = temp

    # 한 줄로 만들기
    cnt = 0
    bowl = []
    for j in range(c):
        for i in range(r-1, -1, -1):
           #값을 변경했을 때만
           if rot[i][j] != -1:
                bowl.append(rot[i][j])

    fishes = bowl[:]
    return fishes

def stackBowl2(fishes, N):
    left = list(reversed(fishes[:(N//2)]))
    right = fishes[N//2:]
    stackbowl = [left] + [right]

    left = [[0]*(N//4) for _ in range(2)]
    right = [[0]*(N//4) for _ in range(2)]
    for i in range(2):
        for j in range(N//2):
            if j < N//4:
                left[i][j] = stackbowl[i][j]
            else:
                right[i][j-(N//4)] = stackbowl[i][j]
    # left만 180도 회전
    left = list(reversed(left))
    leftup = list(reversed(left[0]))
    leftdown = list(reversed(left[1]))
    left =  [leftup] + [leftdown]
    stackbowl = left + right

    r = 4
    c = N//4
    temp = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                d = (stackbowl[x][y] - stackbowl[nx][ny])// 5
                if d > 0:
                    if stackbowl[x][y] < stackbowl[nx][ny]:
                        temp[x][y] += d
                        temp[nx][ny] -= d
                    elif stackbowl[nx][ny] < stackbowl[x][y]:
                        temp[nx][ny] += d
                        temp[x][y] -= d

    for x in range(r):
        for y in range(c):
            stackbowl[x][y]+= temp[x][y]
    bowl = []
    for c in range(N//4):
        for r in range(3, -1, -1):
            bowl.append(stackbowl[r][c])
    fishes = bowl[:]
    return fishes

def fillFish(fishes, N):
    # 물고기 수 가장 적은 어항에 물고기 한마리 넣음
    # if 여러개 >
    #  모두 1마리 넣음
    minCnt = min(fishes)
    for i in range(N):
        if fishes[i] == minCnt:
            fishes[i] += 1
    return fishes

def solve(fishes, N):
    fishes = fillFish(fishes, N)
    fishes = stackBowl1(fishes, N)
    fishes = stackBowl2(fishes, N)
    return fishes

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, K = map(int, input().split())
fishes = list(map(int, input().split()))
op = 0
while max(fishes) - min(fishes) > K:
    op += 1
    fishes = solve(fishes, N)
print(op)
