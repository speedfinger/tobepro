"""
hash : 땅점령게임
https://codepass.co.kr/contest/406/problem/10?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4Ijo5fQ==

key를 좌표 xy를 붙힌 str로 처리해서 누가 소유한건지 갱신
dict["N-1""N-1"] = A

본인이 소유한거면, None 처리
다른사람이 소유한거면 cnt 비교
최종 cnt 출력

remember@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
remember1) key를 만들때
map_key=f"{x}{y}"로 처리했는데 이런 경우 x,y 조합에 따라 다른 좌표가 같은 key가 되버리는 경우가 발생할 수 있음
map_key=f"{x},{y}" 로 변경후 solve

remember2)
dict = {}
dict.pop('key') 가 가능함.

"""

import sys 
sys.stdin = open('./hash/jnm_10.txt')

input = sys.stdin.readline

map_db={}

map_size, play_count = list(map(int,input().split()))
# print(map_size)
# print(play_count)
player_score = [0,0,0,0]
for idx in range(0,play_count):
    current_player=idx%4
    # print(player)

    x, y= list(map(str,input().split()))
    map_key=f"{x},{y}"
    # print(map_key)

    #한번도 방문하지 않은 key
    if map_key not in map_db:
        map_db[map_key]=current_player
        player_score[current_player]=player_score[current_player]+1
        
    #그외: key가 점유된 상황일 경우
    else:
        before_palyer = map_db[map_key]

        #본인 key인 경우
        if before_palyer==current_player:
            map_db.pop(map_key)
            player_score[current_player]=player_score[current_player]-1
            # print(map_db)
            # print(player_score)
            continue


        # print(f"{before_palyer} has {map_key} map with score : {player_score[before_palyer]} and current score : {player_score[current_player]}")
        # 기존 땅을 차지하고 있던 palyer 점수보다 신규 플레이어 점수보다 작으면 주인 change
        if player_score[before_palyer]>player_score[current_player]:
            map_db[map_key]=current_player

            #기존 주인 count --
            player_score[before_palyer]=player_score[before_palyer]-1
            #새로운 주인 count++
            player_score[current_player]=player_score[current_player]+1
        

        pass

    # print(map_db)
    # print(player_score)
for idx in range(0,4):
    print(player_score[idx])