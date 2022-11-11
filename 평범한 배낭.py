#https://www.acmicpc.net/problem/12865          (https://www.acmicpc.net/workbook/view/4349)

#https://velog.io/@na0ngkim/%EB%83%85%EC%83%89knapsack-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B0%EB%82%AD-%EB%AC%B8%EC%A0%9C-%EB%B0%B1%EC%A4%80-12865-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%AD-%ED%8C%8C%EC%9D%B4%EC%8D%AC

Numofstf, maxweight = map(int,input().split())

listofstf = []
result = [[0 for i in range(maxweight+1)] for j in range(Numofstf+1)]


for i in range(Numofstf):
    listofstf.append(list(map(int,input().split())))

for i in range(1,Numofstf+1):
    for j in range(1,maxweight+1):
        if j < listofstf[i][0]:
            result[i][j] = listofstf[i-1][1]
        




print (valueofstf)

#찾아보니 냅색 알고리즘 이라고 한다
