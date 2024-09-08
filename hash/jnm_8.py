"""
hash - 문자열 넘버링
https://codepass.co.kr/contest/406/problem/8?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4Ijo3fQ==

"""

import sys
from collections import defaultdict
sys.stdin = open("./hash/jnm_8.txt",'r')


db = defaultdict(str)

line = int(input())
tmp_idx = 1
for _ in range(0, line):
    # print(input())
    tmp_str,tmp_score = list(map(str,input().split()))
    score = int(tmp_score)
    l_str = tmp_str.lower()
    # print(f"{l_str} : {score}")


    
    if db[l_str]:
        b_idx , b_score = db[l_str]
        # print(f"already has value , {b_idx}, {b_score}")
        
        if b_score<score:
            b_score = score
        
        db[l_str] = [b_idx,b_score]
        print(f"{b_idx} {b_score}")

        
        # _socre=db[l_str]
    else:
        db[l_str] = [tmp_idx,score]
        print(f"{tmp_idx} {score}")
        tmp_idx+=1

# print(db)    