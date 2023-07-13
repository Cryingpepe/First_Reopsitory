#https://www.acmicpc.net/problem/1157

import sys
input = sys.stdin.readline

cnt = [0 for _ in range(26)]

#getting sentence
sentence = input().strip().upper()

for i in sentence:
    cnt[ord(str(i))-65] += 1

result = max(cnt)

if cnt.count(result) > 1:
    print('?')
else:
    print(chr(cnt.index(result)+65))
