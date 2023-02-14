n = []

for _ in range(9): 
    n.append(int(input()))

for i in n:
    for j in n:

        if i != j:
            if i+j == sum(n) - 100:
                n.remove(i)
                n.remove(j)
                break

for i in sorted(n):
    print(i)
