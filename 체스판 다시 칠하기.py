#https://www.acmicpc.net/problem/1018
y, x = map(int ,input().split())

map = []

for i in range(y):
    map.append(input())

for i in range(0,x-7):
    for j in range(0,y-7):
        map[i][j:j+7].count("W")
        map[i][j:j+7]

print(map)
