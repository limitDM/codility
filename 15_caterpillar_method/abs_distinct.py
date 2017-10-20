def solution(a):
  n = len(a)

  if a[0] >=0 or a[n-1] <= 0:
    last_seen = a[0]
    cnt = 1
    for i in xrange(1, n):
      if a[i] != last_seen:
        cnt += 1
        last_seen = a[i]
    return cnt
    
  beg = 0
  end = n-1
    
  
  while beg <= end:
    mid = (beg + end) / 2
    if a[mid] >= 0:
      center = mid
      end = mid - 1
    else:
      beg = mid + 1

  beg = 0
  end = n-1
  last_seen = max(-a[beg], a[end])
  cnt = 1

  while end >= center:
    while -a[beg] >= a[end]:
      if -a[beg] != last_seen:
        last_seen = -a[beg]
        cnt += 1
      beg += 1
    if a[end] != last_seen:
      last_seen = a[end]
      cnt += 1
    end -= 1
  while beg < center:
    if -a[beg] != last_seen:
      last_seen = -a[beg]
      cnt += 1
    beg += 1
  return cnt
