def solution(A):
  n = len(A)
  lst = [0] * (n + 1)
  for i in A:
    ind = min(i, n + 1)
    lst[ind-1] += 1
  for i in lst[:-1]:
    if i == 0:
      return 0
  return 1
