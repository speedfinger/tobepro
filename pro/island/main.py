"""
https://codepass.co.kr/contest/404/problem/9?cursor=eyJwcm9ibGVtc2V0IjoiY180MDQiLCJmaWVsZCI6MCwiaWR4Ijo4fQ==



[제약사항]

1. 각 테스트 케이스 시작 시 init() 함수가 호출된다.

2. 각 테스트 케이스에서 getcount() 함수의 호출 횟수는 150,000 이하이다.

3. 각 테스트 케이스에서 getMaxArea() 함수의 호출 횟수는 50 이하이다.

4. 각 테스트 케이스에서 getMaxArea() 함수의 구조물 structure를 설치할 수 있는 경우의 수의 총합은 5,000 이하이다.​
"""

 
### main.py ###
import sys
from solution import init, getCount, getMaxArea
# from query_to_gpt_1_5 import init, getCount, getMaxArea
 
CMD_INIT = 1
CMD_COUNT = 2
CMD_AREA = 3
 
def run():
    numQuery = int(sys.stdin.readline())
    isCorrect = False
    land = [[0 for _ in range(20)] for __ in range(20)]
    structure = [0 for _ in range(5)]
 
    for q in range(numQuery):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))
 
        if cmd == CMD_INIT:
            N = int(next(inputs))
            for i in range(N):
                for j in range(N):
                    land[i][j] = int(next(inputs))
            init(N, land)
            isCorrect = True
 
        elif cmd == CMD_COUNT:
            M = int(next(inputs))
            for i in range(M):
                structure[i] = int(next(inputs))
                # print(structure[i])
            # print(structure)
            userAns = getCount(M, structure)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False
 
        elif cmd == CMD_AREA:
            M = int(next(inputs))
            for i in range(M):
                structure[i] = int(next(inputs))
            seaLevel = int(next(inputs))
            userAns = getMaxArea(M, structure, seaLevel)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False
 
    return isCorrect
 
if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])
 
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)