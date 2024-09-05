import sys
from collections import deque

# if sys.platform == 'win32':                 # window 환경에서만 작동
sys.stdin = open('./dfsbfs/jnm_24.txt')              # input data를 text 파일에서 읽어오기

input = sys.stdin.readline                  # 데이터 입력 속도 향상

M, N = map(int, input().split())                                # 공장의 세로, 가로 크기
F = [list(map(int, input().split())) for _ in range(M)]         # 공장 정보

SR, SC, SD = map(int, input().split())                          # 로봇의 시작 위치와 방향
ER, EC, ED = map(int, input().split())                          # 로봇의 목표 위치와 방향
SR -= 1; SC -= 1; ER -= 1; EC -= 1                              # 공장은 (0 ~ M - 1, 0 ~ N - 1) 사용

# 제자리, 동, 서, 남, 북
DR = [0, 0, 0, 1, -1]
DC = [0, 1, -1, 0, 0]

visited = [[[0] * 5 for _ in range(N)] for _ in range(M)]       # 방문 여부 [세로][가로][방향]

que = deque()

def push(r, c, d, cnt):
    if visited[r][c][d]: return False                           # 방문 여부 확인
    if (r, c, d) == (ER, EC, ED): return True                   # 목표 지점과 방향에 도달한 경우
    visited[r][c][d] = 1
    que.append((r, c, d, cnt))                                  # (행, 열, 방향, 명령 횟수)
    return False

def bfs():
    # 시작 상태 세팅
    if push(SR, SC, SD, 0): return 0
    
    while que:
        r, c, d, cnt = que.popleft()
        
        # 전진
        for k in range(1, 4):
            nr, nc = r + DR[d] * k, c + DC[d] * k
            if nr < 0 or nr >= M or nc < 0 or nc >= N: break    # 공장 벗어나면 진행 불가
            if F[nr][nc]: break                                 # 궤도가 없으면 진행 불가
            if push(nr, nc, d, cnt + 1): return cnt + 1

        # 회전
        if d in (1, 2):                                     # 방향이 (동, 서)인 경우
            if push(r, c, 3, cnt + 1): return cnt + 1
            if push(r, c, 4, cnt + 1): return cnt + 1
        else:                                               # 방향이 (남, 북)인 경우
            if push(r, c, 1, cnt + 1): return cnt + 1
            if push(r, c, 2, cnt + 1): return cnt + 1
    return -1

print(bfs())