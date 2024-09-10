"""
MCS
https://codepass.co.kr/contest/406/problem/11?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4IjoxMH0=


처음 0:k-1 까지 문자열로 db에 저장
ex) A:3,C:2,G:1,T:5

1:k 는 
0 이 A라면 A:2,C:2,G:1,T:5
k 가 C 라면 A:2,C3,G:1,T:5 
으로 저장

db = {
"A3C2G1T5":{
    "cnt":1
    ,"A":3
    ,"C":2
    ,"
    }
}

cnt를 저장하면서, 마찬가지로 top 염기서열을 계속 저장해두면,
나중에 정렬해서 최빈 염기서열을 찾을 필요가 없을 것 같음.


정답은 맞췄는데..
정답지랑 너무 큰 차이..
import sys
from collections import defaultdict

if sys.platform == 'win32':         # window 환경에서만 동작
    sys.stdin = open('11.txt')      # input data를 text 파일에서 읽어오기

input = sys.stdin.readline          # 데이터 입력 속도 향상

K = int(input())
DNA = input().strip()

DB = defaultdict(int)                       # { 알파뱃 별 빈도 수 : 등장 횟수 }

dnaCnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}   # 각 문자별 빈도수
for idx in range(len(DNA)):
    dnaCnt[DNA[idx]] += 1                   # 현재 문자의 빈도 수 +1  
    
    # sliding window가 1칸씩 이동시, 
    # 이전에 있던 가장 앞에 있던 문자의 수를 1 감소
    if idx >= K: dnaCnt[DNA[idx - K]] -= 1  
    
    # sliding window가 1칸씩 이동시, 
    # 현재 sliding window 안에 있는 문자열의 등장 횟수를 1 증가
    if idx >= K - 1: DB[tuple(dnaCnt.values())] += 1

print(max(DB.values()))

"""

import sys
sys.stdin = open('./hash/jnm_11.txt')
input = sys.stdin.readline

k = int(input().strip())
# print(f"k : {k}")
DNA = input().strip()
# print(f"k : {DNA}")

db = {}
subdna_list=[]

max_substring =""
max_cnt =0

def probe_subDNA(subdna):
    global max_cnt
    global max_substring
    A_cnt = 0
    C_cnt = 0
    G_cnt = 0
    T_cnt = 0
    for idx in range(0,k):
        character = subdna[idx]
        # print(character)
        if character == "A":
            A_cnt +=1
        elif character == "C":
            C_cnt +=1
        elif character == "G":
            G_cnt +=1
        elif character == "T":
            T_cnt +=1
    # print(f"A{A_cnt}C{C_cnt}G{G_cnt}T{T_cnt}")
    key = f"A{A_cnt}C{C_cnt}G{G_cnt}T{T_cnt}"
    db[key]={"cnt":1,"A":A_cnt,"C":C_cnt,"G":G_cnt,"T":T_cnt}
    subdna_list.append(key)
    max_substring=key
    max_cnt=1

subDNA =  DNA[0:k]
# print(f"first : {subDNA}")
probe_subDNA(subDNA)


from pprint import pprint
# DNA 문자열을 1부터 len(DNA)-k 까지 k 서브문자열로 순회
for idx in range(1,len(DNA)-k+1):
    
    subDNA = DNA[idx:idx+k]
    # print(idx)
    prev_key = subdna_list[idx-1]

    # cnt = db[prev_key]["cnt"]
    A_cnt = db[prev_key]["A"]
    C_cnt = db[prev_key]["C"]
    G_cnt = db[prev_key]["G"]
    T_cnt = db[prev_key]["T"]


    head_character = DNA[idx-1]
    tail_character = DNA[idx+k-1]

    # print(f"subDNA : {subDNA} {head_character}~{tail_character}")
    # print()
    if head_character =="A":
        A_cnt-=1
    elif head_character =="C":
        C_cnt-=1
    elif head_character =="G":
        G_cnt-=1
    elif head_character =="T":
        T_cnt -=1
    
    
    if tail_character =="A":
        A_cnt+=1
    elif tail_character =="C":
        C_cnt+=1
    elif tail_character =="G":
        G_cnt+=1
    elif tail_character =="T":
        T_cnt +=1

    key = f"A{A_cnt}C{C_cnt}G{G_cnt}T{T_cnt}"    
    subdna_list.append(key)

    if key in db:
        
        cnt = db[key]["cnt"]
        
        cnt = cnt +1

        if cnt>max_cnt:
            max_cnt=cnt
            max_substring=key
    else:
        cnt = 1
    # print(f"key : {key}")
    
    db[key]={"cnt":cnt,"A":A_cnt,"C":C_cnt,"G":G_cnt,"T":T_cnt}

    # pprint(db)
    

    
    # print(f"{idx} with {head_character},{tail_character} : {subDNA}, key:{key}")

    #서브 문자열 순회

# print(subdna_list)
# print(f"{max_substring} with {max_cnt}") 
# pprint(db)
print(max_cnt)