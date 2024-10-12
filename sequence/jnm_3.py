"""

import sys

if sys.platform == 'win32':     # window 환경에서만 동작
    sys.stdin = open('03.txt')  # input data를 text 파일에서 읽어오기

input = sys.stdin.readline      # 데이터 입력 속도 향상

scores = []                     # 학생들의 점수 리스트 (수학, 과학, 번호)

# 데이터 입력 받기
for i in range(1, 6):
    a, b = map(int, input().split())
    scores.append((a, b, i))

mode = int(input())

if mode == 1:                               # 수학 점수 별 정렬
    # scores.sort(reverse=1)                # 내림차순
    scores.sort(key = lambda tu: -tu[0])    # 내림차순
elif mode == 2:                             # 과학 점수 별 정렬
    scores.sort(reverse=1, key = lambda tu: tu[1])
else:                                       # 수학 + 과학 점수 별 정렬
    scores.sort(reverse=1, key = lambda tu: tu[0] + tu[1])
    
print(*[tu[2] for tu in scores])


*lambda 활용하는거... 
print(' '.join(map(str, print_result)))

"""
import sys

sys.stdin = open("./sequence/jnm_3.txt",'r')

input = sys.stdin.readline

LINE = 5

MATH =[]
SCIENCE = []
TOTAL = []

for idx in range(0,LINE):
    math, science = map(int,input().strip().split())
    MATH.append([math,idx+1])
    SCIENCE.append([science,idx+1])
    TOTAL.append([math+science,idx+1])

SORT_KEY=int(input().strip())

# print(MATH)
# print(SCIENCE)
# print(TOTAL)

MATH.sort(reverse=True)
SCIENCE.sort(reverse=True)
TOTAL.sort(reverse=True)

# print(MATH)
# print(SCIENCE)
# print(TOTAL)


print_result = []
if SORT_KEY ==1:
    for I in range(0,len(MATH)):
        score,idx= MATH[I]
        print_result.append(idx)
if SORT_KEY ==2:
    for I in range(0,len(SCIENCE)):
        score,idx= SCIENCE[I]
        print_result.append(idx)
if SORT_KEY ==3:
    for I in range(0,len(TOTAL)):
        score,idx= TOTAL[I]
        print_result.append(idx)


print(' '.join(map(str, print_result)))