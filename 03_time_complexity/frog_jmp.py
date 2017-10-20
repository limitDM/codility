def solution(X, Y, D):
    remainder = (Y-X) % D
    quotient = (Y-X) // D
    if remainder:
        return quotient + 1
    else:
        return quotient
