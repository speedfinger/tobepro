"""
https://codepass.co.kr/contest/406#0
먹느냐 먹히느냐



1 1 3 7 8
1 3 6

3 2 2

"""
import sys
sys.stdin = open("./sequence/jnm_6.txt",'r')
input = sys.stdin.readline


TEST_CASE = int(input().strip())
# print(TEST_CASE)

def sol(LIST_A : list,LIST_B: list):
    count =0
    # print(LIST_A)    
    # print(LIST_B)
    a_cursor = 0
    for b_idx in range(0,len(LIST_B)):        
        for a_idx in range(a_cursor, len(LIST_A)):
            if LIST_A[a_idx]>LIST_B[b_idx]:
                # print(f"b value {LIST_B[b_idx]} is greater then a value {LIST_A[a_idx]}")
                # print(f"a_cursor : {a_idx} ~ {len(LIST_A)}")
                a_cursor=a_idx
                count=count+(len(LIST_A)-a_idx)
                # print(f"count: {count}")
                break

    return count


for _ in range(0,TEST_CASE):
    N,M = list(map(int,input().strip().split()))
    LIST_A=list(map(int,input().strip().split()))
    LIST_B=list(map(int,input().strip().split()))

    # print(f"A : {LIST_A}")
    # print(f"B : {LIST_B}")
    # 

    
    LIST_A.sort()
    LIST_B.sort()
    print(sol(LIST_A,LIST_B))
