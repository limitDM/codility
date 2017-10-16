def solution(a):
  n = len(a)
  appearance = [0] * (2 * n + 1)
  for i in a:
    appearance[i] += 1

  distinct_elts = set(a)

  non_divisors = [0] * (2 * n + 1)

  non_divisors[1] = n - appearance[1]

  for i in distinct_elts:
    if i == 1:
      continue
    div_cnt = n - appearance[1] - appearance[i]
    j = 2
    while j * j < i:
      if i % j == 0:
        div_cnt -= appearance[j] + appearance[i / j]
      j += 1
    if j * j == i:
      div_cnt -= appearance[j]
    non_divisors[i] = div_cnt

  ret = [0] * n

  i = 0
  for i in xrange(n):
    ret[i] = non_divisors[a[i]]

  return ret
