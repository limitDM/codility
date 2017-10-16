def solution(a):
  n = len(a)
  a.sort()

  beg = 0
  end = n-1

  center = None
  while beg <= end:
    mid = (beg + end) / 2

    if a[mid] <= 0:
      center = mid
      beg = mid + 1
    else:
      end = mid - 1

  if center == None:
    return 2 * a[0]
  elif center == n-1:
    return -2 * a[-1]
  else:
    left = center
    right = center + 1
    ret = a[right] - a[left]
    while right < n:
      while left >= 0 and -a[left] < a[right]:
        left -= 1
      ret = min(ret,
                min(abs(a[right] + a[left]),
                    abs(a[right] + a[left + 1])))
      right += 1
  return ret
