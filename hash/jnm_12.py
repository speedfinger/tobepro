"""
구간 성분
https://codepass.co.kr/contest/406/problem/12?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4IjoxMX0=


sliding 하는 방법을 dfs, bfs구현하는거 익숙해졌듯이,,
숙지 할 필요가 있다..

# set 공통 element만 추출
common_set = a_set.intersection(b_set)


#배열을 문자열로 연결
result = ''.join(map(str, DNA))

"""
import sys

sys.stdin = open('./hash/jnm_12.txt')
input = sys.stdin.readline

A_STR = input().strip()
B_STR = input().strip()


# print(A_STR)
# print(B_STR)


# db = [0]*27
# print(db)

def save_db(some_str:str,db):
    # db = [0]*27
    # for i in range(0,len(some_str)):
    #     some_charater = some_str[i]
    #     # print(f"{some_str[i]} : {type(some_str[i])}")
    #     print(f"{some_charater} : {chr(some_charater)}")
    for s in some_str:
        idx = ord(s)-97
        # print(f"{s} : {ord(s)}, idx: {idx}")
        

        db[idx]=db[idx]+1

def probe(idx,STR):
    # print(f"idx:{idx}")
    len_A=len(STR)

    db=set()
    DNA=[0]*26

    for i in range(0,len_A-idx+1):
        
        
        # print(f"{i}:{STR[i:idx+i]}")
        if i==0:
            # print("save db")
            
            save_db(STR[i:idx+i],DNA)
            # print("save end ")
            # print(db)
            result = ''.join(map(str, DNA))
            # print(result)
            db.add(result)

            
        else:
            pre_char = STR[i-1]
            post_char = STR[idx+i-1]
            pre_db_idx=ord(pre_char)-97
            post_db_idx=ord(post_char)-97
            # print(f"i : {i} , pre_char:{pre_char}:{pre_db_idx}, post_char:{post_char}:{post_db_idx}")
            # print(f"befre: {DNA}")
            DNA[pre_db_idx]=DNA[pre_db_idx]-1
            DNA[post_db_idx]=DNA[post_db_idx]+1
            result = ''.join(map(str, DNA))
            db.add(result)
            
            # print(f"after : {DNA}")
            # print("modify db")
    return db
        

    print(db)
    print("@@@@@@@")
        


for idx in range(min(len(A_STR),len(B_STR)),-1,-1):
    # print(idx)
    a_set = probe(idx,A_STR)
    b_set = probe(idx,B_STR)
    # print(a_set)
    # print(b_set)

    common_set = a_set.intersection(b_set)
    if common_set:
        print(f"{idx}")
        break
