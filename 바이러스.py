N = int(input()) # Number of computer
NumofCon = int(input()) # Number of connections

ListofCon = [] # List of connections
ListofVic = [1] # List of Victim

for i in range(NumofCon):
    if input().split() in [a for a in ListofVic] :
        ListofVic += input().split()

print (ListofVic)
