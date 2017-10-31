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

def check(a, b):
  g = gcd(a, b)
  a /= g
  b /= g
  i = 2
  while (a != 1 or b != 1) and g != 1 and i <= g:
    if g % i == 0:
      g = remove_factor(g, i)
      a = remove_factor(a, i)
      b = remove_factor(b, i)
    i += 1
  return (a == 1 and b == 1)

def solution(a, b):
  ret = 0
  z = len(a)
  for i in range(z):
    ret += check(a[i], b[i])
  return ret
