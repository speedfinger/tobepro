
"""
M : 구조물의 크기 (1 ≤ M ≤ 5)
structure : 구조물의 각 부분의 높이 (1 ≤ structure[] ≤ 5)

return 구조물을 설치할 수 있는 경우의 수

고도가 올라간 이후에는, M개 지역의 고도가 모두 일치해야만 한다.
일치하지 않을 것으로 예상될 때에는, 구조물을 설치할 수 없다.
구조물은 시계 방향으로 90도, 180도, 270도만큼 회전시킬 수 있다.


설치할 수 있는 경우를 저장하고, 이때 getMaxArea에서 호출해서 사용할 수 있게 저장해줘, 
저장하는 자료형은 getcount(*)가 150,000까지 호출될 수 있다는 점을 유의해서 getMaxArea가 저장된 자료형을 탐색할때 timecompexity가 높지 않게 고려해줘

"""

"""
아래의 기능을 하는 def getCount(M, structure) 를 만들어줘
structure는 리스트이고 M은 structur에서 [0:M] 으로 리스트에서 key로 바꾸면 돼

def init(N, land) 에서 초기화 했던 defaultdict 인 result에서 structur[0:M] 의 key에 해당하는 리스트의 사이즈를 반환하는 함수를 만들어줘
"""
# def getCount(M, structure):
#     global result
#     # structure에서 0:M까지의 부분 리스트를 키로 만듦
#     key = ''.join(map(str, structure[:M]))
    
#     # result에서 해당 key에 대한 리스트의 크기를 반환
#     getcount_result = len(result[key])
#     print(result)
#     print(f"key: {key}, getcount_result : {getcount_result}")
#     return getcount_result
 
"""
structure 을 가지고 검색할 key를 만드는 방법을 바꿀께 
예를 들어 structure가 434으로 들어오면, 121 으로 바꿔서 defaultdict에서 검색해줘
"""

def key_from_structure(li):  # 검색시(건축물): list 가장 큰 값에서 각각의 값을 빼고 문자열 연결
    maxv = max(li)

    # ex) [3,2,3,1] -> (0,1,0,2)
    # return tuple(map(lambda x: maxv - x, li))

    # ex) [3,2,3,1] -> ['0','1','0','2'] -> '0102'
    return ''.join(map(lambda x: str(maxv - x), li))