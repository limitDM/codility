def solution(A):
  n = len(A)
  if n == 0:
    return 0
  
  buy = A[0]
  sell = -1
  max_profit = 0

  for i in A[1:]:
    if i < buy:
      max_profit = max(max_profit, sell - buy)
      buy = i
      sell = i
    else:
      sell = max(i, sell)

  max_profit = max(max_profit, sell - buy)
  if max_profit > 0:
    return max_profit
  else:
    return 0
