def solution(A):
    lefts = ['(', '{', '[']
    rights =  [')', '}', ']']

    stack = []

    for i in A:
        if i in lefts:
            stack.append(i)
        else:
            j = rights.index(i)
            try:
                now = stack.pop()
            except:
                return 0
            if now != lefts[j]:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
