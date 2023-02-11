import sys
n  = int(input())
nlist =  list(map(int,(sys.stdin.readline().split())))
new = []
maxpoint = max(nlist)

for i in nlist:
    new.append((i/maxpoint)*100)

print(sum(new)/n)
