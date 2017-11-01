def fib_check(l):
  x, y = 1, 1
  ret = [1]
  for i in xrange(l):
    ret += [x]
    x, y = (x + y) % 2 ** 30, x
  return ret

def solution(a, b):
  l = len(a)
  fibs = fib_check(l)
  ret = []
  for i in xrange(l):
    ret += [fibs[a[i]] % 2 ** b[i]]

  return ret
