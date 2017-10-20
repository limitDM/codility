def solution(H):
  stack = [0]
  cnt = 0
  for i in H:
    while i < stack[-1]:
      stack.pop()
      cnt += 1
    if i > stack[-1]:
      stack.append(i)
  cnt += len(stack) - 1
  return cnt
