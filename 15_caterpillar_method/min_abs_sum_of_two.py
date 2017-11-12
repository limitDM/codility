def solution(a):
  n = len(a)
  rt = int(2e9)
  beg = 0
  end = n - 1
  a.sort()
  while (beg < end):
    rt = min(rt, abs(a[beg] + a[end]))
    if -a[beg] == a[end]:
      return 0
    elif abs(a[beg]) < abs(a[end]):
      end -= 1
    else:
      beg += 1
  return min(rt, abs(a[beg] + a[end]))
