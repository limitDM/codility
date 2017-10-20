def get_prefix_sum(A):
  store = 0
  ret = []

  for i in A:
    store += i
    ret.append(store)

  return ret

def solution(A):
  P = get_prefix_sum(A)

  n = len(P)
  start = 0
  end = P[0]
  max_slice = end

  for i in xrange(1, n):
    if P[i - 1] < start:
      max_slice = max(max_slice, end - start)
      start = P[i - 1]
      end = P[i]
    else:
      end = max(end, P[i])

  max_slice = max(max_slice, end - start)

  return max_slice
