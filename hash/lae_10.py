import sys

if sys.platform == "win32":
    sys.stdin = open('lae_10.txt')

input = sys.stdin.readline

N, Q = map(int, input().split())
landMap = dict()
playerScore = [0, 0, 0, 0]

# {(1,1): 1} / {1: 10}

for n in range(Q):
    player = n%4
    r, c = map(int, input().split())
    if (r, c) in landMap:
        opponent = landMap[(r,c)]
        # print(f'({r}, {c}) --> {opponent+1}, player: {player+1} // score: {playerScore[opponent]}, {playerScore[player]}')
        if opponent == player:
            landMap.pop((r, c))
            playerScore[player] -= 1
        elif opponent != player:
            if playerScore[opponent] > playerScore[player]:
                landMap[(r, c)] = player
                playerScore[player] += 1
                playerScore[opponent] -= 1
    else:
        # print(f'({r}, {c}) --> X')
        landMap[(r, c)] = player
        playerScore[player] += 1
    # print(f'[{playerScore[0]}, {playerScore[1]}, {playerScore[2]}, {playerScore[3]}]')

for cnt in playerScore:
    print(cnt)