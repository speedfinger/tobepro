import sys

# if sys.platform == 'win32':         # window 환경에서만 동작
sys.stdin = open('./hash/jnm_12.txt')      # input data를 text 파일에서 읽어오기

input = sys.stdin.readline          # 데이터 입력 속도 향상

A = input().strip()
B = input().strip()

# windowAlphCnt에 ch의 빈도 수를 delta 만큼 업데이트
def update(ch, delta):
    idx = ord(ch) - ord('a')        # 알파벳을 숫자 0 ~ 25로 변환
    windowAlphCnt[idx] += delta

def findSameSeq(k):
    global windowAlphCnt
    DB = set()                  # 알파벳 별 빈도 수 조합 DB, ex> (0, 3, ..., 1) => 26개 숫자

    windowAlphCnt = [0] * 26    # 알파벳 별 빈도 수

    # A 문자열의 k 구간 길이에 대한 알파벳 빈도 수 DB 생성
    for i in range(len(A)):
        update(A[i], 1)         # 현재 알파벳의 빈도 수 +1

        # sliding window가 1칸 이동시,
        # 이전에 있던 가장 앞에 있던 문자의 빈도 수 -1
        if i >= k: update(A[i - k], -1)

        # sliding window가 움직이기 시작하면,
        # 현재 sliding window의 알파벳 빈도 수를 DB에 등록
        if i >= k - 1: DB.add(tuple(windowAlphCnt))

    print(f"k {k} : {DB}")
    
    # B 문자열의 k 구간 길이의 알파벳 빈도 수 조합이 DB에 존재하는지 확인
    windowAlphCnt = [0] * 26
    for i in range(len(B)):
        update(B[i], 1)         # 현재 알파벳의 빈도 수 +1

        # sliding window가 1칸 이동시,
        # 이전에 있던 가장 앞에 있던 문자의 빈도 수 -1
        if i >= k: update(B[i - k], -1)

        # sliding window가 움직이기 시작하면,
        # 현재 sliding window의 알파벳 빈도 수 조합이 DB에 있는지 확인
        if i >= k - 1 and tuple(windowAlphCnt) in DB: return True
    
    return False    # k 구간의 길이에서는 같은 성분을 찾지 못한 경우

# k는 비교할 구간의 길이, 긴 구간 길이 부터 확인
for k in range(min(len(A), len(B)), -1, -1):
    # k 구간 길이에 해당하는 같은 성분의 구간이 있는지 확인
    if findSameSeq(k):
        print(k)
        break