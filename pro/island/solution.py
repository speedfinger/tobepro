"""

"""

"""
Parameters​
N : 섬의 한 변의 길이 (5 ≤ N ≤ 20)
land : 섬의 각 지역의 고도 (1 ≤ land[][] ≤ 5)
"""

from collections import defaultdict
key_map = defaultdict()


"""


# """

land_map = list
result = defaultdict(list)
map_size = 0
def init(N, land):
    global map_size
    map_size = N
    global land_map
    land_map = land
    global result
    temp_result = defaultdict(list)
    
    for block_size in range(1, 6):
        for i in range(N):
            for j in range(N - block_size + 1):
                # 가로 방향 블록의 값 추출
                block = land[i][j:j + block_size]
                min_value = min(block)
                block_value = ''.join(str(x - min_value) for x in block)
                rotated_block_value = ''.join(str(x - min_value) for x in block[::-1])  # 180도 회전
                
                # 원본 순서와 회전된 순서 모두 추가
                temp_result[block_value].append((i, j, '가로', 0))
                if block_value != rotated_block_value:
                    temp_result[rotated_block_value].append((i, j, '가로', -1))
                
        # 세로 방향 탐색 (블록 사이즈가 1일 때는 가로, 세로가 같으므로 중복을 피함)
        if block_size > 1:
            for i in range(N - block_size + 1):
                for j in range(N):
                    # 세로 방향 블록의 값 추출
                    block = [land[i + k][j] for k in range(block_size)]
                    min_value = min(block)
                    block_value = ''.join(str(x - min_value) for x in block)
                    rotated_block_value = ''.join(str(x - min_value) for x in block[::-1])  # 180도 회전
                    
                    # 원본 순서와 회전된 순서 모두 추가
                    temp_result[block_value].append((i, j, '세로', 0))
                    if block_value != rotated_block_value:
                        temp_result[rotated_block_value].append((i, j, '세로', -1))
    
    result = temp_result
    return temp_result
 

def key_from_structure(li):  # 검색시(건축물): list 가장 큰 값에서 각각의 값을 빼고 문자열 연결
    maxv = max(li)

    # ex) [3,2,3,1] -> (0,1,0,2)
    # return tuple(map(lambda x: maxv - x, li))

    # ex) [3,2,3,1] -> ['0','1','0','2'] -> '0102'
    return ''.join(map(lambda x: str(maxv - x), li))
def getCount(M, structure):
    global result
    # structure의 각 원소에서 최소값을 빼는 방식으로 key 생성
    # min_value = min(structure[:M])  # M개의 요소 중에서 최소값을 찾음

    key = key_from_structure(structure[0:M])
    
    # result에서 해당 key에 대한 리스트의 크기를 반환
    return len(result[key])

from collections import deque

def getMaxArea(M, structure, seaLevel):
    global land_map
    land = land_map
    N = len(land)
    
    # 1. result 함수에서 설치 가능한 좌표를 가져옴
    # key = ''.join(map(str, structure[:M]))  # 구조물의 첫 M 개를 key로 만듬
    key = key_from_structure(structure[:M])
    possible_locations = result.get(key, [])

    if len(possible_locations) ==0:
        return -1
    
    
    # 2. 구조물을 설치하는 함수 정의
    def install_structure(land, locations, structure, M):
        new_land = [row[:] for row in land]  # land 맵을 복사
        
        for (i, j, direction, rotation) in locations:

            if rotation == -1:
                # print(f"sturcture reveresed : {structure}")
                structure = structure[::-1]  # 180도 회전 (배열을 뒤집음)
                # print(f"sturcture reveresed : {structure}")
            if direction == '가로':
                for k in range(M):
                    new_land[i][j + k] = new_land[i][j + k]+ structure[k]
            elif direction == '세로':
                for k in range(M):
                    new_land[i + k][j] = new_land[i + k][j] + structure[k]
        
        return new_land
    
    # 3. 해수면 이하의 블록을 0으로 만드는 BFS 함수 정의
    def flood_fill_bfs(land, seaLevel):
        visited = [[False] * N for _ in range(N)]
        queue = deque()
        
        # 바깥 테두리부터 시작
        for i in range(N):
            if land[i][0] < seaLevel and not visited[i][0]:
                queue.append((i, 0))
                visited[i][0] = True
            if land[i][N - 1] < seaLevel and not visited[i][N - 1]:
                queue.append((i, N - 1))
                visited[i][N - 1] = True
        for j in range(N):
            if land[0][j] < seaLevel and not visited[0][j]:
                queue.append((0, j))
                visited[0][j] = True
            if land[N - 1][j] < seaLevel and not visited[N - 1][j]:
                queue.append((N - 1, j))
                visited[N - 1][j] = True
        
        # BFS로 인접한 해수면 이하의 영역을 0으로 변경
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
        while queue:
            x, y = queue.popleft()
            land[x][y] = 0  # 잠기면 0으로 설정
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if land[nx][ny] < seaLevel:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
    
    # 4. 해수면 이상인 블록 개수 계산 함수 정의
    def count_above_sea_level(land):
        global map_size
        count = 0

        for i in range(map_size):
            for j in range(map_size):
                if land[i][j] > 0:
                    count += 1
        return count
    
    max_area = 0
    
    # 5. 설치 가능한 각 위치에 대해 구조물 설치 후 해수면 높이에 따른 블록 수를 계산
    for location in possible_locations:
        land = land_map

        
        new_land = install_structure(land, [location], structure[:M], M)
        
        flood_fill_bfs(new_land, seaLevel)
        
        # 해수면보다 높은 블록의 수를 카운트
        area = count_above_sea_level(new_land)
        
        # 최대 영역을 갱신
        max_area = max(max_area, area)
    
    return max_area


"""
1. 각 테스트 케이스 시작 시 init() 함수가 호출된다.
2. 각 테스트 케이스에서 getcount() 함수의 호출 횟수는 150,000 이하이다.
3. 각 테스트 케이스에서 getMaxArea() 함수의 호출 횟수는 50 이하이다.
4. 각 테스트 케이스에서 getMaxArea() 함수의 구조물 structure를 설치할 수 있는 경우의 수의 총합은 5,000 이하이다.


"""