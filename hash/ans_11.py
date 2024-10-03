import sys
from collections import defaultdict

# if sys.platform == 'win32':         # window 환경에서만 동작
sys.stdin = open('./hash/jnm_11.txt')      # input data를 text 파일에서 읽어오기

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

    print(tuple(dnaCnt.values()))

print(max(DB.values()))