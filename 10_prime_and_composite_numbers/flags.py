def peak_gaps(a):
  ret = []
  cnt = 0
  for i in range(1, len(a) - 1):
    cnt += 1;
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
      ret += [cnt]
      cnt = 0
  return ret

def solution(a):
  n = len(a)
  pgaps = peak_gaps(a)
  m = len(pgaps)
  flags = 0
  
  while flags < m and flags * (flags + 1) < n:
    flags += 1

  if flags < 3:
    return flags

  for k in range(flags, 2, -1):
    remained = k - 1
    step = 0
    for i in range(1, m):
      step += pgaps[i]
      if (step >= k):
        step = 0
        remained -= 1
        if remained == 0:
          return k
  return k
