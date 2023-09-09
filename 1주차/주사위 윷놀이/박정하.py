horse = [0,0,0,0]
dices = list(map(int, input().split()))
ans = 0

# 모든 원에 대해서 index 지정. [점수, 다음 index] 저장
index = [[0,1],[2,2],[4,3],[6,4],[8,5],         [10,6],[12,7],[14,8],[16,9],[18,10],
 [20,11],[22,12],[24,13],[26,14],[28,15],   [30,16],[32,17],[34,18],[36,19],[38,20],
 [40,32],[13,22],[16,23],[19,24],[25,30],   [22,26],[24,24],[28,28],[27,29],[26,24],
 [30,31],[35,20],[0,32]]

# 파란색 칸 정보는 따로 저장.
blue_index = {}
blue_index[5]=[10, 21]
blue_index[10]=[20, 25]
blue_index[15]=[30, 27]

def dfs(turn, score):
    global ans
    ans = max(ans, score)
    if turn == 10:
        return

    for i in range(4):
        # 주사위 만큼 이동
        before_idx = horse[i]
        # 파란색 칸에서 이동을 시작하면 파란색 화살표를 타야 함.
        next_idx = blue_index[before_idx][1] if before_idx in blue_index else before_idx
        cycle = dices[turn] - 1 if before_idx in blue_index else dices[turn]
      
        for _ in range(cycle):
            next_idx = index[next_idx][1]

        if next_idx != 32 and horse.count(next_idx) >= 1:
            continue
          
        horse[i] = next_idx
        dfs(turn+1, score + index[next_idx][0])
        horse[i] = before_idx

dfs(0,0)
print(ans)
