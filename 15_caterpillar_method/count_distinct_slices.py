MAX = int(1e9)

def solution(m, a):
  n = len(a)
  cnts = [0] * (m + 1)
  rt = 0
  back = 0
  for front in range(n):
    cnts[a[front]] += 1
    while cnts[a[front]] == 2:
      cnts[a[back]] -= 1
      back += 1
    rt += front - back + 1
    if rt > MAX:
      return MAX
  return rt
