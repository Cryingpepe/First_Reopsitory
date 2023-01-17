N = int(input())
x = input()
    
def solver(ps):

    stack = 0
    maxstack = 0


    for i in ps:

        if i == '(':
            stack += 1

            if stack > maxstack:
                maxstack = stack

        else:
            stack -= 1

    stack = 0


    for i in ps:

        if i == ')':
            stack += 1

            if stack > maxstack:
                maxstack = stack

        else:
            stack -= 1

    print(maxstack)

if N % 2 == 1:
    print(-1)      
elif x.count('(') != x.count(')'):
    print(-1)      
else:
    solver(x)
