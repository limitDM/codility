def mul_triple(A, a, b, c):
    return A[a] * A[b] * A[c]

def solution(A):
    l = len(A)

    A.sort()

    candidate = mul_triple(A, -1, -2, -3)

    if A[0] * A[1] > 0:
        return max(candidate,
                   mul_triple(A, 0, 1, -1))
    return candidate
