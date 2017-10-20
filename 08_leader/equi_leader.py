def find_dominator(A):
  n = len(A)
  size = 0
  lst = []

  #find candidate
  for i in xrange(n):
    if size == 0:
      val = A[i]
      size = 1
    elif val == A[i]:
      size += 1
    else:
      size -= 1

  #make counting history of candidate
  cnt = 0
  for i in xrange(n):
    lst.append(cnt)
    if val == A[i]:
      cnt += 1
  
  if cnt > n // 2:
    return val, lst, cnt
  else:
    return None, None, None


def solution(A):
  dominator, history, total = find_dominator(A)
  cnt = 0
  n = len(A)
  if dominator == None:
    return 0
  else:
    for i in xrange(1, n):
      if history[i] > i//2 and (total - history[i]) > (n - i) // 2:
        cnt += 1
    return cnt
