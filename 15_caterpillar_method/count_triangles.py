def solution(a):
  n = len(a)

  a.sort(reverse=True)

  cnt = 0
  for i in xrange(n-2):
    beg = i+1
    end = n-1
    while beg < end:
      while beg < end and a[i] >= a[beg] + a[end]:
        end -= 1
      cnt += end - beg
      beg += 1
  return cnt
