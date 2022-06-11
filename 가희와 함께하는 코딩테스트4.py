#first problem

#문제
#메이플스토리 몬스터는 방어율 수치가 있습니다. 이 방어율 수치의 일정 %를 무시하는 것을 방무라고 합니다. 유저는 아이템을 사거나, 특정한 스킬 레벨을 올려서 방무 수치를 올릴 수 있습니다. 그렇게 해서, 유저가 체감하는 몬스터의 방어율 수치를 낮출 수 있습니다. 몬스터의 방어율이 200이고, 유저의 방무가 20이라면, 몬스터의 방어율 200의 20%를 무시하게 되므로, 40만큼 무시하게 됩니다. 즉, 160이 유저가 체감하는 방어율 수치가 됩니다.

#유저가 체감하는 몬스터의 방어율 수치가 100보다 크거나 같으면 몬스터에게 대미지를 줄 수 없습니다. 몬스터의 방어율 수치를 a, 유저의 방무를 b라고 할 때, 유저가 몬스터에게 대미지를 줄 수 있는지 없는지 알려주세요.  

#입력
#첫 번째 줄에 정수 a와 b가 공백으로 구분되어 주어집니다.

#출력
#몬스터에게 대미지를 줄 수 있으면 1, 그렇지 않으면 0을 출력해 주세요.

#answer

a, b = input().split()
if int(a) - int(a)*(int(b)/100) >= 100:
    print ('0')
else:
    print('1')
    
#second problem (https://www.acmicpc.net/problem/25239)

#answer

ClockH, ClockM = input().split(':')
ClockH = int(ClockH)
ClockM = int(ClockM)
HealingP = list(input().split())
for i in HealingP:
    HealingP[HealingP.index(i)] = int(i)
NumofEvent = int(input())
Evt = []
while NumofEvent > 0:
    a = input()
    Evt.append(a)
    NumofEvent -= 1

Clocksection = 0 

if 0 <= ClockH < 2:
    Clocksection = 0
elif 2 <= ClockH < 4:
    Clocksection = 1
elif 4 <= ClockH < 6:
    Clocksection = 2
elif 6 <= ClockH < 8:
    Clocksection = 3
elif 8 <= ClockH < 10:
    Clocksection = 4
else:
    Clocksection = 5

for i in Evt:
    a, b = i.split()

    if float(a) > 60:
        break

    if '^' in i:
        HealingP[Clocksection] = 0

    else:
        if 'MIN' in b:
            ClockM += int(b[0:2])
        if 'HOUR' in b:
            ClockH += int(b[0])
            
        if ClockM >= 60:
            ClockH += 1
            ClockM -= 60
        if ClockH >= 12:
            ClockH -= 12

        if 0 <= ClockH < 2:
            Clocksection = 0
        elif 2 <= ClockH < 4:
            Clocksection = 1
        elif 4 <= ClockH < 6:
            Clocksection = 2
        elif 6 <= ClockH < 8:
            Clocksection = 3
        elif 8 <= ClockH < 10:
            Clocksection = 4
        elif 10 <= ClockH < 12:
            Clocksection = 5

    if sum(HealingP) == 0:
        break

        
if sum(HealingP) > 100:
    print('100')
else:
    print(sum(HealingP))
    
#third problem (https://www.acmicpc.net/problem/25240)

#answer

NofUser, NofFile = input().split()
NofUser = int(NofUser)
NofFile = int(NofFile)
dictofinfo = {}
dictofbook = {}
Task = []

while NofUser > 0:
    a = input().split()
    if len(a) > 1:
        dictofinfo[a[0]] = a[1].split(',')
    else:
        dictofinfo[a[0]] = ''
    NofUser -= 1

while NofFile > 0:
    a = input().split()
    dictofbook[a[0]] = a[1:]
    NofFile -= 1

NofTask = int(input())

while NofTask > 0 :
    a = input().split()
    Task.append(a)
    NofTask -= 1


