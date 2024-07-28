import sys
from collections import deque

if sys.platform == "win32":
    sys.stdin = open("input.txt")

input = sys.stdin.readline

R, C = map(int, input().split())
KR, KC, PR, PC = map(int, input().split())

visited = [[0]*(C+1) for _ in range(R+1)]

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

visit = -1

def bfsQue():
    que = deque([(KR, KC, 0)])
    visited[KR][KC] = 1

    while(que):
        r, c, dist = que.popleft()
        if r == PR and c == PC:
            return dist
        for i in range(8):
            nr = r+dr[i]
            nc = c+dc[i]
            if nr < 1 or nr > R or nc < 1 or nc > C:
                continue
            else:
                if visited[nr][nc] == 1:
                    continue
                else:
                    que.append((nr,nc,dist+1))
                    visited[nr][nc] = 1
    return -1

# print(bfsQue())

def bfsMat():
    que = deque([(KR, KC)])
    visited[KR][KC] = 0

    while(que):
        r, c = que.popleft()
        if r == PR and c == PC:
            return visited[r][c]
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 1 or nr > R or nc < 1 or nc > C:
                continue
            if visited[nr][nc] == -1:
                que.append((nr,nc))
                visited[nr][nc] = visited[r][c]+1
    return -1

visited = [[visit]*(C+1) for _ in range(R+1)]
print(bfsMat())