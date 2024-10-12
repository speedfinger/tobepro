import sys

if sys.platform == "win32":
    sys.stdin = open('lae_8.txt')

input = sys.stdin.readline

N = int(input())
map = dict()
nameMap = dict()
id = 0

# {1: name}   {name: (id, score)}

for n in range(N):
    name, score = input().split()
    name = name.lower()
    score = int(score)
    if name in nameMap:
        map[n] = (name, (nameMap[name][0], max(nameMap[name][1], score)))
        nameMap[name] = (nameMap[name][0], max(nameMap[name][1], score))
    else:
        id += 1
        map[n] = (name, (id, score))
        nameMap[name] = (id, score)
    print(f'{nameMap[map[n][0]][0]} {nameMap[map[n][0]][1]}')
