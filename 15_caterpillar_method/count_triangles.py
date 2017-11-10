def solution(a):
  n = len(a)
  a.sort()
  rt = 0
  for i in range(n - 2):
    k = i + 2;
    for j in range(i + 1, n - 1):
      while k < n and a[k] < a[i] + a[j]:
        k += 1
      rt += k - j - 1
  return rt
