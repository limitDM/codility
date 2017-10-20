def solution(n, p, q):
  prime_check = [0] * 2 + [1] * (n - 1)
  i = 2
  while i * i <= n:
    if prime_check[i] == 1:
      j = 2
      while i * j < n + 1:
        prime_check[i * j] = 0
        j += 1
    i += 1

  semiprime_check = [0] * (n + 1)
  i = 2
  while i < n + 1:
    if prime_check[i] == 0:
      i += 1
      continue
    j = i
    while j < n + 1:
      if prime_check[j] == 0:
        j += 1
        continue
      elif i * j > n:
        break
      else:
        semiprime_check[i * j] = 1
      j += 1
    i += 1

  prefix_count = [0] * (n + 1)
  i = 0
  cnt = 0
  while i < n + 1:
    cnt += semiprime_check[i]
    prefix_count[i] = cnt
    i += 1

  m = len(p)
  ret = []
  for i in xrange(m):
    ret.append(prefix_count[q[i]] - prefix_count[p[i]-1])
  return ret
