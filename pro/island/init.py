"""
1 2 1 5 5 5 
3 1 3 1 1 5 
1 4 5 5 5 5 
2 1 1 1 4 5 
1 4 5 5 5 5 
3 2 3 4 1 2
이런 형태의 N*N 의 형태를 받는 def init(N, land) 함수에서
1부터 5개단위로 블럭을 만들면서서 가로방향,세로방향을 검색하면서 가장작은 값을 각 요소에서 뺀 값들을 key값으로 가지고 value는 리스트인데, 블럭의 시작점과 가로방향,세로방향인지를 저장하는 defaultdict를 만드는 함수로 만들어줘
예를 들어 3개단위로 블럭에 대한 defaultdict를 만들때때 
0,0 가로방향 3개 는 1 2 1 이고 key는 121가 되고 value는 [(0,0,가로)]가 되는거야
0,0 세로방향 3개는 1 3 1 이고 key는 131가 되고 value는 [(0,0,세로)]가 돼
0,1 가로방향 3개 는 2 1 5 이고 key는 215 , 512가 되고 value는 [0,1,가로]가 돼

==================================================================================================

result = defaultdict(list)
def init(N, land):
    
    global result
    for block_size in range(1, 6):
        for i in range(N):
            for j in range(N - block_size + 1):
                # 가로 방향 블록의 값 추출
                block = land[i][j:j + block_size]
                min_value = min(block)
                block_value = ''.join(str(x - min_value) for x in block)
                result[block_value].append((i, j, '가로', block_size))
                
        # 세로 방향 탐색 (블록 사이즈가 1일 때는 가로, 세로가 같으므로 중복을 피함)
        if block_size > 1:
            for i in range(N - block_size + 1):
                for j in range(N):
                    # 세로 방향 블록의 값 추출
                    block = [land[i + k][j] for k in range(block_size)]
                    min_value = min(block)
                    block_value = ''.join(str(x - min_value) for x in block)
                    result[block_value].append((i, j, '세로', block_size))
    from pprint import pprint
                
    pprint(result)
    return result

여기에서 추가적으로 가로, 세로 180도 회전에 대한 질문으로 코드를 좀 더 수정해서 solution.py 코드가 최종
"""