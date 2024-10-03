import sys

# if sys.platform == 'win32':         # window 환경에서만 동작
sys.stdin = open('./hash/jnm_10.txt')      # input data를 text 파일에서 읽어오기

input = sys.stdin.readline          # 데이터 입력 속도 향상

DB = {}                             # 땅 위치 별 주인 { 땅의 좌표 : 플레이어 id}
playerCnt = [0] * 4                 # 플레이어 별 가지고 있는 땅의 수

N, Q = map(int, input().split())

for i in range(Q):
    curId = i % 4                           # 현재 플레이어의 id
    loc = tuple(map(int, input().split()))  # 현재 플레이 중인 땅의 위치 (row, col)
    print(loc)
    
    # 땅이 점령 되어 있는지 확인
    if loc in DB:                           # 땅이 점령 되어 있는 경우
        prevId = DB[loc]                    # 땅의 원래 주인 ID
        if prevId == curId:
            DB.pop(loc)                     # 땅 반납하기
            playerCnt[curId] -= 1
        elif playerCnt[prevId] > playerCnt[curId]:  # 현재 플레이어의 땅의 수가 더 적은 경우
            DB[loc] = curId
            playerCnt[curId] += 1
            playerCnt[prevId] -= 1
    else:                                   # 땅의 주인이 없는 경우
        DB[loc] = curId
        playerCnt[curId] += 1

print(*playerCnt, sep='\n')
            