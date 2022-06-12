#https://www.acmicpc.net/problem/12865

Numofstf, maxweight = map(int,input().split())
listofstf =[]

while Numofstf > 0:
    a, b = map(int,input().split())
    listofstf.append([a,b])
    Numofstf -= 1

for i in listofstf:
    totalw, totalv = 0, 0
    while maxweight =< totalw:
