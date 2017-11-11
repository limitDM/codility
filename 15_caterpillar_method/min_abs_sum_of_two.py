def solution(a):
  n = len(a)
  rt = int(2e9)
  beg = 0
  end = n - 1
  a.sort()
  while (beg < end):
    rt = min(rt, abs(a[beg] + a[end]))
    if (abs(a[beg]) < abs(a[end])):
      end -= 1
    elif (abs(a[beg]) > abs(a[end])):
      beg += 1
    else:
      return 0
  return min(rt, abs(a[beg] + a[end]))
