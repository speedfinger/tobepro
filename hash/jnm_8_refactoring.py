"""
hash - 문자열 넘버링
https://codepass.co.kr/contest/406/problem/8?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4Ijo3fQ==


default dict로 풀었는데, 정답으로 풀면 runtime이 훨씬 빠름
default dict : 1891ms
dict : 321ms~500ms

*********************원인은,, input = sys.stdin.readline을 쓰고 안쓰고의 차이..


import sys

if sys.platform == 'win32':         # window 환경에서만 동작
    sys.stdin = open('08.txt')      # input data를 text 파일에서 읽어오기

input = sys.stdin.readline          # 데이터 입력 속도 향상

DB = {}                             # empty dict {문자열 : [번호, 점수]}

for _ in range(int(input())):
    word, score = input().split()
    score = int(score)
    word = word.lower()             # 대소문자 구분이 없으므로 모든 문자열을 소문자로 변경

    if word in DB:
        DB[word][1] = max(DB[word][1], score)   # score를 더 큰 값으로 업데이트
    else:
        DB[word] = [len(DB) + 1, score]
    
    print(*DB[word])

        


"""

import sys
from collections import defaultdict
sys.stdin = open("./hash/jnm_8.txt",'r')

db = {}
line = int(input())
tmp_idx = 1
for _ in range(0, line):
    tmp_str,tmp_score =  input().split()
    score = int(tmp_score)
    l_str = tmp_str.lower()

    # if l_str in db:
    #     b_idx , b_score = db[l_str]
    #     if b_score<score:
    #         b_score = score        
    #     db[l_str] = [b_idx,b_score]
    #     print(f"{b_idx} {b_score}")
    # else:
    #     db[l_str] = [tmp_idx,score]
    #     print(f"{tmp_idx} {score}")
    #     tmp_idx+=1

    if l_str in db:
        db[l_str][1] = max(db[l_str][1],score)
    else:
        db[l_str] = [len(db)+1,score]
    print(*db[l_str])