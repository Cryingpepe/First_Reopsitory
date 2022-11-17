#https://www.acmicpc.net/problem/1018
y, x = map(int ,input().split())

map = []

for i in range(y):
    map.append(input())

result = [] #[[0,0] for q in range((y-7)*(x-7))]

ylist = [i for i in range(0,y)]
xlist = [i for i in range(0,x)]

for w in xlist[:x-7]:
    for q in ylist[:y-7]:
        a = 0
        for i in range(0,8):
            a += map[i+q][0+w:8+w].count("W")
        result.append([a])

for w in xlist[:x-7]:
    for q in ylist[:y-7]:
        b = 0
        for i in range(0,8):
            if max(result)[0] > 32:
                if map[i+q][0] == 'W':
                    b += map[i+q][0+w:8+w:2].count("W")
                    b += map[i+q][1+w:8+w:2].count("B")
                else:
                    b += map[i+q][0+w:8+w:2].count("B")
                    b += map[i+q][1+w:8+w:2].count("W")
            elif max(result)[0] < 32:
                if map[i+q][0] == 'W':
                    b += map[i+q][0+w:8+w:2].count("B")
                    b += map[i+q][1+w:8+w:2].count("W")




print(map)
print(result)
print(abs(max(result)[0]-32))
