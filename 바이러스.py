N = int(input()) # Number of computer
NumofCon = int(input()) # Number of connections

ListofVic = [1] # List of Victim
ListofUninf = [] # List of Uninfected

for i in range(NumofCon):

    a,b = map(int, input().split())

    if a in ListofVic:
        if b in ListofVic:
            continue
        ListofVic.append(b)

    elif b in ListofVic:
        if a in ListofVic:
            continue
        ListofVic.append(a)

    else:
        ListofUninf.append([a,b])



for x in ListofUninf and ListofUninf[::-1]:

    while x[:] in ListofVic:

        if x[0] in ListofVic:
            if x[1] in ListofVic:
                continue
            else:
             ListofVic.append(x[1])


        elif x[1] in ListofVic:
            if x[0] in ListofVic:
                continue
            else:
                ListofVic.append(x[0])

        else:
            continue
    

print(len(ListofVic)-1)
