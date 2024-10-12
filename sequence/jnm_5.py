"""
https://codepass.co.kr/contest/406/problem/5?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4Ijo0fQ==
"""

import sys
sys.stdin = open("./sequence/jnm_5.txt",'r')
input = sys.stdin.readline
N,K = list(map(int,input().strip().split()))

INPUT_LIST=list(map(int,input().strip().split()))
# print(*INPUT_LIST)


SUM_LIST = []

INIT_SUM = INPUT_LIST[0:K]

tmp_sum=0
for i in range(0,len(INIT_SUM)):
    tmp_sum=tmp_sum+INIT_SUM[i]

SUM_LIST.append(tmp_sum)

for i in range(1 ,len(INPUT_LIST)-K+1,1):
    """
    TMP_LIST=INPUT_LIST[i:i+K]
    tmp_sum=0
    for i in range(0,len(TMP_LIST)):
        tmp_sum=tmp_sum+TMP_LIST[i]
    SUM_LIST.append(tmp_sum)
    """
    minus = INPUT_LIST[i-1]
    plus=INPUT_LIST[i+K-1]
    tmp_sum = tmp_sum+plus-minus
    # print(f"minus: {minus}, plus:{plus}, sum:{tmp_sum}")
    SUM_LIST.append(tmp_sum)


# print(SUM_LIST)
SUM_LIST.sort(reverse=True)

print(SUM_LIST[0])