def count_pairs(l):
  n = len(l)
  rt = 0
  i = 1
  while i < n:
    if l[i - 1] == l[i]:
      rt += 1
      i += 1
    i += 1
  return rt

def remove_pairs(l):
  l.append(None)
  n = len(l)
  rt = []
  i = 1
  while i < n:
    if l[i] == l[i - 1]:
      i += 1
    else:
      rt.append(l[i - 1])
    i += 1
  return rt

def solution(k, c, d):
  c.sort()
  d.sort()
  clean_pairs = count_pairs(c)
  c = remove_pairs(c)
  n = len(c)
  
  pointer = 0
  rt = clean_pairs
  remainder = []
  for i in d:
    if k == 0:
      break
    while pointer < n and c[pointer] < i:
      pointer += 1
    if pointer < n and c[pointer] == i:
      rt += 1
      k -= 1
      pointer += 1
    else:
      remainder.append(i)
  dirty_pairs = count_pairs(remainder)
  if k // 2 > 0:
    rt += min(k // 2, dirty_pairs)
  return rt
