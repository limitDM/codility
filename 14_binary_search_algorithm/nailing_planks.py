def check(v, a, b, c):
  n = len(a)
  m = len(c)
  nail_cnts = [0] * (2 * m + 1)
  for i in c[:v]:
    nail_cnts[i] = 1
  for i in range(1, 2 * m + 1):
    nail_cnts[i] += nail_cnts[i - 1]
  for i in range(n):
    if nail_cnts[b[i]] - nail_cnts[a[i] - 1] == 0:
      return 0
  return 1

def solution(a, b, c):
  m = len(c)
  beg = 1
  end = m
  rt = -1
  while beg <= end:
    mid = (beg + end) / 2
    if check(mid, a, b, c):
      rt = mid
      end = mid - 1
    else:
      beg = mid + 1
  return rt
