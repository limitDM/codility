"""
room
0 1
2 3
courdinate as binary number
"""

def find_coordinate(pos, n):
  row = int(pos[:-1]) - 1
  col = int(ord(pos[-1]) - ord('A'))
  return 2 * (row >= n // 2) + (col >= n // 2)

def preprocess(n, s, t):
  side = n // 2
  init = side * side
  vacancy = [init] * 4
  weights = [0] * 4
  for i in s:
    vacancy[find_coordinate(i, n)] -= 1
  for i in t:
    coor = find_coordinate(i, n)
    vacancy[coor] -= 1
    weights[coor] += 1
  return vacancy, weights

def rowsum(m, i):
  pos = 2 * i
  return m[pos] + m[pos ^ 1]

def colsum(m, i):
  pos = i
  return m[pos] + m[pos ^ 2]

def summary(m):
  return colsum(m, 0), colsum(m, 1), rowsum(m, 0), rowsum(m, 1)

def check_balance(w):
  c0, c1, r0, r1 = summary(w)
  return r0 == r1, c0 == c1

def candidate(w):
  c0, c1, r0, r1 = summary(w)
  return 2 * (r0 > r1) + (c0 > c1)

def extra(v):
  return 2 * min(v[0], v[3]) + 2 * min(v[1], v[2])

def balancing(v, w):
  cnt = 0
  rowbal, colbal = check_balance(w)
  while not (rowbal and colbal):
    c = candidate(w)
    if v[c] == 0:
      return -1
    else:
      v[c] -= 1
      w[c] += 1
      cnt += 1
    rowbal, colbal = check_balance(w)
  return cnt + extra(v)
      
def solution(n, s, t):
  s = s.split()
  t = t.split()
  vacancy, weights = preprocess(n, s, t)
  rt = balancing(vacancy, weights)
  return rt
