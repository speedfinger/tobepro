"""


22*2 
+22*2

88+8 = 96
"""

import sys

sys.stdin = open("./sequence/jnm_2.txt",'r')
input = sys.stdin.readline
NUMBER_OF_TORWHDDL = int(input().strip())

LIST_OF_X = []
LIST_OF_Y = []

for _ in range(0,NUMBER_OF_TORWHDDL):
    X,Y = map(int,input().split())
    LIST_OF_X.append(X)
    LIST_OF_Y.append(Y)
    

# print(LIST_OF_TORWHDDL)


for idx in range(0,len(LIST_OF_X)):
    X= LIST_OF_X[idx]
    Y = LIST_OF_Y[idx]


    # 가장 아랫변 탐색
    for x in range(X+1,X+11):
        
        
