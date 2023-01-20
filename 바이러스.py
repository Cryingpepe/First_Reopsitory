N = int(input()) # Number of computer
NumofCon = int(input()) # Number of connections

ListofVic = ['1'] # List of Victim
ListofUninf = [] # List of Uninfected

for i in range(NumofCon):

    a,b = input().split()

    if a in [x for x in ListofVic]:
        if b in ListofVic:
            continue
        ListofVic.append(str(b))

    elif b in [x for x in ListofVic]:
        if a in ListofVic:
            continue
        ListofVic.append(str(a))

    else:
        ListofUninf.append([str(a),str(b)])

for x in ListofUninf:
    if x[0] in ListofVic:
        if x[1] in ListofVic:
            continue
        ListofVic.append(str(x[1]))
    elif x[1] in ListofVic:
        if x[0] in ListofVic:
            continue
        ListofVic.append(str(x[0]))

print(len(ListofVic)-1)
