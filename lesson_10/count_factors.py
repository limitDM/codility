def solution(n):
  i = 1
  cnt = 0
  while i ** 2 <= n:
    if n % i == 0:
      cnt += 2
    i += 1
  if (i - 1) ** 2 == n:
    cnt -= 1
  return cnt
