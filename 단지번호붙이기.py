import sys

n = int(input())

maplist = []
houses = []
result = 0

def DFS(x, y):
    global result

    if x < 0 or x >= n or y < 0 or y >= n:
        return None
    
    if maplist[x][y] == 1:
        result += 1
        maplist[x][y] = 0

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            DFS(a, b)

for _ in range(n):
    maplist.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for i in range(n):
    for j in range(n):
        if maplist[i][j] == 1:
            DFS(i, j)
            houses.append(result)
            result = 0

print(len(houses))

for i in sorted(houses):
    print(i)
