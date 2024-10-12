"""
색종이(초)
https://codepass.co.kr/contest/406/problem/1?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4IjowfQ==


"""

import sys


sys.stdin = open("./sequence/jnm_1.txt",'r')

input = sys.stdin.readline

NUMBER_OF_TORWHDDL = int(input().strip())




SIZE = 25
EHGHKWL = [[0]*SIZE for _ in range(0,SIZE)]


def print_map(EHGHKWL):
    for i in range(len(EHGHKWL)-1,-1,-1):
        print(EHGHKWL[i])

LIST_OF_TORWHDDL=[]
for _ in range(0,NUMBER_OF_TORWHDDL):
    X,Y = map(int,input().strip().split())
    LIST_OF_TORWHDDL.append([X,Y])

    for x in range(X-1,X+9):
        for y in range(Y-1,Y+9):
            EHGHKWL[y][x]=1
    
    # EHGHKWL[X-1:X+9][Y-1:Y+9]=1
    # EHGHKWL[Y-1:Y+9]=1

# print(LIST_OF_TORWHDDL)


# EHGHKWL[0][1]=1

# EHGHKWL[1][0]=1

# print_map(EHGHKWL)

sum =0
for i in range(0,len(EHGHKWL)):
    for k in range(0,len(EHGHKWL[i])):
        if EHGHKWL[i][k]==1:
            sum=sum+1
print(sum)