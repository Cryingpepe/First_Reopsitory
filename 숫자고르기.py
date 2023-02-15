import sys
input = sys.stdin.readline

n = int(input())

chart = [[i, 0] for i in range(n + 1)]

for i in range(1, n+1):
    chart[i][1] = int(input())

result1 = []
result2 = []
answer = []

visited = [0 for _ in range(n + 1)]

def DFS(i):
    global result1
    global result2
    global visited
    
    if visited[i] == 0:
        visited[i] = 1

        result1.append(chart[i][0])
        result2.append(chart[i][1])
        DFS(chart[i][1])
    else:
        for i in range(n):
            if sorted(result1) == sorted(result2):
                for i in sorted(result1):
                    if i not in answer:
                        answer.append(i)

        result1 = []
        result2 = []
        visited = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i not in answer:
        DFS(i)

print(len(answer))
for i in sorted(answer):
    print(i)
