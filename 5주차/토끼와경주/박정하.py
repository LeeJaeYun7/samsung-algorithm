'''
시간 복잡도 통과
Point1. 우선순위 큐 사용
Point2. i번 토끼를 제외한 나머지 토끼들 전부 점수 더해주는 것 -> i번 토끼의 점수를 빼준다
Point3. 상하좌우 네 방향으로 각각 d만큼 이동할 때, 한칸씩 가면서 확인하면 시간초과. d만큼 한번에 가서 outOfRange 함수로 인덱스 고쳐준다.
'''
import heapq

Q = int(input())

info = list(map(int,input().split()))[1:]
N,M,P = info[0], info[1], info[2]

rabbitHeap = []
scores = {}
distance = {}

minus_score = 0

for i in range(3, len(info), 2):
    heapq.heappush(rabbitHeap, [0,0,0,0,info[i]]) # 총 점프횟수, 행+열, 행, 열, 고유번호
    scores[info[i]] = 0
    distance[info[i]] = info[i+1]

orders = []
for _ in range(Q-1):
    orders.append(list(map(int,input().split())))

def isValid(nx,ny):
    return 0<=nx<N and 0<=ny<M

def outOfRange(nx, ny):
    nx %= 2*(N-1)
    ny %= 2*(M-1)
    return min(nx, 2*(N-1)-nx), min(ny, 2*(M-1)-ny)
    
def getLocation(x,y,d): 
    dx = [-1,0,1,0] # 상 좌 하 우
    dy = [0,-1,0,1] # 0이면 2, 1이면 3, 2이면 0, 3이면 1 
    candidates = []

    for i in range(4): # 상 하 좌 우 네방향으로 각각 d만큼 이동했을때의 위치
        nx = x + dx[i]*d
        ny = y + dy[i]*d

        if not isValid(nx, ny):
            nx, ny = outOfRange(nx, ny)
        
        candidates.append([nx, ny])        

    candidates.sort(key= lambda x: (x[0]+x[1], x[0], x[1]))
    return candidates[-1] # 우선순위가 가장 높은 칸 위치 [x,y] 반환

def getScore(pid, score):
    global minus_score
    minus_score += -(score + 2)
    scores[pid] += -(score + 2)

def run(K, S): # K번 반복, 점수 S
    pickedRabbit = []
    for _ in range(K):
        # 총 점프횟수, 행+열, 행, 열, 고유번호
        cnt, xy, x, y, pid = heapq.heappop(rabbitHeap) # 우선순위가 가장 높은 토끼의 위치 x,y와 이동거리 d, 고유번호 pid
        cnt += 1
        r, c = getLocation(x, y, distance[pid]) # 이동할 칸 위치

        getScore(pid, r+c) # pid 토끼 빼고 나머지 토끼 점수 얻음
        heapq.heappush(rabbitHeap, [cnt, r+c, r, c, pid])
        heapq.heappush(pickedRabbit, [-(r+c), -r, -c, -pid])

    d,um,my, pid = heapq.heappop(pickedRabbit)

    scores[-pid] += S
    return 

def changeD(pid, L):
    distance[pid] *= L
    return

def bestRabbit():
    score = -1
    for s in scores.values():
        score = max(score, s)
    return score - minus_score

for order in orders:
    if order[0] == 200: # 경주 진행
        run(order[1], order[2])

    elif order[0] == 300: # 이동 거리 정보 변경
        changeD(order[1], order[2]) # pid_t 토끼의 이동거리를 L 로 변경

    else:
        print(bestRabbit())
