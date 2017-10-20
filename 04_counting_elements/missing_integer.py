def solution(A):
  n = len(A)
  lst = [0] * (n+2)
  for i in A:
    ind = max(i, 0)
    ind = min(n+1, ind)
    lst[ind] += 1
  for i in xrange(1, n+1):
    if lst[i] == 0:
      return i
  return n+1
