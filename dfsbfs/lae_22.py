import sys
from collections import deque

if sys.platform == 'win32':
    sys.stdin = open('lae_22.txt')

input = sys.stdin.readline

C, R = map(int, input().split())
mat = [[0] * (C) for _ in range(R)]
visited = [[0] * (C) for _ in range(R)]
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]
loc = []

def setMat():
    for i in range(R):
        line = list(map(int, input().split()))
        for v in range(len(line)):
            mat[i][v] = line[v]
            if line[v] == 1:
                loc.append((i, v))

def bfs():
    maxDist = 0
    que = deque([])
    for i in range(len(loc)):
        r, c = loc[i]
        visited[r][c] = 1
        que.append((r,c,0))

    while(que):
        r, c, dist = que.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if(nr < 0 or nr > R-1 or nc < 0 or nc > C-1):
                continue
            elif mat[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                mat[nr][nc] = 1
                que.append((nr, nc, dist+1))
                maxDist = max(maxDist, dist+1)
    return maxDist

def findAnswer():
    answer = bfs()
    if answer != 0:
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    return -1
    return answer

setMat()
print(findAnswer())