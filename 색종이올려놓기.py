import sys
input = sys.stdin.readline

n = int(input())

papers = []
dp = [1 for _ in range(n)]

for _ in range(n):
    xys = list(map(int, input().split()))
    papers.append(sorted(xys))

papers.sort()

for i in range(n):
    for j in range(i):
        if papers[i][1] >= papers[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))
