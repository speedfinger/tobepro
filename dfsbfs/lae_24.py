import sys
from collections import deque

if sys.platform == "win32":
    sys.stdin = open('lae_24.txt')

input = sys.stdin.readline

R, C = map(int, input().split())
mat = [[0]*(C+1) for _ in range(R+1)]
visited = [[[0]*5 for _ in range(C+1)] for _ in range(R+1)]

# 0 4 0
# 2 0 1
# 0 3 0
dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]

for r in range(R):
    line = list(map(int, input().split()))
    for c in range(C):
        mat[r+1][c+1] = line[c]

sr, sc, sd = map(int, input().split())
er, ec, ed = map(int, input().split())

que = deque()

def push(r, c, d, cnt):
    pos = (r, c, d)
    if pos == (er, ec, ed):
        # print(f'pos: {pos}, cnt: {cnt}')
        return True
    elif visited[r][c][d] == 1:
        return False
    else:
        # print(f'pos: {pos}, cnt: {cnt}')
        visited[r][c][d] = 1
        que.append((pos, cnt))
        return False


def bfs(sr, sc, sd, er, ec, ed):
    if push(sr, sc, sd, 0):
        return 0
    else:
        while(que):
            pos, cnt = que.popleft()
            r, c, d = pos[0], pos[1], pos[2]
            for k in range(1,4):
                nr = r + dr[d]*k
                nc = c + dc[d]*k
                if (nr <= 0 or nr > R or nc <= 0 or nc > C):
                    break
                elif mat[nr][nc] == 1:
                    break
                elif mat[nr][nc] == 0:
                    if push(nr, nc, d, cnt+1):
                        return cnt+1
            if d == 1 or d == 2:
                if push(r, c, 3, cnt+1):
                    return cnt+1
                elif push(r, c, 4, cnt+1):
                    return cnt+1
            elif d == 3 or d == 4:
                if push(r, c, 1, cnt+1):
                    return cnt+1
                elif push(r, c, 2, cnt+1):
                    return cnt+1
    return -1

# for i in range(R+1):
#     for j in range(C+1):
#         print(mat[i][j], end = ' ')
#     print()

print(bfs(sr,sc,sd,er,ec,ed))