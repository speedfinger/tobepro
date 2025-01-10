
"""
Parameters​
M : 구조물의 크기 (1 ≤ M ≤ 5)
structure : 구조물의 각 부분의 높이 (1 ≤ structure[] ≤ 5)
seaLevel : 해수면의 상승 폭 (1 ≤ seaLevel ≤ 10)

Returns​
최대 지역 개수

 해수면이 seaLevel만큼 상승하여도 바다에 잠기지 않고 남아있는 지역의 개수가
최대가 되도록 구조물 structure를 1개 설치했을 때, 그 개수를 반환한다.
구조물 structure를 설치할 방법이 없는 경우에는, -1을 반환
"""

"""
def getMaxArea(M, structure, seaLevel, land): 함수는

land는 아래 형태의 N*N의 맵 지형이야.
1 2 1 5 5 5 
3 1 3 1 1 5 
1 4 5 5 5 5 
2 1 1 1 4 5 
1 4 5 5 5 5 
3 2 3 4 1 2

M : 구조물의 크기 (1 ≤ M ≤ 5)
structure : 구조물의 각 부분의 높이 (1 ≤ structure[] ≤ 5)
이고 seaLevel : 해수면의 상승 폭 (1 ≤ seaLevel ≤ 10) 이야.

이때 앞에서 이미 구현했던 result 함수에서 result[key]로 설치할 수 있는 좌표 목록을 받아와서
예) M은 2 structure가 [1,4,0,0,0] 이면 key는: 03로 변환해서서 설치가능한 좌표 목록을 result[key]로 받아오면 아래와 같이 받아올 수 있어어
좌표 목록 예) [(2, 0, '가로', 2),
                    (3, 3, '가로', 2),
                    (4, 0, '가로', 2),
                    (5, 3, '가로', 2),
                    (1, 1, '세로', 2),
                    (2, 1, '세로', 2),
                    (3, 1, '세로', 2),
                    (4, 5, '세로', 2)],

설치가능한 각 좌표에 구조물을 설치하고 난 다음 높이를 기준으로 , 해수면높이(seaLevel) 보다 
예를 들어 2,1 가로로 설치 하면

1 2 1 5 5 5 
3 1 3 1 1 5 
1 4 5 5 5 5 
2 1 1 1 4 5 
1 4 5 5 5 5 
3 2 3 4 1 2
에서

1 2 1 5 5 5 
3 1 3 1 1 5 
1 5 5 5 5 5 
2 5 1 1 4 5 
1 4 5 5 5 5 
3 2 3 4 1 2
가 돼, 이 때 해수면 높이가 5라고 한다면
5보다 같거나 높은블럭으로 쌓여있는 아래 블럭들(0으로 바뀌지 않은) 의 갯수 (18) 를 계산해서
설치가능한 블럭위치 중 해수면으로 0이 되지 않는 블럭들이 최대가 될때의 갯수를 리턴하는 함수를 만들어줘줘

0 0 0 5 5 5 
0 0 0 0 0 5 
0 5 5 5 5 5 
0 5 1 1 4 5 
0 0 5 5 5 5 
0 0 0 0 0 0
================================================================================================================================

def getMaxArea(M, structure, seaLevel, land):
    N = len(land)
    
    # 1. result 함수에서 설치 가능한 좌표를 가져옴 (예시로 M=2 구조물일 경우)
    key = ''.join(map(str, structure[:M]))  # 구조물의 첫 M 개를 key로 만듬
    possible_locations = result.get(key, [])
    
    # 2. 구조물을 설치하는 함수 정의
    def install_structure(land, locations, structure, M):
        new_land = [row[:] for row in land]  # land 맵을 복사
        
        for (i, j, direction, size) in locations:
            if direction == '가로':
                for k in range(M):
                    new_land[i][j + k] = structure[k]
            elif direction == '세로':
                for k in range(M):
                    new_land[i + k][j] = structure[k]
        
        return new_land
    
    # 3. 해수면 위의 블록 개수 계산 함수 정의
    def count_above_sea_level(land, seaLevel):
        count = 0
        for i in range(N):
            for j in range(N):
                if land[i][j] >= seaLevel:
                    count += 1
        return count
    
    max_area = 0
    
    # 4. 설치 가능한 각 위치에 대해 구조물 설치 후 해수면 높이에 따른 블록 수를 계산
    for location in possible_locations:
        new_land = install_structure(land, [location], structure, M)
        area = count_above_sea_level(new_land, seaLevel)
        max_area = max(max_area, area)
    
    return max_area


"""

