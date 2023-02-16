n = int(input())

result = []

for i in range(1, n + 1):
    chart = [n]
    chart.append(i)

    current = 1

    while(1):
        nextnumber = chart[current - 1] - chart[current]

        if nextnumber < 0:
            break

        chart.append(nextnumber)

        current += 1

    if len(result) < len(chart):
        result = chart

print(len(result))
for i in result:
    print(i, end=" ")
