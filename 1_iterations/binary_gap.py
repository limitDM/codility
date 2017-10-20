def solution(N):
    max_len = 0
    length = 0
    remainder = 0
    while remainder != 1:
        remainder = N%2
        N //=2
    while N>0:
        remainder = N%2
        N //= 2
        if remainder == 1:
            max_len = max(max_len, length)
            length = 0
        else:
            length += 1
    return max_len
