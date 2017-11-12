def solution(a):
    n = len(a)
    if n == 0:
        return 0
    a = map(abs, a)
    cnts = [0] * (101)
    for i in a:
        cnts[i] += 1
    s = sum(a)
    ub = s // 2
    dm = [-1] * (ub + 1)
    dm[0] = 0
    for i in range(1, 101):
        if cnts[i] < 1:
            continue
        for j in range(ub + 1):
            if dm[j] >= 0:
                dm[j] = cnts[i]
            elif (j >= i and dm[j-i] > 0):
                dm[j] = dm[j-i] - 1
    for i in range(ub, -1, -1):
        if dm[i] >= 0:
            return s - 2 * i
