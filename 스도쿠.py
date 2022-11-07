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

    for j in range(0,9):                     # H만들기
        for i in range(0,9):
            sudokuH[i].append(sudokuW[j][i])

    for i in sudokuH:                     # H뺴기
        if i.count(0) == 1:
            i[i.index(0)] = 45 - sum(i)
    
    if 0 not in [i for i in sudokuH]:
        end += 1

    sudokuW = [[],[],[],[],[],[],[],[],[]] # W리스트 초기화

    for j in range(0,3):
        sudokuS[0]+=sudokuH[j][0:3]
        sudokuS[3]+=sudokuH[j][3:6]
        sudokuS[6]+=sudokuH[j][6:9]
        sudokuS[1]+=sudokuH[j+3][0:3]
        sudokuS[4]+=sudokuH[j+3][3:6]
        sudokuS[7]+=sudokuH[j+3][6:9]
        sudokuS[2]+=sudokuH[j+6][0:3]
        sudokuS[5]+=sudokuH[j+6][3:6]
        sudokuS[8]+=sudokuH[j+6][6:9]
    
    for i in sudokuH:                     # S뺴기
        if i.count(0) == 1:
            i[i.index(0)] = 45 - sum(i)

    if 0 not in [i for i in sudokuS]:
        end += 1

    sudokuH = [[],[],[],[],[],[],[],[],[]] # H리스트 초기화

    for i in range(9):                     # W만들기 - 미완
        for j in range(9):
            sudokuW[i]+=sudokuS[::3][i::3]
            sudokuW[i+3]+=sudokuS[1::3][i::3]
            sudokuW[i+6]+=sudokuS[2::3][i::3]

result = ""

for i in range(9):
    for j in range(9):
        result += str(sudokuW[i][j]) + " "
    result += "\n"

print (result)
