#https://www.acmicpc.net/problem/20044
NofT = int(input())

listofmember = []
listofmember += list(map(int, input().split()))
listofmember.sort()

result = []

for x in range(NofT):
    result.append(listofmember.pop()+listofmember.pop(0))

print (min(result))
