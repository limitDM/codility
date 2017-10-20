def solution(n, a):
  max_cnt = 0
  ckpt = 0
  ret = [0] * n
  for i in a:
    if i > n:
      ckpt = max_cnt
    else:
      ind = i-1
      ret[ind] = max(ckpt, ret[ind]) + 1
      max_cnt = max(max_cnt, ret[ind])
  for i in xrange(n):
    ret[i] = max(ckpt, ret[i])
  return ret
