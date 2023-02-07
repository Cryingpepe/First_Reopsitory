import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    command = ""
    command += input()
    
    if "push" in command:
        x = command.split()
        stack.append(x[1])

    elif "pop" in command:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print('-1')

    elif "size" in command:
        print(len(stack))
    
    elif "empty" in command:
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    
    elif "top" in command:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print('-1')
