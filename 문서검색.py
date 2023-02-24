import sys
input = sys.stdin.readline

while True():
    
    try:
        hole = int(input())
        legos = []
        result = []

        for i in range(int(input())):
            legos.append(int(input()))
        
        legos.sort()
        
        for i in legos:
            legos.remove(i)
            if (hole*10000000 - i) in legos:
                if i > hole - i:
                    result.append("yes " + str(hole*10000000 - i) + " " + str(i))
                    legos.remove(hole*10000000 - i)
                else:
                    result.append("yes " + str(i) + " " + str(hole*10000000 - i))
                    legos.remove(hole*10000000 - i)

        if len(result) == 0:
            print('danger')
        else:
            print(sorted(result)[0])
    except:
        None