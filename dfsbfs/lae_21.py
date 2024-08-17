import sys
from collections import deque

if sys.platform == "win32":
    sys.stdin = open('lae_21.txt')

input = sys.stdin.readline

R, C = map(int, input().split())
mat = [[0]*C for _ in range(R)]
visited = [[0]*C for _ in range(R)]
answer = -1
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def initVisited():
    for i in range(R):
        for j in range(C):
            visited[i][j] = 0

def setMat():
    for i in range(R):
        line = input()
        for j in range(C):
            if line[j] == "L":
                mat[i][j] = 1

def bfs(row, col):
    maxDist = -1
    if mat[row][col] == 1:
        visited[row][col] = 1
        que = deque([(row, col, 0)])

        while (que):
            r, c, dist = que.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if (nr < 0 or nr > R-1 or nc < 0 or nc > C-1):
                    continue
                elif mat[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    que.append((nr, nc, dist+1))
                    maxDist = max(maxDist, dist+1)
    return maxDist

setMat()
for i in range(R):
    for j in range(C):
        initVisited()
        answer = max(answer, bfs(i,j))

print(answer)