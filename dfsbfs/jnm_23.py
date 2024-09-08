"""
버스 갈아타기
https://codepass.co.kr/contest/390/problem/23?cursor=eyJwcm9ibGVtc2V0IjoiY18zOTAiLCJmaWVsZCI6MCwiaWR4IjoyMn0=


출발지와 목적지는 다르게 주어지며 출발지에서 목적지로 가는 방법은 한 가지 이상 존재


입력
첫 번째 줄에 수직선의 수 m과 수평선의 수 n이 빈칸을 사이에 두고 주어진다(1 ≤ m,n ≤ 100,000).
두 번째 줄에 버스의 수 k(1≤k≤5,000)가 주어진다. 
세 번째 줄부터 k줄에 걸쳐 각 줄에 버스의 운행구간을 나타내는 5개의 수 b, x1, y1, x2, y2가 빈칸을 사이에 두고 주어진다. 
여기서 b(1≤b≤k)는 버스의 번호, (x1,y1)과 (x2,y2)는 이 버스가 운행하는 양쪽 끝 교차점의 좌표를 나타낸다. 
마지막 줄에 출발지와 목적지 좌표를 나타내는 네 개의 수 sx, sy, dx, dy가 빈칸을 사이에 두고 주어진다. 
여기서 (sx,sy)는 출발지 좌표이고 (dx,dy)는 목적지 좌표이다. 1≤x1, x2, sx, dx≤m이고, 1≤y1, y2, sy, dy≤n이다. 
모든 입력에 대하여, 출발지와 목적지는 다르게 주어지며 출발지에서 목적지로 가는 방법은 한 가지 이상 존재한다.
<제약조건> 
m 혹은 n이 1인 테스트데이터가 전체의 20%이다.

*************
핵심은 
- 제약조건? m 혹은 n이 1인 테스트데이터가 전체의 20%이다.


출발지가 (2, 1)이고 목적지가 (7, 4)라 하자. 

2번 버스: (1, 1) - (5, 1)
3번 버스: (3, 2) - (6, 2)
4번 버스: (5, 6) - (5, 1)
5번 버스: (1, 5) - (7, 5)
6번 버스: (7, 3) - (7, 6)
7번 버스: (2, 1) - (2, 6)
8번 버스: (3, 5) - (6, 5)

출발지 2,1
-> 
2번버스, 7번 버스
1<=x=<5 and 1<=y <=1
위 식을 만족하는 버스를 찾고, 버스가 방문 가능한 모든 점을 방문하면서, 모든 버스에 대해서 계속 방문한다.
버스를 방문할때마다 +1

dfs, bfs ?


lesson learn 
점탐 색이 아니라 선 탐색임
ans_23.py 참고,,

"""

import sys
import copy

sys.stdin = open('./dfsbfs/jnm_23.txt','r')

X,Y=list(map(int,input().split(" ")))
# print(f"{X},{Y}")
bus_number = int(input())
# print(f"{bus_number}")

def show_bus(bus_list):
    for i in range(0,len(bus_list)):
        print(bus_list[i])
    print("@@@@@")


"""
입력단계
"""
bus_list=[]
visited =[[0 for _ in range(0, X)] for _ in range(0, Y) ]

for i in range(0,bus_number):
    bus_n,s_x,s_y,e_x,e_y=input().split(" ")
    bus_list.append([bus_n,s_x,s_y,e_x,e_y])
# show_bus(bus_list)

start_X,start_Y,end_X,end_Y=list(map(int,input().split(" ")))
# print(f"{start_X},{start_Y}/ {end_X},{end_Y}")

min_transfer_cnt = 999
bus_set=set()


transfer_cnt_answer_list =[]

def dfsbfs(x,y,transferCOUNT,is_visited,bus_set):
    global min_transfer_cnt
    new_transferCOUNT=transferCOUNT
    # print(f"?? xy : {x},{y} / {end_X}/{end_Y}, transferCOUNT :{transferCOUNT}, new_bus_set:{bus_set}")
    # new_visited=copy.deepcopy(is_visited)
    # new_visited[y-1][x-1]=1
    # show_bus(is_visited)
    is_visited[y-1][x-1]=1

    if x==end_X and y==end_Y:
        print(f"end...@@@@@ {transferCOUNT}")
        # return transferCOUNT
        transfer_cnt_answer_list.append(transferCOUNT)

    for i in range(0,bus_number):
        new_transferCNT=transferCOUNT
        new_bus_set = copy.deepcopy(bus_set)


        # print(bus_list[i])
        bus_NUMBER,bus_SX,bus_SY,bus_EX,bus_EY= list(map(int, bus_list[i]))
        # print(type(x))
        # print(type(bus_NUMBER))
        # print(type(bus_SX))

        is_possible_transfer = ((bus_SX<=x and x<=bus_EX) and (bus_SY<=y and y<=bus_EY)) or ((bus_EX<=x and x<=bus_SX) and (bus_EY<=y and y<=bus_SY))
        
            

        if is_possible_transfer:
            print(f"bus_NUMBER: {bus_NUMBER} with start: {x},{y} / new_transferCNT:{new_transferCNT}")
            show_bus(is_visited)
            new_transferCNT+=1
            new_bus_set.add(bus_NUMBER)
            for nx in range(bus_SX,bus_EX+1):
                for ny in range(bus_SY,bus_EY+1):
                    if is_visited[ny-1][nx-1]==1:
                        continue
                    # print(f"bus xy : {nx},{ny}")
                    # if x !=nx and y !=ny:
                    # if x !=nx or y !=ny:
                    if (x !=nx or y !=ny):
                        # is_visited[ny-1][nx-1]=1
                        
                        # print(f"visited : {nx},{ny}")
                        dfsbfs(nx,ny,new_transferCNT,is_visited,new_bus_set)
                        # print(f"### dfsbfs return...{min_transfer_cnt}, call value : {nx},{ny}")
    # return min_transfer_cnt
                        

"""
bfs호출
"""
dfsbfs(start_X,start_Y,0,visited,bus_set)
print(transfer_cnt_answer_list)