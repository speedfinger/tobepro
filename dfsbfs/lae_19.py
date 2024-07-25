import sys
from collections import deque

if sys.platform=="win32":
    sys.stdin = open("lae_19.txt")

input = sys.stdin.readline

N, M = map(int, input().split())

mat = [[0]*(N+1) for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
visit = [0]*(N+1)
count = 0

def setMat():
    for _ in range(M):
        a, b = map(int, input().split())
        mat[a][b] = mat[b][a] = 1

def setArr():
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

def dfsMat(n):
    visit[n] = 1
    for v in range(1,N+1):
        if mat[n][v]==1 and visit[v]==0:
            dfsMat(v)

def bfsMat(n):
    visit[n] = 1
    que = deque([n])

    while(que):
        q = que.popleft()
        for v in range(1,N+1):
            if mat[q][v] and visit[v]==0:
                visit[v]=1
                que.append(v)

def dfsArr(n):
    visit[n] = 1
    for v in arr[n]:
        if visit[v]==0:
            dfsArr(v)

def bfsArr(n):
    visit[n] = 1
    que = deque([n])

    while(que):
        q = que.popleft()
        for v in arr[q]:
            if visit[v]==0:
                visit[v]=1
                que.append(v)

# setMat()
setArr()

for i in range(1,N+1):
    if visit[i]==0:
        # dfsMat(i)
        # bfsMat(i)
        # dfsArr(i)
        bfsArr(i)
        count+=1

print(count)