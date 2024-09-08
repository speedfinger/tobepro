"""
https://www.codepass.co.kr/bbs/bbs_solve_lecture.php?idx=390&prod_idx=3539&pCode=lecture&seq=20&page=1
장기2
"""

import sys
from collections import deque
sys.stdin = open('./jnm_20.txt','r')


R, C = map(int,input().split())
kr,kc,pr,pc =map(int,input().split())
# print(f"{R}/ {C}")
# print(f"{kr},{kc} / {pr},{pc}")

dx = [ 1, 2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2, 2, 1,-1,-2]

def show_map(maps):
    for i in range(0,len(maps)):
        print(maps[i])

maps=[]
for i in range(0,(R)):
    maps.append([0]*C)

# show_map(maps)


def bfs(x,y,pr,pc):
    que = deque()
    que.append((x,y))

    while que:
        x,y=que.popleft()

        for i in range(0,8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx<0 or ny<0 or nx>=R or ny>=C):
                continue

            if maps[nx][ny]==0:
                maps[nx][ny]=maps[x][y]+1
                que.append((nx,ny))
            if nx == pr and ny == pc:
                return maps[x][y]+1
    return maps[pr][pc]

bfs(kr-1,kc-1,pr-1,pc-1)
print(maps[pr-1][pc-1])
