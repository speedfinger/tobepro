import sys

if sys.platform == "win32":
    sys.stdin = open('lae_11.txt')

input = sys.stdin.readline

k = int(input())
str = input()
strLen = len(str)

subStrDict = dict()
cnt = 0

# [A,C,G,T]
# [0,0,0,0]
def convertArray(str):
    arr = [0,0,0,0]
    for chr in str:
        if chr == "A":
            arr[0] += 1
        elif chr == "C":
            arr[1] += 1
        elif chr == "G":
            arr[2] += 1
        elif chr == "T":
            arr[3] += 1
    return f'{arr[0]}{arr[1]}{arr[2]}{arr[3]}'

for i in range(strLen-k+1):
    # print(f'sub: {str[i:i+3]}')
    subStr = convertArray(str[i:i+k])
    # print(subStr)
    if subStr in subStrDict:
        subStrDict[subStr] += 1
    else:
        subStrDict[subStr] = 1

for i in subStrDict:
    cnt = max(subStrDict[i], cnt)

print(cnt)

