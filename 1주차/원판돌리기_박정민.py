
N ,M , T =map(int ,input().split())

circle =[]
for i in range(N):
    temp =list(map(int ,input().split()))
    circle.append(temp)

for test in range(T):

    x ,d , k =map(int ,input().split())

    # rotate
    for i in range(1 , N +1):

        if i% x == 0:

            if d == 0:  # 시계방향

                temp = circle[i - 1]

                for j in range(k):
                    last = temp[-1]

                    for y in range(M - 2, -1, -1):
                        temp[y + 1] = temp[y]

                    temp[0] = last
            elif d == 1:  # 반시계방향
                temp = circle[i - 1]

                for j in range(k):
                    first = temp[0]

                    for y in range(1, M):
                        temp[y - 1] = temp[y]

                    temp[-1] = first


    # 인접한 수 제거 부분

    check = 0
    delete_lst = []
    for i in range(N):
        for j in range(M):
            current = circle[i][j]
            if current != 'x':

                right = (j + 1) % M
                left = (j - 1) % M
                if current == circle[i][right]:
                    delete_lst.append([i, right])
                if current == circle[i][left]:
                    delete_lst.append([i, left])
                up = i + 1
                down = i - 1

                if i == 0:
                    if current == circle[up][j]:
                        delete_lst.append([up, j])
                elif i == N - 1:
                    if current == circle[down][j]:
                        delete_lst.append([down, j])
                else:
                    if current == circle[up][j]:
                        delete_lst.append([up, j])
                    if current == circle[down][j]:
                        delete_lst.append([down, j])

    if len(delete_lst) >= 1:
        check += 1


        for a, b in delete_lst:
            circle[a][b] = 'x'


    # 인접한게 0 일때

    if check == 0:
        sum = 0

        c = 0
        for i in range(N):
            for j in range(M):
                if circle[i][j] != 'x':
                    c += 1
                    sum += circle[i][j]
        if c!=0:
            avg = sum / c


        for i in range(N):
            for j in range(M):
                if circle[i][j] != 'x':
                    if circle[i][j] > avg:
                        circle[i][j] -= 1
                    elif circle[i][j] < avg:
                        circle[i][j] += 1


answer = 0
for i in range(N):
    for j in range(M):
        if circle[i][j] != 'x':
            answer += circle[i][j]
print(answer)

