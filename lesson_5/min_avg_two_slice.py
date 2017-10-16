def solution(A):
  n = len(A)
  avg = (A[0] + A[1]) / 2.0
  ret = 0

  for i in xrange(2, n): # just have to check for length 2 and 3.
    this_avg = (A[i-1] + A[i]) / 2.0
    if this_avg < avg:
      ret = i-1
      avg = this_avg
    this_avg = (A[i-2] + A[i-1] + A[i]) / 3.0
    if this_avg < avg:
      ret = i-2
      avg = this_avg

  return ret
