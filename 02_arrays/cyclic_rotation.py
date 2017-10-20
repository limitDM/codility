def solution(A, K):
    try:
        K %= len(A)
    except:
        K = 0
    return A[-K:] + A[:-K]
