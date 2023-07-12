https://www.acmicpc.net/problem/10809

S = str(input())

for i in range(26):

    if S.find(chr(97+i)) != -1: #a의 아스키코드 활용
        print(S.find(chr(97+i)), end=" ")
    else:
        print(-1, end=" ")
