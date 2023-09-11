r,c,k = map(int,input().split())
r -= 1
c -= 1

array = []
for _ in range(3):
    array.append(list(map(int,input().split())))

def mysort(array):
    maxlen = 0
    for i in range(len(array)): # 행 하나씩
        temp = list(set(array[i])) # 중복 제거
        new = []
        for j in temp: 
            if j != 0:
                new.append([j, array[i].count(j)])
        new = sorted(new, key= lambda x:(x[1],x[0]))
        array[i] = []
        for val,cnt in new:
            array[i].append(val)
            array[i].append(cnt)
        maxlen = max(maxlen, len(array[i])) # 제일 긴 행 길이 갱신

    for i in range(len(array)): 
        while len(array[i]) < maxlen:
            array[i].append(0)

time = 0
while time <= 100:
    nrows = len(array)
    ncols = len(array[0])

    if 0<=r<nrows and 0<=c<ncols and array[r][c] == k:
        print(time)
        break

    if nrows >= ncols:
        mysort(array)
    else:
        array = list(map(list, zip(*array)))    
        mysort(array)
        array = list(map(list, zip(*array)))    
    time += 1
    
if time == 101:
    print(-1)
