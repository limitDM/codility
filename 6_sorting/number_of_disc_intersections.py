def solution(a):
  n = len(a)
  left_ends = []
  right_ends = []

  for i in xrange(n):
    left_ends.append(i - a[i])
    right_ends.append(i + a[i])

  left_ends.sort()
  right_ends.sort()

  cnt = -1
  ind = 0
  ret = 0

  for rpt in right_ends:
    while ind < n and left_ends[ind] <= rpt:
      cnt += 1
      ind += 1
    ret += cnt
    if ret > 10000000:
      return -1
    cnt -= 1

  return ret
