def solution(a, b):
  n = len(b)

  last = -1
  cnt = 0
  for i in xrange(n):
    if a[i] > last:
      cnt += 1
      last = b[i]
  return cnt
