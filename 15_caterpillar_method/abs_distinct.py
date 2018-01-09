def remove_duplicate(a):
  rt = []
  last = a[0] + 1;
  for i in a:
    if i != last:
      last = i
      rt.append(i)
  return rt

def solution(a):
  a = remove_duplicate(a)
  n = len(a)
  rt = n
  if a[0] >= 0 or a[n - 1] <= 0:
    return rt
  end = n - 1
  beg = 0
  while a[end] >= 0 and a[beg] < 0:
    if - a[beg] < a[end]:
      end -= 1
    elif - a[beg] > a[end]:
      beg += 1
    else:
      end -= 1
      rt -= 1
  return rt
