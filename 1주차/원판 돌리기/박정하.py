N,M,T = map(int, input().split())

array =[] 
for _ in range(N): # 원판에 적힌 수
    array.append(list(map(int, input().split())))

array.append([0]*M) # N+1 개의 행 

rotations = []    
for i in range(T): # 회전 정보 
    rotations.append(list(map(int, input().split())))

# x번째 원판을 d 방향으로 k칸 만큼 회전시키는 함수
def rotate(x, d, k):
    if d == 0: # 시계 방향
        for _ in range(k): # k칸
            array[x].insert(0, array[x].pop()) # 맨 마지막 값을 빼서 맨 앞에 삽입

    elif d == 1: # # 반시계 방향
        for _ in range(k): 
            array[x].append(array[x].pop(0)) # 맨 앞에 값을 빼서 맨 뒤에 삽입



# 인접하면서 같은 수 찾아서 삭제해주는 함수 (or 없다면 평균 구해서 +-1)
def removeAdj():
    global array
    temp = [[0 for _ in range(M)] for _ in range(N+1)]

    exist = False # 전체에서 인접하면서 같은 수가 존재하는지 체크

    for i in range(N):
        for j in range(M):
            if array[i][j] == 0: continue # 이미 삭제된 수라면 pass

            isSame = False # 현재 칸과 인접하면서 같은 수가 있는지
            if array[i][j] == array[i+1][j] or array[i][j] == array[i-1][j]:
                isSame = True
                exist = True
            if array[i][j] == array[i][(j+1)%M] or array[i][j] == array[i][j-1]:      
                isSame = True
                exist = True

            if not isSame: # 현재 칸과 같은 값이 없다면
                temp[i][j] = array[i][j] # 값 복사
            # 같은 값이 있다면 0으로 남겨둠
    
    if exist: # 삭제된게 있는 경우에는 temp 그대로 복사
        array = temp

    else: # 전체에서 인접하면서 같은 수가 하나도 없으면
        # 평균 구하기
        sumVal = 0
        cnt = 0

        for i in range(N):
            for j in range(M):
                if array[i][j]: # 0 이 아니면
                    sumVal += array[i][j]
                    cnt += 1

        avg = sumVal / cnt # 평균
        print("SUM" ,sumVal, "CNT", cnt)

        for i in range(N): 
            for j in range(M):
                if not array[i][j]: continue
                if array[i][j] > avg: # 평균보다 크면 -1
                    array[i][j] -= 1
                elif array[i][j] < avg: # 평균보다 작으면 +1
                    array[i][j] += 1


for i in range(T): # T번 회전
    x, d, k = rotations[i]
    for xx in range(x-1 , N, x): # x의 배수 원판에 대해
        rotate(xx, d, k) # 회전 수행
    
    removeAdj()

ans = 0
for i in range(N):
    ans += sum(array[i])

print(ans)
