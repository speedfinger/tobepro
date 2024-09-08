"""
https://codepass.co.kr/contest/406/problem/9?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4Ijo4fQ==
hash - 문자열 별칭

입력
9
son
sonny
song
so
su
son
s
son
s

출력
s
sonn
song
so
su
son2
s
son3
s2


풀긴 했는데, 정답 코드가 너무 간결함..
import sys
from collections import defaultdict

if sys.platform == 'win32':         # window 환경에서만 동작
    sys.stdin = open('09.txt')      # input data를 text 파일에서 읽어오기

input = sys.stdin.readline          # 데이터 입력 속도 향상

# DB = {}                             # { 접두사 : str로 나온 횟수 }
DB = defaultdict(int)

for _ in range(int(input())):
    word = input().strip()
    
    ans = ""                        # 별칭
    prefix = ""                     # 접두사
    for w in word:
        prefix += w                 # 접두사 만들기
        if prefix not in DB:        # 접두사가 DB에 없는 경우
            DB[prefix]
            # DB[prefix] = 0          # 접두사를 DB에 등록
            if not ans:             # 별칭이 정해지지 않은 경우
                ans = prefix
    DB[word] += 1                   # str로 등장한 문자열의 나온 횟수 +1
    
    if not ans:                     # 이미 접두사가 모두 DB에 등록 되어 있던 경우
        ans = word
        if DB[word] > 1: ans += str(DB[word])   # cnt 값이 2이상인 경우 숫자를 붙여서 별칭 생성

    print(ans)

"""

import sys

sys.stdin = open('./hash/jnm_9.txt')
input = sys.stdin.readline

line = int(input())

db = {}
cnt_db ={}

for _ in range(0,line):
    # print(input())
    text = input().strip()
    if text not in cnt_db:
        cnt_db[text] = 1
    else:
        cnt_db[text] = cnt_db[text]+1
    # print(f"{text} : {len(text)}")
    
    prefix = text[0:1]
    # print(type(prefix))
    if prefix not in db:
       db[prefix] = set()       
    tmp_set = db[prefix]


    is_print = False
    cnt = 0
    for idx in range(0,len(text)):
        split_text = text[0:idx+1]
        # print(split_text)

        if split_text not in tmp_set and not is_print:
            # print(f"{text} : {split_text}")
            print(split_text)
            is_print = True
        else:
            cnt+=1
        tmp_set.add(split_text)

        if cnt == len(text) and not is_print:
            if cnt_db[text]==1:
                # print(f"{text} : {split_text}")
                print(split_text)
            else:
                # print(f"{text} : {split_text}{cnt_db[text]}")
                print(f"{split_text}{cnt_db[text]}")
            # print(f"{text} : {split_text} with cnt {cnt_db[text]}")
            # cnt_db[text] = cnt_db[text]+1

    # print(f"@@@@@@@@@@@@ with prefix : {prefix}")

# print(db)