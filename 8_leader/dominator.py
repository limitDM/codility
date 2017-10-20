def solution(A):
  n = len(A)
  size = 0

  #find candidate
  for i in xrange(n):
    if size == 0:
      val = A[i]
      size = 1
    elif val == A[i]:
      size += 1
    else:
      size -= 1

  #verify candidate
  cnt = 0
  for i in xrange(n):
    if val == A[i]:
      loc = i
      cnt += 1
  if cnt > n // 2:
    return loc
  else:
    return -1
