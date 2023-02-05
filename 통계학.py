listofn = []
howmanyns = {}

n = int(input())

for i in range(n):
    a = int(input())
    listofn.append(a)
    if str(a) in howmanyns.keys():
        howmanyns[str(a)] += 1
    else:
        howmanyns[str(a)] = 1

listofn.sort()

print(int(sum(listofn) / len(listofn)))

print(listofn[int(len(listofn)/2)])

# if list(howmanyns.values()).count((list(howmanyns.values())).index(max(list(howmanyns.values())))) > 1:
#     print()
# else:
print(list(howmanyns.keys())[(list(howmanyns.values())).index(max(list(howmanyns.values())))])

print(abs(max(listofn) - min(listofn)))

