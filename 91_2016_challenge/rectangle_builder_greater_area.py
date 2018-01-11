def bisearch(x, l):
  n = len(l)
  beg = 0
  end = n - 1
  rt = -1
  while beg <= end:
    mid = (beg + end) // 2
    if l[mid] < x:
      beg = mid + 1
    else:
      end = mid - 1
      rt = mid
  return rt

def preprocess(a):
  a.append(-1)
  n = len(a)
  rt1 = []
  rt2 = []
  last = a[0]
  cnt = 1
  for i in range(1, n):
    if a[i] == last:
      cnt += 1
    else:
      if cnt > 1:
        rt1.append(last)
        rt2.append(min(1, cnt // 2 - 1))
      last = a[i]
      cnt = 1
  return rt1, rt2

def solution(a, x):
  a.sort()
  l1, l2 = preprocess(a)
  n = len(l1)
  rt = 0
  for i in range(n):
    target = bisearch(x // l1[i] + (x % l1[i]) * 1, l1)
    if target == -1:
      continue
    elif target <= i:
      rt += n - i - 1 + l2[i]
    else:
      rt += n - target
    if rt > 1000000000:
      return -1
  return rt
