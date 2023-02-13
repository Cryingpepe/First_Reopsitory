import sys
input = sys.stdin.readline

def DFS(V):
    global DFS_result

    check[V] = 1
    DFS_result += str(V) + " "

    for i in range(1, n + 1):
        if check[i] == 0 and links[V][i] == 1:
            DFS(i)

def BFS(V):
    global BFS_result

    queue = [V]

    while len(queue):
        
        V = queue.pop(0) # 큐의 첫번째 ()
        check[V]= 1
        BFS_result += str(V) + " "

        for i in range(1, n + 1):
            if check[i] == 0 and links[V][i] == 1:
                queue.append(i)
                check[i] = 1

n, m, v = map(int, input().split())
DFS_result = ""
BFS_result = ""

links = [[0] * (n + 1) for _ in range(n + 1)] # 인접 행렬 생성 - https://sarah950716.tistory.com/12
check = [0] * (n + 1) # 방문 여부 확인

for _ in range(m):
    a, b = map(int, input().split())
    links[a][b] = 1
    links[b][a] = 1

DFS(v)
check = [0] * (n + 1) # 방문 여부 리셋
BFS(v)

print(DFS_result)
print(BFS_result)
