def bisearch(x, l):
  n = len(l)
  beg = 0
  end = n - 1
  rt = -1
  while beg <= end:
    mid = (beg + end) // 2
    if l[mid] >= x:
      rt = mid
      end = mid - 1
    else:
      beg = mid + 1
  return rt

def preprocess(a):
  a.append(-1)
  n = len(a)
  elts = []
  one_pair = []
  last = a[0]
  cnt = 1
  for i in range(1, n):
    if a[i] == last:
      cnt += 1
    else:
      if cnt >= 2:
        elts.append(last)
        one_pair.append(cnt < 4)
      last = a[i]
      cnt = 1
  return elts, one_pair

def solution(a, x):
  a.sort()
  distinct_elts, one_pair = preprocess(a)
  n = len(distinct_elts)
  rt = 0
  for i in range(n):
    target = x // distinct_elts[i] + (x % distinct_elts[i] != 0)
    target_pos = bisearch(target, distinct_elts)
    if target_pos == -1:
      continue
    elif target_pos <= i:
      rt += n - i - one_pair[i]
    else:
      rt += n - target_pos
    if rt > 1000000000:
      return -1
  return rt
