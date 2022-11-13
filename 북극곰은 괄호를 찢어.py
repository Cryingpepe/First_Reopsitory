import sys
sys.setrecursionlimit(10**6)

N = int(input())
x = input()
counts = 0  
    
def solver(ps):
    global counts
    
    if len(ps) == 0:
        print (counts)
        exit()
    
    listofps = [x for x in ps.split('()')]

    rest = ''
    
    for i in listofps:
        rest += i
        
    listofps = [x for x in rest.split(')(')]

    rest = ''
    
    for i in listofps:
        rest += i
        
    counts += 1
    
    solver(rest)
    
if N % 2 == 1:
    print(-1)      
elif x.count('(') != x.count(')'):
    print(-1)      
else:
    solver (x)
