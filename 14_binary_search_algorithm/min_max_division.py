def check(A, b, K):
  this = b
  cnt = 1
  for i in A:
    if i > b:
      return K + 1
    elif i <= this:
      this -= i
    else:
      this = b-i
      cnt += 1
  return cnt

def solution(K, M, A):
  n = len(A)

  beg = 0
  
  end = n / K
  if n % K != 0:
    end += 1
  end *= M

  ret = 0
  while beg <= end:
    mid = (beg + end) / 2
    if check(A, mid, K) <= K:
      ret = mid
      end = mid - 1
    else:
      beg = mid + 1
  return ret
