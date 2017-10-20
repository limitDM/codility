def get_prefix_sum(A):
  store = 0
  ret = []

  for i in A:
    store += i
    ret.append(store)

  return ret

def solution(A):
  A = A[1:-1]
  P = get_prefix_sum(A)
  
  start = 0
  m_diff = A[0]
  stored_start = A[0]
  M_sum = 0

  n = len(P)

  for i in xrange(1, n):
    m_diff = min(m_diff, A[i])
    stored_start = min(stored_start, start + m_diff)
    M_sum = max(M_sum, P[i] - stored_start)
    if P[i-1] < start:
      start = P[i-1]
      m_diff = A[i]

  return M_sum 
