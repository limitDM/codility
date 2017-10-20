def solution(s, p, q):
  m = len(p)
  a = prefix_count(s, 'A')
  c = prefix_count(s, 'C')
  g = prefix_count(s, 'G')
  ret = []
  for i in xrange(m):
    start = p[i]
    end = q[i] + 1
    if a[end] - a[start] > 0:
      ret.append(1)
    elif c[end] - c[start] > 0:
      ret.append(2)
    elif g[end] - g[start] > 0:
      ret.append(3)
    else:
      ret.append(4)
  return ret

def prefix_count(s, char):
  n = len(s)
  ret = [0] * (n + 1)
  cnt = 0
  for i in xrange(n):
    if s[i] == char:
      cnt += 1
    ret[i+1] = cnt
  return ret
