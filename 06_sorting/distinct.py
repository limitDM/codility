def solution(A):
    l = len(A)
    if l == 0:
        return 0
    
    A.sort()

    cnt = 1
    for i in xrange(1, l):
        if A[i-1] != A[i]:
            cnt += 1
    return cnt
