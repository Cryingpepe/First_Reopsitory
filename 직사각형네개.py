import sys
input = sys.stdin.readline

chart = [[0 for i in range(100)] for i in range(100)]

for i in range(4):
    x, y, X, Y = map(int, input().split())

    for i in range(x, X):
        for j in range(y, Y):
            chart[i][j] = 1

result = 0

for i in range(100):
    for j in range(100):
        if chart[i][j] == 1:
            result += 1

print (result)
