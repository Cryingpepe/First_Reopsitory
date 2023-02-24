string = input()
finding = input()

count = 0
ls = 0

while len(string) - len(finding) >= ls:
    if string[ls:ls + len(finding)] == finding:
        count += 1
        ls += len(finding)
        
    else:
        ls += 1

print (count)