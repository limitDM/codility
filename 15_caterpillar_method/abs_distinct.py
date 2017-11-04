def remove_duplicate(a):
  rt = []
  last = a[0] + 1;
  for i in a:
    if i != last:
      last = i
      rt.append(i)
  return rt

def search_smallest_nonnegative(a):
  n = len(a)
  end = n-1
  beg = 0
  while (beg <= end):
    mid = (beg + end) / 2
    if (a[mid] >= 0):
      rt = mid
      end = mid -1
    else:
      beg = mid + 1
  return rt
  
def solution(a):
  a = remove_duplicate(a)
  n = len(a)
  rt = n
  if a[0] >=0 or a[n-1] <= 0:
    return rt
  end = search_smallest_nonnegative(a);
  beg = end - 1
  while beg >= 0 and end < n:
    if - a[beg] < a[end]:
      beg -= 1
    elif - a[beg] > a[end]:
      end += 1
    else:
      end += 1
      rt -= 1
  return rt
