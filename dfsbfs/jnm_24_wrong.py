"""
https://codepass.co.kr/contest/406/problem/24?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4IjoyM30%3D

로봇

일단 bfs인것 같음.


1. break point를 잘못 선정함,
- > 55 53 -> 회전 count를 하고 정답을 산출..

2. 아래와 같이 제자리에서 로테이션 도는 경우를 만족하지 못함
3 3
1 1 1
1 0 1
1 1 1
2 2 1
2 2 2

3. 
목적지까지 갈수 있는 경로가 여러개 있을 경우,
A: 이동만 하면 끝나는 경우
B: 이동 후 회전을 해야 하는 끝나는 경우
의 케이스가 있을때

A는 이동하는 경우가 B의 이동시점이랑 같은 bfs호출 횟수라면 ,,
B의 경우가 먼저 return 되서 (회전count가 처리되서) 오답이 되는 경우가 발생할 수 있음

"""
import sys
import copy
from collections import deque

sys.stdin = open('./dfsbfs/jnm_24.txt','r')

M,N=list(map(int,input().split()))

def show_map(bus_list):
    for i in range(0,len(bus_list)):
        print(bus_list[i])
    print("@@@@@")

# def show_map(bus_list):
#     for item in reversed(bus_list):
#         print(item)
#     print("@@@@@")

maps=[]
for _ in range(0,M):
    maps.append(list(map(int,input().split())))

# maps[3][1]=5

vistied = [[0 for _ in range(0,N)] for _ in range( 0, M)]

visited_r = [[[0] * 5 for _ in range(N)] for _ in range(M)]

# show_map(maps)
# show_map(vistied)

start_X,start_Y,start_R = list(map(int,input().split()))
end_X,end_Y,end_R = list(map(int,input().split()))

que = deque()
que.append([start_X,start_Y,start_R,0])
# vistied[start_X-1][start_Y-1]=1




d_r = [1,2,3,4]

#동 서 남 북에 따라 x, y좌표 이동
d_y = [1,-1,0,0]
d_x = [0,0,1,-1]


def bfs(s_x,s_y,s_r,command_cnt):
    if s_x==end_X and s_y == end_Y and s_r == end_R:
        return command_cnt
    
# if M == 44 and M ==36:
#     print(f"{start_X},{start_Y},{start_R}")    

while que:
    # print(que)
    
    st_x , st_y, st_r, command_cnt=que.popleft()    

    if vistied[st_x-1][st_y-1] == 1:
        continue

    if vistied[st_x-1][st_y-1] == 0:
        vistied[st_x-1][st_y-1] =1

    for idx in range(0,len(d_r)):
        tmp_command = command_cnt
        direction = d_r[idx]

        # print(f"{st_x},{st_y},{direction} / {end_X},{end_Y},{end_R}")
        

        if st_r==direction:
            pass
        else:
            if (direction==1 and st_r==2)or (direction==2 and st_r==1)or (direction==3 and st_r==4)or (direction==4 and st_r==3):
                # print(f"{direction} and {st_r} have to 2 commans")
                tmp_command+=2
            else:
                tmp_command+=1

        if st_x==end_X and st_y == end_Y and direction == end_R:
            print(f"{tmp_command}")
            break
        # if st_x == 2 and st_y ==4 :
            # print(f"{direction}?????? {end_X},{end_Y},{end_R}")
        
        
        for mul in range(0,3):
            nx = st_x + d_x[direction-1]*(mul+1)
            ny = st_y + d_y[direction-1]*(mul+1)

            # print(f"{st_x},{st_y} / {direction} -> {nx},{ny}")

            if nx<=0 or nx> M or ny<=0 or ny>N:
                break
            
            if maps[nx-1][ny-1]==1 :
                break

            
            if vistied[nx-1][ny-1] == 0:
                que.append([nx,ny,direction,tmp_command+1])



    
    


# show_map(vistied)    
# show_map(visited_r)    