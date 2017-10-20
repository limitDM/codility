def challenge(size, stack):
  while len(stack)>0:
    if stack[-1][1] == 0:
      stack.append((size, 0))
      return stack
    elif stack[-1][0] > size:
      return stack
    else:
      stack.pop()
  stack.append((size, 0))
  return stack

def solution(A, B):
  l = len(A)
  stack = []
  for i in xrange(l):
    size = A[i]
    way = B[i]
    if way == 0:
      stack = challenge(size, stack)
    else:
      stack.append((size, way))
  return len(stack)
