"""
보물섬
https://codepass.co.kr/contest/390/problem/21?cursor=eyJwcm9ibGVtc2V0IjoiY18zOTAiLCJmaWVsZCI6MCwiaWR4IjoyMH0=

WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

WLLWWWL
LLLWLLL
LLLWLWW
LLLWLLL
WLLWLWW

1. 꼭지점 먼저 구하기

2. 꼭지점들 중 하나를 임의로 선정 해서, 간선(거리)를 가진 그래프로 변환

3. 완전탐색..?
더 좋은 방법?????


todo::
코테를 할때 좌표 저장시 [[x,y]...] 형태로 많이 쓰는데..
defaultdict를 쓰지 않고 중복 제거하는방법

"""
import sys
from collections import deque
import copy
from collections import defaultdict

sys.stdin = open("./dfsbfs/jnm_21.txt",'r')


def show_maps(maps):
    for i in range(0,len(maps)):
        print(maps[i])
    print("@@@@@@@@@@@@@@@@")


R, C = map(int,input().split())

maps =[]

# Land 
que = deque()
visited =[[0 for _ in range(0, C)] for _ in range(0, R) ]
# 꼭지점 리스트
# dot_list =[]
dot_list = defaultdict(list)

#map을 읽으면서, visited(방문 가능한 땅인지) 기록
for r in range(0, R):
    row = list(map(str,input()))
    maps.append(row)
    for c in range(0,C):
        if maps[r][c]=="L":
            que.append([r,c])
        else:
            visited[r][c]=1

show_maps(maps)
# print(que)
show_maps(visited)

dx =[-1,0,1,0]
dy =[0,-1,0,1]

from_xy=[]
to_xy=[]

def bfs(maps,x,y):
    
    visited[x][y]==1
    global from_xy
    from_xy = [x,y]
    print(from_xy)
    for i in range(0,4):
        # print(i)
        nx=x+dx[i]
        ny=y+dy[i]
        # print(f"x, y visited : {nx},{ny} / {x},{y}")

        if nx <0 or ny <0 or nx>R-1 or ny>C-1:
            continue
        
        # W (땅이 아니라면) pass
        if visited[nx][ny] ==1:
            continue
        visited[nx][ny]=1
        bfs(maps,nx,ny)

#꼭지점 구하기
dot_que = copy.deepcopy(que)
# print(f"dot_que : {dot_que}")
while dot_que:
    x , y= dot_que.popleft()
    # print(f"checking dot ... {x} , {y}")

    
    for i in range(0,4):
        cnt = 0

        nx1 = x + dx[i]
        ny1 = y + dy[i]

        if i !=3:
            nx2 = x + dx[i+1]
            ny2 = y + dy[i+1]
        else:
            nx2 = x + dx[0]
            ny2 = y + dy[0]

        # print(f"{nx1},{ny1} / {nx2},{ny2}")
        if nx1 <0 or ny1 <0 or nx1>R-1 or ny1>C-1:
            cnt +=1
        else:
            if visited[nx1][ny1] ==1:
                cnt +=1 
        
        if nx2 <0 or ny2 <0 or nx2>R-1 or ny2>C-1:
            cnt +=1
        else:
            if visited[nx2][ny2] ==1:
                cnt +=1 

        if cnt == 2:
            # dot_list.append([x,y])
            dot_list[(x,y)]=1


print(dot_list)

# 
"""
꼭지점 하나 뽑아서
인접 행렬로 가중치 저장해서
모든 꼭지점

dp 150*150 정도가 메모리 사용
"""


# while que:
#     x , y = que.popleft()
#     # print(que)
#     if visited[x][y] ==0:
#         bfs(maps,x,y)
# show_maps(visited)
