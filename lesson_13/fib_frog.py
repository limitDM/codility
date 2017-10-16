def solution(a):
  n = len(a)

  fibs = [0] * (2 * n + 2)

  f1, f2 = 1, 1
  i = 0
  while f1 < n+2:
    fibs[i] = f1
    f1, f2 = f1+f2, f1
    i += 1
  fibs[i] = f1

  steps = [n+2] * (n + 1)

  for i in xrange(n+1):
    min_step = n+2
    f = fibs[0]
    j = 0
    while f < i+1:
      if a[i-f]:
        min_step = min(min_step, steps[i-f] + 1)
      j += 1
      print j
      f = fibs[j]
    if i-f == -1:
      steps[i] = 1
    else:
      steps[i] = min_step
  if steps[n] == n+2:
    return -1
  else:
    return steps[n]
