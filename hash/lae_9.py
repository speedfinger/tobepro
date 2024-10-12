import sys

if sys.platform == "win32":
    sys.stdin = open('lae_9.txt')

input = sys.stdin.readline

N = int(input())
map = dict()
preFixMap = set()

for _ in range(N):
    word = input().strip()
    if len(map) == 0:
        for n in range(1, len(word)+1):
            preFixMap.add(word[0:n])
        print(f'{word[0:1]}')
        map[word] = 1
    else:
        if word in map:
            map[word] += 1
            print(f'{word}{map[word]}')
        else:
            map[word] = 1
            preFix = ""
            for n in range(1, len(word)+1):
                if word[0:n] in preFixMap and  n != len(word):
                    continue
                elif word[0:n] in map and  n != len(word):
                    continue
                else:
                    preFixMap.add(word[0:n])
                    if preFix == "":
                        preFix = word[0:n]
                if n == len(word) and preFix == "":
                    preFix = word+str(map[word])
            print(preFix)