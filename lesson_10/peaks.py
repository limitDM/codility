def solution(a):
  def next_divisor(i):
    i += 1
    while i <= n:
      if n % i == 0:
        return i
      else:
        i += 1
    return 0

  def find_blocks(i):
    for j in xrange(n/i):
      cnt = 0
      for k in xrange(i):
        cnt += b[j * i + k]
      if cnt == 0:
        return 0
    return n/i

  n = len(a)

  b = [0] * n
  for i in xrange(1, n-1):
    if a[i] - a[i-1] > 0 and a[i+1] - a[i] < 0:
      b [i] = 1

  ret = 0
  i = next_divisor(0)
  while i != 0:
    ret = find_blocks(i)
    if ret != 0:
      return ret
    i = next_divisor(i)
  return 0
