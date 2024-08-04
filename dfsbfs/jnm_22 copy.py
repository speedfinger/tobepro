
"""
토마토(고)
https://codepass.co.kr/contest/390/problem/22?cursor=eyJwcm9ibGVtc2V0IjoiY18zOTAiLCJmaWVsZCI6MCwiaWR4IjoyMX0=

1. 0 인 애들을 que에 넣는다?
2. 1인 애들을 bfs 시작
3. 0인애들 1로 변경
4. que가 빌때까지 반복

0 0 0 0 0 0 
0 1 0 0 0 0 
0 0 0 0 0 0 
0 0 0 0 0 1


0 1 0 0 0 0 
1 1 1 0 0 0 
0 1 0 0 0 1 
0 0 0 0 1 1


1 1 1 0 0 0 
1 1 1 1 0 1 
1 1 1 0 1 1 
0 1 0 1 1 1

1 1 1 1 0 1 
1 1 1 1 1 1 
1 1 1 1 1 1 
1 1 1 1 1 1
"""
import sys
from collections import deque
if sys.platform=="linux":
    sys.stdin = open("./dfsbfs/jnm_22.txt")

# sys.stdin = open("./dfsbfs/jnm_22.txt",'r')


def show_maps(maps):
    for i in range(0,len(maps)):
        print(maps[i])
    print("@@@@@@@@@@@@@@@@")


M,N = map(int, input().split())

# print(f"{N} {M}")
# print(sys.platform)

maps =[]

que = deque()
for r in range(0,N):
    row = list(map(int,input().split()))
    maps.append(row)
    for c in range(0, M):
        if row[c] ==1:
            # print(f"{r} / {c}")
            que.append([r,c])
# show_maps(maps)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 0으로 초기화된 N x M 행렬 생성
visited = [[0 for _ in range(M)] for _ in range(N)]
# print(visited)



def bfs(maps, x, y):
    visited[x][y]=1
    
    for i in range(0,4):
        nx = x + dx[i]
        ny = y + dy[i]

        # print(f"{nx} / {ny} / {x} / {y}")

        

        if nx<0 or ny <0 or nx>N-1 or ny > M-1:
            continue

        if maps[nx][ny] ==-1:
            continue
        if visited[nx][ny] == 1:
            continue
        maps[nx][ny]=1
        que.append([nx,ny])
        # show_maps(maps)
        
        
        # bfs(maps,nx,ny)
    


while que:
    x ,y = que.popleft()
    print(f"{x} / {y}")
    
    bfs(maps,x,y)
    show_maps(visited)


