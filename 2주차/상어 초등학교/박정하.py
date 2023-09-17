n = int(input())
seat = [[0] * n for _ in range(n)]
student = {}
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n*n):
    likes = list(map(int, input().split()))
    student[likes[0]] = likes[1:]
    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1
  
    for j in range(n):
        for k in range(n):
            if seat[j][k] == 0:
                empty = 0
                like = 0
                for l in range(4):
                    nx = j + dx[l]
                    ny = k + dy[l]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] == 0:
                            empty += 1
                        if seat[nx][ny] in likes[1:]:
                            like += 1

                if like > max_like or (max_like == like and max_empty < empty):
                    max_x = j
                    max_y = k
                    max_like = like
                    max_empty = empty

    seat[max_x][max_y] = likes[0]

# 만족도 구하기
ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        people = seat[i][j]
        like_list = student[people]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if seat[nx][ny] in like_list:
                    cnt +=1

        if cnt ==0 :
            ans += 0
        elif cnt == 1:
            ans += 1
        elif cnt ==2 :
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
print(ans)
