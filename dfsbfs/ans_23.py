import sys
from collections import deque

# if sys.platform == 'win32':                 # window 환경에서만 작동
sys.stdin = open('./dfsbfs/23.txt')              # input data를 text 파일에서 읽어오기

input = sys.stdin.readline                  # 데이터 입력 속도 향상

M, N = map(int, input().split())
K = int(input())
BUS = []

q = deque()
visited = [False] * (K + 1)

# (sx1, sy1, dx1, dy1)와 (sx2, sy2, dx2, dy2)가 서로 겹치면 True 반환
def checkBus(sx1, sy1, dx1, dy1, sx2, sy2, dx2, dy2):
    return sx1 <= dx2 and sx2 <= dx1 and sy1 <= dy2 and sy2 <= dy1

def push(bus, cnt):
    if visited[bus[0]]: return False                    # 이미 탑승 했던 버스인 경우
    visited[bus[0]] = True
    q.append((bus, cnt))
    return checkBus(bus[1], bus[2], bus[3], bus[4], Dx, Dy, Dx, Dy)

def bfs():
    # 시작 위치에서 탑승 가능한 버스들 큐에 삽입
    for busInfo in BUS:
        _, x1, y1, x2, y2 = busInfo
        # 버스 경로가 시작 위치와 겹치는 경우
        if checkBus(x1, y1, x2, y2, Sx, Sy, Sx, Sy):
            if push(busInfo, 1): return 1
    
    while q:
        bus, cnt = q.popleft()
        for nextBus in BUS:                 # 인접행렬
            _, x1, y1, x2, y2 = nextBus
            # 환승 가능 여부 확인 및 도착지 도달 여부 확인
            if checkBus(x1, y1, x2, y2, bus[1], bus[2], bus[3], bus[4]):
                # 도착지에 갈 수 있다면 환승 횟수 반환
                if push(nextBus, cnt + 1): return cnt + 1
    
    return -1

for _ in range(K):
    b, x1, y1, x2, y2 = map(int, input().split())
    # x1 보다 x2가 더 큰 값으로, y1 보다 y2가 더 큰 값으로 세팅
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    BUS.append((b, x1, y1, x2, y2))

Sx, Sy, Dx, Dy = map(int, input().split())

print(bfs())