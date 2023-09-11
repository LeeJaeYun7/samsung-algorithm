from collections import Counter

r,c,k=map(int,input().split())
r=r-1
c=c-1

matrix=[]
for _ in range(3):
    matrix.append(list(map(int,input().split())))

time=0


def cal(matrixs):
    global matrix
    new_matrix = []

    for i in range(len(matrix)):
        new=[]
        x=Counter(matrix[i])
        del x[0]
        x=list(x.items())
        x.sort(key=lambda x:(x[1],x[0]))
        if len(x)>50:
            x=x[:50]
        for a,b in x:
            new.append(a)
            new.append(b)
        new_matrix.append(new)

    maxNum=-1
    for i in range(len(matrix)):
        maxNum=max(maxNum,len(matrix[i]))

    for i in range(len(matrix)):
        if len(matrix[i])<maxNum:

            for j in range(maxNum-len(matrix[i])):
                matrix[i].append(0)

    matrix=new_matrix



while True:

    if r < len(matrix) and c < len(matrix[0]):
        if matrix[r][c] == k:
            print(time)
            break
    if len(matrix) >= len(matrix[0]):
        cal(matrix)
    else:
        matrix = list(map(list, zip(*matrix)))
        cal(matrix)
        matrix = list(map(list, zip(*matrix)))
    time += 1

    # for i in matrix:
    #     print(i)
    # print()
    if time > 100:
        print(-1)
        break
    if r < len(matrix) and c < len(matrix[0]):
        if matrix[r][c] == k:
            print(time)
            break
