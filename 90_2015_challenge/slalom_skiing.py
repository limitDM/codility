def lis(a):
  n = len(a)
  if n < 2:
    return n
  b = [None] * n
  b[0] = a[0]
  rt = 1
  for i in a[1:]:
    end = rt - 1
    beg = 0
    point = -1
    while beg <= end:
      mid = (beg + end) // 2
      if b[mid] <= i:
        point = mid
        beg = mid + 1
      else:
        end = mid - 1
    if point + 1 == n:
      return n
    elif b[point + 1] == None:
      rt += 1
      b[point + 1] = i
    else:
      b[point + 1] = min(b[point + 1], i)
  return rt

def preprocess(a):
  b = []
  m = max(a)
  for i in a:
    b.append(2 * m + i)
    b.append(2 * m - i + 1)
    b.append(i)
  return b

def solution(a):
  n = len(a)
  b = preprocess(a)
  rt = min(lis(b), n)
  return rt