"""
count_above_sea_level 가 잘못됐어 
단순히 모든 좌표에대해서 검색하는게 아니라 
가장 테두리의 좌표들로 부터 bfs또는 dfs 탐색을 하면서 , 해수면으로 잠기는 곳은 0으로 인접한 곳이 해수면으로 잠기지 않으면 끝나면 돼


from collections import deque

def getMaxArea(M, structure, seaLevel, land):
    N = len(land)
    
    # 1. result 함수에서 설치 가능한 좌표를 가져옴
    key = ''.join(map(str, structure[:M]))  # 구조물의 첫 M 개를 key로 만듬
    possible_locations = result.get(key, [])
    
    # 2. 구조물을 설치하는 함수 정의
    def install_structure(land, locations, structure, M):
        new_land = [row[:] for row in land]  # land 맵을 복사
        
        for (i, j, direction, size) in locations:
            if direction == '가로':
                for k in range(M):
                    new_land[i][j + k] = structure[k]
            elif direction == '세로':
                for k in range(M):
                    new_land[i + k][j] = structure[k]
        
        return new_land
    
    # 3. 해수면 이하의 블록을 0으로 만드는 BFS 함수 정의
    def flood_fill_bfs(land, seaLevel):
        visited = [[False] * N for _ in range(N)]
        queue = deque()
        
        # 바깥 테두리부터 시작
        for i in range(N):
            if land[i][0] <= seaLevel and not visited[i][0]:
                queue.append((i, 0))
                visited[i][0] = True
            if land[i][N - 1] <= seaLevel and not visited[i][N - 1]:
                queue.append((i, N - 1))
                visited[i][N - 1] = True
        for j in range(N):
            if land[0][j] <= seaLevel and not visited[0][j]:
                queue.append((0, j))
                visited[0][j] = True
            if land[N - 1][j] <= seaLevel and not visited[N - 1][j]:
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
                    if land[nx][ny] <= seaLevel:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
    
    # 4. 해수면 이상인 블록 개수 계산 함수 정의
    def count_above_sea_level(land, seaLevel):
        count = 0
        for i in range(N):
            for j in range(N):
                if land[i][j] > seaLevel:
                    count += 1
        return count
    
    max_area = 0
    
    # 5. 설치 가능한 각 위치에 대해 구조물 설치 후 해수면 높이에 따른 블록 수를 계산
    for location in possible_locations:
        new_land = install_structure(land, [location], structure, M)
        
        # 해수면 이하의 영역을 0으로 처리
        flood_fill_bfs(new_land, seaLevel)
        
        # 해수면보다 높은 블록의 수를 카운트
        area = count_above_sea_level(new_land, seaLevel)
        
        # 최대 영역을 갱신
        max_area = max(max_area, area)
    
    return max_area


"""

"""
    def install_structure(land, locations, structure, M):
        new_land = [row[:] for row in land]  # land 맵을 복사
        
        for (i, j, direction, rotation) in locations:
            if direction == '가로':
                for k in range(M):
                    new_land[i][j + k] = new_land[i][j + k]+ structure[k]
            elif direction == '세로':
                for k in range(M):
                    new_land[i + k][j] = new_land[i + k][j] + structure[k]
        
        return new_land

이 함수를 rotation 이 0일때와 -1(180도 회전)으로 구분해줘 

================================================================================================
def install_structure(land, locations, structure, M):
    new_land = [row[:] for row in land]  # land 맵을 복사
    
    for (i, j, direction, rotation) in locations:
        if direction == '가로':
            if rotation == 0:
                # 구조물을 원래 순서대로 설치 (가로)
                for k in range(M):
                    new_land[i][j + k] = new_land[i][j + k] + structure[k]
            elif rotation == -1:
                # 구조물을 180도 회전하여 설치 (가로)
                for k in range(M):
                    new_land[i][j + k] = new_land[i][j + (M - 1 - k)] + structure[k]
        
        elif direction == '세로':
            if rotation == 0:
                # 구조물을 원래 순서대로 설치 (세로)
                for k in range(M):
                    new_land[i + k][j] = new_land[i + k][j] + structure[k]
            elif rotation == -1:
                # 구조물을 180도 회전하여 설치 (세로)
                for k in range(M):
                    new_land[i + k][j] = new_land[i + (M - 1 - k)][j] + structure[k]
    
    return new_land

================================================================================================
아니 회전하는걸 structure기준으로 바꿔줘
================================================================================================

def install_structure(land, locations, structure, M):
    new_land = [row[:] for row in land]  # land 맵을 복사
    
    for (i, j, direction, rotation) in locations:
        # 회전 여부에 따라 structure 배열을 변경
        if rotation == -1:
            structure = structure[::-1]  # 180도 회전 (배열을 뒤집음)
        
        if direction == '가로':
            for k in range(M):
                new_land[i][j + k] = new_land[i][j + k] + structure[k]
        
        elif direction == '세로':
            for k in range(M):
                new_land[i + k][j] = new_land[i + k][j] + structure[k]
    
    return new_land


"""