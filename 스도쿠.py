sudokuW = []
sudokuH = [[],[],[],[],[],[],[],[],[]]
for i in range(9):
    sudokuW.append(input().split())

for i in sudokuW:
    for j in range(9):
        if i.count("0") == 1:
            i[i.index("0")] = str(j)

for j in range(9):
    for i in range(9):
        sudokuH[i].append(sudokuW[j][i])

for i in sudokuH:
    for j in range(9):
        if i.count("0") == 1:
            i[i.index("0")] = str(j)

print(sudokuH)

