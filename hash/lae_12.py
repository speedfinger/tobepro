import sys
from sre_parse import parse

if sys.platform == "win32":
    sys.stdin = open('lae_12.txt')

input = sys.stdin.readline

strA, strB = input().strip(), input().strip()
if len(strA) > len(strB):
    tmp = strA
    strA = strB
    strB = tmp

strPatternSet = set()
print(f'strA:[{strA}], strB:[{strB}]')

for i in range(len(strA)):
    for j in range(len(strA)-i):
        print(f'strA[j:len(strA)-i]:{strA[j:len(strA)-i]}')
        strList = [0] * 26
        strPattern = ""
        for k in strA[j:len(strA)-i]:
            strList[ord(k) - 97] += 1
        for l in strList:
            strPattern += f'{l}'
        strPatternSet.add(strPattern)

for i in range(len(strA)-len(strB)):
    for j in range(len(strA)-i):
        print(f'strB[j:len(strA)-i]:{strB[j:len(strA)-i]}')
        strList = [0] * 26
        strPattern = ""
        for k in strB[j:len(strA)-i]:
            strList[ord(k) - 97] += 1
        for l in strList:
            strPattern += f'{l}'