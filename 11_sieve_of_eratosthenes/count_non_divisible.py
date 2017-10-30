def elt_counter(a):
  n = len(a)
  ret = [0] * (2 * n + 1)
  for i in a:
    ret[i] += 1
  return ret

def solution(a):
  n = len(a)
  elt_cnts = elt_counter(a)
  non_divs = [n] * (2 * n + 1)
  ret = []

  for i in range(2 * n + 1):
    if elt_cnts[i] != 0:
      j = 1
      while (i * j < 2 * n + 1):
        if elt_cnts[i * j] != 0:
          non_divs[i * j] -= elt_cnts[i]
        j += 1

  for i in range(n):
    ret += [non_divs[a[i]]]

  return ret
