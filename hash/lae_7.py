import sys

if sys.platform == "win32":
    sys.stdin = open('lae_7.txt')

input = sys.stdin.readline

N =  int(input())
s = set()
cnt = 0
for _ in range(N):
    word = input().strip()
    if word in s:
        s.remove(word)
        cnt -= 1
    else:
        s.add(word)
        cnt += 1

print(cnt)