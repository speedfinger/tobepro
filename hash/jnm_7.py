"""
hash - 문자열 검색
https://codepass.co.kr/contest/406/problem/7?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4Ijo2fQ==

"""

import sys

sys.stdin = open('./hash/jnm_7.txt')

line = int(input())

input_list=[]
db_set=set()
for _ in range(0,line):    
    tmp_str = input()
    if tmp_str in db_set:
        db_set.remove(tmp_str)
    else:
        db_set.add(tmp_str)


# print(db_set)
print(len(db_set))

