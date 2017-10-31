def gcd(n, m):
  a = max(n, m)
  b = min(n, m)
  while b != 0:
    c = a % b
    a = b
    b = c
  return a

def remove_factor(a, b):
  while a % b == 0:
    a /= b
  return a

def solution(a, b):
  ret = 0
  z = len(a)
  for i in range(z):
    l = a[i]
    r = b[i]
    if l == r:
      ret += 1
      continue
    g = gcd(l, r)
    j = 2
    while g != 1 or j * j <= g:
      if g % j == 0:
        g = remove_factor(g, j)
        l = remove_factor(l, j)
        r = remove_factor(r, j)
      j += 1
    if l == 1 and r == 1:
      ret += 1
  return ret
