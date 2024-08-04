
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
# 0으로 초기화된 N x M 행렬 생성
visited = [[0 for _ in range(M)] for _ in range(N)]

maps =[]
tomato_answer =N*M
tomato_chk=0
que = deque()
nextque = deque()
for r in range(0,N):
    row = list(map(int,input().split()))
    maps.append(row)
    for c in range(0, M):
        if row[c] ==1:
            # print(f"{r} / {c}")
            que.append([r,c])
            tomato_chk+=1
        if row[c] ==-1:
            tomato_answer-=1
            visited[r][c]=1

# show_maps(maps)

dx = [-1,0,1,0]
dy = [0,-1,0,1]







def bfs(maps, x, y):
    global tomato_answer
    global tomato_chk
    visited[x][y]=1
    
    
    for i in range(0,4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or ny <0 or nx>N-1 or ny > M-1:
            continue
        if visited[nx][ny] == 1:
            continue

        if maps[nx][ny] ==-1:
            continue
        if maps[nx][ny] ==1:
            continue
        maps[nx][ny]=1
        visited[nx][ny]=1
        tomato_chk+=1

        nextque.append([nx,ny])

day =0
while que:
    x ,y = que.popleft()
    # print(f"{x}, {y}")
    
    bfs(maps,x,y)

    if not que:
        # print("@@@@@@@@@@@@@")
        # show_maps(maps)
        # print(f"tomato_chk : {tomato_chk}")
        # print("que is empty..")
        
        # print(nextque)
        if tomato_chk !=tomato_answer:
            que=nextque
            nextque=deque()
            day +=1
            # show_maps(visited)
# print(day)
# print(f"tomato_answer : {tomato_answer}")
# print(f"tomato_chk : {tomato_chk}")
if tomato_chk !=tomato_answer:
    print("-1")
elif day==0:
    print(day)
else:
    print(day+1)

# print(tomato_chk)
# print(day)



"""
tomato_answer
tomato_chk
갯수가 안맞아서 오래 걸렸음..(1시간 삽질)

        if maps[nx][ny] ==1:
            continue
조건을 주지 않아서 인접한 토마토가 있는 경우에 tomato_chk가 더 증가하는 경우가 발생함..
"""