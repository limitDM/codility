def gcd(n, m):
  a = max(n, m)
  b = min(n, m)
  while b != 0:
    c = a % b
    a = b
    b = c
  return a

def solution(n, m):
  g = gcd(n, m)
  return n / g
