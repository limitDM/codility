def check(val, k, a):
  this = 0;
  for i in a:
    if i > val:
      return 0
    this += i
    if (this > val):
      k -= 1
      this = i
  return k > 0

def solution(k, m, a):
  n = len(a)
  beg = 0
  end = m * n
  rt = -1
  while beg <= end:
    mid = (beg + end) / 2
    if check(mid, k, a):
      end = mid - 1
      rt = mid;
    else:
      beg = mid + 1
  return rt
