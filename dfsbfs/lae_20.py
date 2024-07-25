import sys
from collections import deque

if sys.platform == 'win32':
    sys.stdin = open('lae_20.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
SR, SC, ER, EC = map(int, input().split())

visited = [[0] * (M + 1) for _ in range(N + 1)]

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

INF = 987654321

def bfs1():
    que = deque([(SR, SC, 0)])
    visited[SR][SC] = 1

    while que:
        r, c, dist = que.popleft()

        if (r, c) == (ER, EC): return dist

        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 1 or nr > N or nc < 1 or nc > M: continue
            if visited[nr][nc]: continue
            que.append((nr, nc, dist + 1))
            visited[nr][nc] = 1

    return -1


def bfs2():
    que = deque([(SR, SC)])
    visited[SR][SC] = 0

    while que:
        r, c = que.popleft()

        if (r, c) == (ER, EC): return visited[r][c]

        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 1 or nr > N or nc < 1 or nc > M: continue
            if visited[nr][nc] <= visited[r][c] + 1: continue
            que.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1

    return -1

# print(bfs1())

visited = [[INF] * (M + 1) for _ in range(N + 1)]
print(bfs2())