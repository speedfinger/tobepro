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
*******************************
->  반례 존재...
3 7
LLLWLLL
LWLLLWL
LLLWLLL



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
dot_defaultdict = defaultdict(list)

#map을 읽으면서, visited(방문 가능한 땅인지) 기록
for r in range(0, R):
    row = list(map(str,input()))
    maps.append(row)
    for c in range(0,C):
        if maps[r][c]=="L":
            que.append([r,c])
        else:
            visited[r][c]=1

# show_maps(maps)
# show_maps(visited)

dx =[-1,0,1,0]
dy =[0,-1,0,1]

from_xy=[]
to_xy=[]

def bfs(x,y):
    max = -1
    search_que = deque()

    is_possible_visit = copy.deepcopy(visited)

    if is_possible_visit[x][y] ==0:
        search_que.append([x,y,0])
        is_possible_visit[x][y]=1 
        """
        is_possible_visit[x][y]=1  방문하지 않아서 
        아래와 같은 TC 통과하지 못함
        4 3
        WWW
        WLW
        WLW
        WWW
        """

    while(search_que):

        sx,sy,dist = search_que.popleft()

        for i in range(0,4):
            nx = sx + dx[i]
            ny = sy + dy[i]

            # if x==2 and y ==2 and sx==1 and sy==1:
            #     print(f"{nx},{ny}")


            """
            if nx<0 or ny <0 or nx >R-1 or ny >C-1:
            을 아래처럼 초반에 nx<=0   등호가 포함됐는데, 찾지 못해서 40분 허비..
            if nx<=0 or ny <0 or nx >R-1 or ny >C-1:
            """
            if nx<0 or ny <0 or nx >R-1 or ny >C-1:
                continue

            # if x==2 and y ==2:
            #     print(f"{sx},{sy} / {nx},{ny} / {is_possible_visit[nx][ny]}")
            
            if is_possible_visit[nx][ny] ==0:
                is_possible_visit[nx][ny]=1
                search_que.append([nx,ny,dist+1])

                
                if dist+1>max:
                    max=dist+1
                if x==2 and y ==2:
                    pass
                    # show_maps(is_possible_visit)
                    # print(f"{sx},{sy} / {nx},{ny} / {max}")
                    # print(search_que)

    # print(f"{x} / {y} / {max}")
    return max 



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
            # dot_defaultdict.append([x,y])
            dot_defaultdict[(x,y)]=1


# print(dot_defaultdict)

# 
"""
꼭지점 하나 뽑아서
인접 행렬로 가중치 저장해서
모든 꼭지점

dp 150*150 정도가 메모리 사용

=>> 
허무하다는 것에서 hint..
꼭지점 모두 n*n bfs  ?

"""
dot_list=[]
for k,v in dot_defaultdict.items():
    dot_list.append(k)
# print(dot_list)    

answer = -1
# for i in range(0,len(dot_list)):
#     x,y = dot_list[i]
#     answer = max(answer,bfs(x,y))
    

for i in range(R):
    for j in range(C):
        answer = max(answer, bfs(i,j))    
# bfs(answer,4,1)    

print(answer)

# while que:
#     x , y = que.popleft()
#     # print(que)
#     if visited[x][y] ==0:
#         bfs(maps,x,y)
# show_maps(visited)
