MAX = 1000000000

def solution(m, a):
  n = len(a)
  chklst = [0] * (m + 1)

  chklst[a[0]] = 1
  p = 0
  q = 0
  cnt = 0
  distinct = True
  while p < n:
    while distinct:
      cnt += q - p + 1
      if cnt > MAX:
        return MAX
      q += 1
      if q == n:
        return cnt
      chklst[a[q]] += 1
      if chklst[a[q]] == 2:
        distinct = False
    while not distinct:
      if chklst[a[p]] == 2:
        distinct = True
      chklst[a[p]] -= 1
      p += 1
  return cnt
