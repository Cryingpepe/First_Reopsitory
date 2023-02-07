import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = input()
    stack = []

    for i in string:
        if i == "(":
            stack.append(i)
        if i == ")":
            if len(stack) == 0:
                stack.append(i)
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
    
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
