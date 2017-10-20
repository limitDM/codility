def solution(A):
  n = len(A)

  B = [A[0]] * n

  i = 0
  for i in xrange(1, n):
    track = B[i-1]
    j = 2
    while i-j >= 0 and j < 7:
      track = max(track, B[i-j])
      j += 1
    B[i] = A[i] + track
  return B[n-1]
