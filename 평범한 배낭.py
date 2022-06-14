#https://www.acmicpc.net/problem/12865          (https://www.acmicpc.net/workbook/view/4349)

Numofstf, maxweight = map(int,input().split())
listofstf =[]
currentstf = []

currentw, currentv = 0, 0

while Numofstf > 0:
    a, b = map(int,input().split())
    listofstf.append([a,b])
    Numofstf -= 1

for i in listofstf:
    if currentw + i[0] <= maxweight:
        currentw += i[0]
        currentv += i[1]
        currentstf.append(i)
    else:
        for x in currentstf:
            if (i[0] <= x[0] and i[1] > x[1]) or (i[1] == x[1] and i[0] < x[0]):
                x[0], x[1] = i[0], i[1]
            else:
                break

print(currentv)
#본질적으로 잘못되어서 처음부터 바꿔야 할것 
#찾아보니 냅색 알고리즘 이라고 한다
