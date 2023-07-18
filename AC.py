import sys

input = sys.stdin.readline

t = int(input().strip("\n"))

for _ in range(t):

    cmd = input().strip("\n")
    lenth = str(input().strip("\n"))
    arr = input().strip('\n')
    flag = True


    if arr != '[]':
        arr = arr.strip('[]')
        arr = list(map(int, arr.split(',')))
    else:
        arr = ''

    try:
        for i in cmd:
            if i == 'D':
                if len(arr) == 0:
                    raise                   
                elif flag:
                    del arr[0]
                else:
                    del arr[-1]
            else:
                flag = not flag

    
        if flag:
            if arr == '' or len(arr) == 0:
                print('[]')
            else:
                print('[',end='')
                print(*arr, sep=",",end='')
                print(']')
        else:
            if arr == '' or len(arr) == 0:
                print('[]')
            else:
                arr.reverse()
                print('[',end='')
                print(*arr, sep=",",end='')
                print(']')
    except:
        print('error')
