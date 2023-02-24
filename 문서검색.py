import sys
input = sys.stdin.readline

while True():
    
    try:
        hole = int(input())
        legos = []

        for i in range(int(input())):
            legos.append(int(input()))
        
        legos.sort()
        
        while (True):
            if(li[start] + li[end] == x):
                print('yes',li[start] , li[end])
                break
            elif(li[start] + li[end] > x):
                end-=1
            elif (li[start] + li[end] < x):
                start+=1
            if(start >= end):
                print('danger')
                break
        else:
            print(sorted(result)[0])
    except:
        None