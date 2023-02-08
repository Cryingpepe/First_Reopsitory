import sys

input = sys.stdin.readline
stack = []

n = int(input())

for _ in range(n):

    num = int(input())
    
    
    if num == 0:
        if len(stack) != 0:
            stack.pop()
    else:
        stack.append(num)
    
print(sum(stack))
