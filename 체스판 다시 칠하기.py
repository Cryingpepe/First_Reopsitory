#https://www.acmicpc.net/problem/1018
y, x = map(int ,input().split())

map = []

for i in range(y):
    map.append(input())

result = [] #[[0,0] for q in range((y-7)*(x-7))]

ylist = list(range(0,y))
xlist = list(range(0,x))

isitodd = list(range(1,8,2))

for w in xlist[:x-7]:
    for q in ylist[:y-7]:
        a = 0
        b = 0
        for i in range(0,8):
            words = ['W','B']
            firstword = map[i+q][0+w]
            words.pop(words.index(firstword))
            secondword = words[0]
            if i in isitodd:
                a += map[i+q][0+w:8+w:2].count(secondword)
                a += map[i+q][1+w:8+w:2].count(firstword)
                b += map[i+q][0+w:8+w:2].count(firstword)
                b += map[i+q][1+w:8+w:2].count(secondword)
            else:
                b += map[i+q][0+w:8+w:2].count(firstword)
                b += map[i+q][1+w:8+w:2].count(secondword)
                a += map[i+q][0+w:8+w:2].count(secondword)
                a += map[i+q][1+w:8+w:2].count(firstword)
             

        # print(a,b)
        result.append(min(a,b))

# print(map)
# print(result)
print(min(result))

# 예제 2번 빼고 다 맞는데 뭐가 문제일까
