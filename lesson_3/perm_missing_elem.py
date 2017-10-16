def solution(A):
    l = len(A)
    s = (l+1)*(l+2)/2
    for i in A:
        s -= i
    return s
