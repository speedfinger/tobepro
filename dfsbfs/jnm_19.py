"""
https://www.codepass.co.kr/bbs/bbs_solve_lecture.php?idx=390&prod_idx=5027&pCode=lecture&seq=19&page=
연결요소세기
"""

import sys

sys.stdin = open('./jnm_19.txt','r')

# T = int(input())

def show_map(maps):
    for i in range(0,len(maps)):
        print(maps[i])

def dfs(links,idx,visited):
    visited[idx-1]=True
    for i in links[idx-1]:
        if not visited[i-1]:
            dfs(links,i,visited)

# for tc_case in range(0,T):
N,M =map(int,input().split())


links =[]
for i in range(0,(N)):
    links.append([])

for i in range(0,(M)):        
    # print()
    n,m=map(int,input().split())
    # print(f"{n} / {m}")
    links[n-1].append(m)
    links[m-1].append(n)

show_map(links)

visited=[False]*N
count = 0
for idx,is_visitied in enumerate(visited):
    if is_visitied == False:
        dfs(links,idx+1,visited)
        count+=1
        
# print(visited)
print(count)

