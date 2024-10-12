import sys
from collections import deque

if sys.platform == 'win32':     # window 환경에서만 동작
    sys.stdin = open('04.txt')  # input data를 text 파일에서 읽어오기

input = sys.stdin.readline      # 데이터 입력 속도 향상

# seq = []                        # 수열
seq = deque()                   # 수열

def insertData(pos, value):
    if pos: seq.append(value)       # O(1)
    # else: seq.insert(0, value)      # O(N), list
    else: seq.appendleft(value)     # O(1), deque

# 방법 1 - list
def eraseData(pos, value):
    cnt = 0                         # value 이상의 값을 지운 횟수
    if pos:                         # 뒤에서 부터 value 이상의 값 지우기
        idx = len(seq) - 1
        while idx >= 0:
            if seq[idx] >= value:   # 삭제 대상인 경우
                seq.pop(idx)        # O(N)
                cnt += 1
                if cnt >= 3: break  # 3개 이상을 지운 경우 break
            idx -= 1
    else:                           # 앞에서 부터 value 이상의 값 지우기
        idx = 0
        while idx < len(seq):
            if seq[idx] >= value:   # 삭제 대상인 경우
                seq.pop(idx)        # O(N)
                cnt += 1
                if cnt >= 3: break  # 3개 이상을 지운 경우 break
            else:
                idx += 1        

# 방법 2 - list, deque
# def eraseData(pos, value):
#     global seq
#     # temp = []                           # 살아남을 수열
#     temp = deque()                      # 살아남을 수열
#     cnt = 0                             # value 이상의 값을 지운 횟수
    
#     if pos:                             # 뒤에서 부터 value 이상의 값 지우기
#         for s in reversed(seq):
#             if s < value or cnt >= 3:   # 숫자를 새로운 수열로 옮기는 경우
#                 # temp.append(s)        # list, O(1)
#                 temp.appendleft(s)      # deque, O(1)
#             else:
#                 cnt += 1
#         # temp.reverse()                # list
#     else:
#         for s in seq:
#             if s < value or cnt >= 3:   # 숫자를 새로운 수열로 옮기는 경우
#                 temp.append(s)
#             else:
#                 cnt += 1
#     seq = temp            

def sortData(value):
    global seq
    # 1순위: abs(value - x) 작은 순, 2순위: x가 작은 순
    # seq.sort(key=lambda x: (abs(value - x), x))               # O(N * log N), list
    seq = deque(sorted(seq, key=lambda x: (abs(value - x), x))) # O(N * log N), deque
    
def printData(pos):
    if pos: print(*reversed(seq))
    else: print(*seq)

for _ in range(int(input())):   # 쿼리 수 만큼 명령어 수행
    cmd, *val = map(int, input().split())
    if cmd == 1: insertData(*val)
    if cmd == 2: eraseData(*val)
    if cmd == 3: sortData(*val)
    if cmd == 4: printData(*val)