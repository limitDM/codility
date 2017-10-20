def solution(A):
  east_cnt = 0
  pair_cnt = 0

  for i in A:
    if i == 0:
      east_cnt += 1
    else:
      pair_cnt += east_cnt

  if pair_cnt > 10**9:
    return -1
  else:
    return pair_cnt
