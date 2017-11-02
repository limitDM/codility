def fib_under(n):
  a = 1
  b = 1
  rt = []
  while a <= n:
    rt.append(a)
    a, b = a + b, a
  return rt

def solution(a):
  a.append(1)
  n = len(a)
  fibs = fib_under(n)
  steps = [n + 2] * n
  for i in range(n):
    if a[i] == 0:
      continue
    for j in fibs:
      if i - j < -1:
        break
      elif i - j == -1:
        steps[i] = 1
      elif steps[i - j] != n + 2:
        steps[i] = min(steps[i], steps[i - j] + 1)
  if steps[-1] == n + 2:
    return -1
  else:
    return steps[-1]
