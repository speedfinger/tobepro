import sys
from collections import deque

if sys.platform == "win32":
    sys.stdin = open("lae_23.txt")

input = sys.stdin.readline

X, Y = map(int, input().split())
mat = [[0] * (X + 1) for _ in range(Y + 1)]
visited = [[0] * (X + 1) for _ in range(Y + 1)]
bus = int(input())
busArr = [[] for _ in range(bus+1)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

xLine = [[] for _ in range(X+1)]
yLine = [[] for _ in range(Y+1)]

def setBusLine():
    for _ in range(bus):
        num, x1, y1, x2, y2 = map(int, input().split())
        maxY = max(y1, y2)
        minY = min(y1, y2)
        maxX = max(x1, x2)
        minX = min(x1, x2)
        if minX == maxX:
            for v in xLine[minX]:
                vx1, vy1 = busArr[v][0]
                vx2, vy2 = busArr[v][1]
                minvY = min(vy1, vy2)
                maxvY = max(vy1, vy2)
                if maxY <= minvY or maxvY <= minY:
                    continue
                elif minY < minvY and minvY < maxY and maxY < maxvY:
                    y1 = minY
                    y2 = minvY
                elif minvY < minY and minY < maxvY and maxvY < maxY:
                    y1 = maxvY
                    y2 = maxY
                elif minvY < minY and maxY < maxvY:
                    y1 = 0
                    y2 = 0
                else:
                    busArr[v][0] = (minX, minY)
                    busArr[v][1] = (minX, maxY)
                    y1 = 0
                    y2 = 0
            xLine[minX].append(num)
        if minY == maxY:
            for v in yLine[minY]:
                vx1, vy1 = busArr[v][0]
                vx2, vy2 = busArr[v][1]
                minvX = min(vx1, vx2)
                maxvX = max(vx1, vx2)
                if maxX <= minvX or maxvX <= minX:
                    continue
                elif minX < minvX and minvX < maxX and maxX < maxvX:
                    x1 = minX
                    x2 = minvX
                elif minvX < minX and minX< maxvX and maxvX < maxX:
                    x1 = maxvX
                    X2 = maxX
                elif minvX < minX and maxX < maxvX:
                    x1 = 0
                    x2 = 0
                else:
                    busArr[v][0] = (minX, minY)
                    busArr[v][1] = (maxX, minY)
                    x1 = 0
                    x2 = 0
            yLine[minY].append(num)
        busArr[num].append((x1,y1))
        busArr[num].append((x2,y2))

def setMat():
    for v in range(1, len(busArr)):
        x1, y1 = busArr[v][0]
        x2, y2 = busArr[v][1]
        maxY = max(y1, y2)
        minY = min(y1, y2)
        maxX = max(x1, x2)
        minX = min(x1, x2)
        if x1 == x2:
            for i in range(maxY-minY+1):
                mat[minY+i][x1] += 1
        elif y1 == y2:
            for i in range(maxX-minX+1):
                mat[y1][minX+i] += 1

def bfs(sx, sy, ex, ey):
    visited[sy][sx] = 1
    que = deque([(sy, sx, 1)])
    minTrans = 9876543210

    while(que):
        y, x, trans = que.popleft()
        if y == ey and x == ex:
            minTrans = min(trans, minTrans)
        else :
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (nx < 1 or nx > X or ny < 1 or ny > Y):
                    continue
                elif mat[ny][nx] != 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    if mat[ny][nx] > 1:
                        trans +=1
                    que.append((ny,nx,trans))
    return minTrans

def getAnswer():
    sx, sy, ex, ey = map(int, input().split())
    answer = bfs(sx, sy, ex, ey)
    return answer

setBusLine()
setMat()

for i in range(Y):
    for j in range(X):
        print(mat[j][i], end= " ")
    print()
# print(getAnswer())