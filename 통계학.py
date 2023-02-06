import sys
listofn = []
howmanyns = {}

n = int(input())

for i in range(n):
    a = int(sys.stdin.readline())
    listofn.append(a)
    if str(a) in howmanyns.keys():
        howmanyns[str(a)] += 1
    else:
        howmanyns[str(a)] = 1

listofn.sort()

print(round(sum(listofn) / len(listofn)))

print(listofn[int(len(listofn)/2)])

numofmax = list(howmanyns.values()).count(max(list(howmanyns.values())))

listofmax = []

if numofmax == 1:
    print(list(howmanyns.keys())[(list(howmanyns.values())).index(max(list(howmanyns.values())))])
else:
    for key, value in howmanyns.items():
        if value == max(list(howmanyns.values())):
            listofmax.append(key)

    result = []
    for i in listofmax:
        result.append(int(i))

    result.sort()
    print(result[1])

print(abs(listofn[-1] - (listofn[0])))
