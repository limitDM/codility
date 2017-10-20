def check(A, B, cnts):
  N = len(A)
  i = 0
  for i in xrange(N):
    if cnts[B[i]] - cnts[A[i] - 1] == 0:
      return 0
  return 1

def solution(A, B, C):
  M = len(C)
  N = len(A)

  beg = 1
  end = M

  ret = -1

  while beg <= end:
    mid = (beg + end) / 2
    nails = [0] * (2 * M + 1)
    for i in C[:mid]:
      nails[i] = 1

    cnt = 0
    cnts = [0] * (2 * M + 1)
    i = 0
    while i < 2 * M + 1:
      if nails[i] == 1:
        cnt += 1
      cnts[i] = cnt
      i += 1
      
    if check(A, B, cnts):
      ret = mid
      end = mid - 1
    else:
      beg = mid + 1

  return ret
