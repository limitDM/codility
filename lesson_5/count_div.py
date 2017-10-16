def solution(A, B, K):
    remainder = A%K
    if remainder:
        ret = B/K - A/K
    else:
        ret = B/K - A/K +1
    return ret
