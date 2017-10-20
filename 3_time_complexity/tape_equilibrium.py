def solution(A):
    pdiff = A[0]-sum(A[1:])
    result = abs(pdiff)
    
    l = len(A)
    for i in xrange(1, l-1):
        pdiff += 2 * A[i]
        result = min(result, abs(pdiff))
    return result
