def solution(A):
    a = 0
    for i in A:
        a ^= i
    return a
