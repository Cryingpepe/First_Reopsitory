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

    sudokuH = [[],[],[],[],[],[],[],[],[]] # 리스트 초기화

    for j in range(9):                     # H만들기
        for i in range(9):
            sudokuH[i].append(sudokuW[j][i])

    for i in sudokuH:                     # H뺴기
        if i.count(0) == 1:
            i[i.index(0)] = 45 - sum(i)
    
    if 0 not in [i for i in sudokuH]:
        end += 1

    sudokuW = [[],[],[],[],[],[],[],[],[]] # 리스트 초기화

    for i in range(3):                     # S만들기 
        for j in range(3):
            sudokuS[i].append(sudokuH[j][0:2])
            sudokuS[i+3].append(sudokuH[j+3][3:5])
            sudokuS[i+6].append(sudokuH[j+6][6:8])
    
    for i in sudokuH:                     # S뺴기
        if i.count(0) == 1:
            i[i.index(0)] = 45 - sum(i)

    if 0 not in [i for i in sudokuS]:
        end += 1

    sudokuS = [[],[],[],[],[],[],[],[],[]] # 리스트 초기화

    for j in range(9):                     # W만들기 - 미완
        for i in range(9):
            sudokuW[i].append(sudokuH[j][i])


result = ""

for i in range(9):
    for j in range(9):
        result += str(sudokuW[i][j]) + " "
    result += "\n"

print (result)
