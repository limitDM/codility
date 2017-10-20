def solution(A):
    l = len(A)

    if l < 3: # range of n starts from 0
        return 0

    A.sort()

    for i in xrange(l-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0
