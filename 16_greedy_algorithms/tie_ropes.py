def solution(k, a):
  n = len(a)

  tied = 0
  cnt = 0
  for i in xrange(n):
    tied += a[i]
    if tied >= k:
      cnt += 1
      tied = 0

  return cnt
