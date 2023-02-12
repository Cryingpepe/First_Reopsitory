import sys
input = sys.stdin.readline

n = int(input())
sortedlist = []

for _ in range(n):
    a, b = map(int, input().split())
    sortedlist.append([a, b])

sortedlist.sort()

for i, j in sortedlist:
    print(i, j)
