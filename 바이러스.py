N = int(input()) # Number of computer
NumofCon = int(input()) # Number of connections

ListofVic = ['1'] # List of Victim
ListofUninf = [] # List of Uninfected

for i in range(NumofCon):

    a,b = input().split()

    if a in [x for x in ListofVic]:
        if b in ListofVic:
            continue
        ListofVic += b

    elif b in [x for x in ListofVic]:
        if a in ListofVic:
            continue
        ListofVic += a

    else:
        ListofUninf.append([str(a),str(b)])

for i in ListofVic:
    for x in ListofUninf:
        if i == x[0]:
            ListofVic += x[1]
        elif i == x[1]:
            ListofVic += x[0]

print(len(ListofVic)-1)
