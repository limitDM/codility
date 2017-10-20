def solution(n):
  i = 1
  store = 1
  while i**2 <= n:
    if n % i == 0:
      store = i
    i += 1
  other = n / store
  perimeter = 2 * (store + other)

  return perimeter
