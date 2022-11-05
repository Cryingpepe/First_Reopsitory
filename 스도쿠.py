# https://www.acmicpc.net/problem/2580
sudokuW = []
sudokuH = [[],[],[],[],[],[],[],[],[]]
sudokuS = [[],[],[],[],[],[],[],[],[]]
end = 0

for i in range(9):
    sudokuW.append(list(map(int, input().split())))

while end == 0:

    for i in sudokuW:                     # W뺴기
        if i.count(0) == 1:
            i[i.index(0)] = 45 - sum(i)
    
    if 0 not in [i for i in sudokuW]:
        end += 1

    sudokuS = [[],[],[],[],[],[],[],[],[]] # S리스트 초기화

    for j in range(0,8):                     # H만들기
        for i in range(0,8):
            sudokuH[i].append(sudokuW[j][i])

    for i in sudokuH:                     # H뺴기
        if i.count(0) == 1:
            i[i.index(0)] = 45 - sum(i)
    
    if 0 not in [i for i in sudokuH]:
        end += 1

    sudokuW = [[],[],[],[],[],[],[],[],[]] # W리스트 초기화

    for i in range(0,2):                     # S만들기 
        for j in range(0,2):
            sudokuS[i].append(sudokuH[j][1:3])
            sudokuS[i+3].append(sudokuH[j+3][4:6])
            sudokuS[i+6].append(sudokuH[j+6][7:9])
    
    for i in sudokuH:                     # S뺴기
        if i.count(0) == 1:
            i[i.index(0)] = 45 - sum(i)

    if 0 not in [i for i in sudokuS]:
        end += 1

    sudokuH = [[],[],[],[],[],[],[],[],[]] # H리스트 초기화

    for i in range(9):                     # W만들기 - 미완
        for j in range(9):
            sudokuW[i].append(sudokuS[::3][i::3])
            sudokuW[i+3].append(sudokuS[1::3][i::3])
            sudokuW[i+6].append(sudokuS[2::3][i::3])




result = ""

for i in range(9):
    for j in range(9):
        result += str(sudokuW[i][j]) + " "
    result += "\n"

print (result)
