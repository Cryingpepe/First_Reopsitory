#first upload

def solution(A):
    result = []
    for i in A[:-1]:
        profit = max(A[A.index(i)+1:]) - i
        if profit > 0:
            result.append(profit)
    
    if len(result)==0:
        return 0
    
    return max(result)

print(solution( [23171, 21011, 21123, 21366, 21013, 21367])) # Test case should print 356
