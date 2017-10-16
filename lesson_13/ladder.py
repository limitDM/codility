def solution(a, b):
  x, y = 1, 1
  l = len(a)
  fibs = [0] * (l + 1)
  for i in xrange(1, l + 1):
    fibs[i] = x
    x, y = x+y % 2 ** 30, x % 2 ** 30

  ret = [0] * l
  for i in xrange(l):
    ret[i] = fibs[a[i]] % 2 ** b[i]

  return ret
  
