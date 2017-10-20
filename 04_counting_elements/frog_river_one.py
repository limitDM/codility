def solution(x, A):
    lst = [0] * x
    cnt = x
    l = len(A)
    for i in xrange(l):
        ind = A[i] - 1
        if lst[ind] == 0:
            lst[ind] = 1
            cnt -= 1
        if cnt == 0:
            return i
    return -1
