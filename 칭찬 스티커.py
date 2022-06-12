비버고등학교에서는 아래 규칙에 따라 칭찬 스티커를 발급한다.
- 칭찬 스티커는 평일, 주말에 관계없이 매일 발급한다.
- 각 학생은 1년에 1개의 스티커만 받을 수 있으며, 한 번 스티커를 받으면 다시는 받지 못한다.
- 3월 1일에 학생 중 한 명을 선정하여 칭찬 스티커를 발급한다.
- 칭찬 스티커를 받은 학생은 다음 날 새로운 학생들에게 칭찬 스티커를 발급하는데, 발급하는 날의 날짜가 소수인지 아닌지에 따라 다음과 같이 발급하는 스티커의 개수가 달라진다.
  - 날짜가 소수가 아닌 경우 : 전날 스티커를 발급받은 학생이 2명의 학생에게 스티커를 발급
  - 날짜가 소수인 경우 : 전날 스티커를 발급받은 학생이 3명의 학생에게 스티커를 발급

비버고등학교의 학생이 n명이라고 할 때, 모든 학생이 칭찬 스티커를 받기 위해서 최소 몇 일이 필요할까?
칭찬 스티커 제도는 3월 1일에 처음 시작된다.

def m():
    neededStickers = int(input())
    days = 1
    currentmonth = [3]
    currentstickers = 1
    daycount = 1
    previous = 1

    while currentstickers < neededStickers:
        days += 1
        months = [1, 3, 5, 7, 8, 10, 12]

        prime = [2,3,5,7,11,13,17,19,23,31,29]

        if days in prime:
            currentstickers = currentstickers + (previous*3)
            previous *= 3

        else:
            currentstickers = currentstickers + (previous*2)
            previous *= 2

        if currentmonth[0] not in months:
            if days == 30:
                currentmonth[0] = currentmonth[0]+1
                days = 0
        elif currentmonth[0] == 2:
            if days == 28:
                currentmonth[0] = currentmonth[0]+1
                days = 0
        else:
            if currentmonth[0] == 12 and days == 31:
                currentmonth[0] = 1
                days = 0
            elif days == 31:
                currentmonth[0] = currentmonth[0]+1
                days = 0

        daycount += 1
        
    print(daycount)

m()

#https://codeup.kr/problem.php?id=2329
