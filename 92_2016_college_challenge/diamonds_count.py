def marked_board(xs, ys):
  n = len(xs)
  rt = [[0 for i in range(n)] for j in range(n)]
  for x, y in zip(xs, ys):
    rt[x][y] = 1
  return rt

def valid_pt(x, y, n):
  return x >= 0 and x < n and y >= 0 and y < n

def third_pt(x1, y1, x2, y2):
  x = 2 * x2 - x1
  y = y1
  return x, y

def fourth_pt(x1, y1, x2, y2):
  x = x2
  y = 2 * y1 - y2
  return x, y

def solution(xs, ys):
  n = len(xs)
  rt = 0
  board = marked_board(xs, ys)
  for x1, y1 in zip(xs, ys):
    for x2, y2 in zip(xs, ys):
      if x1 <= x2 or y1 >= y2:
        continue
      x3, y3 = third_pt(x1, y1, x2, y2)
      if not valid_pt(x3, y3, n) or board[x3][y3] == 0:
        continue
      x4, y4 = fourth_pt(x1, y1, x2, y2)
      if not valid_pt(x4, y4, n) or board[x4][y4] == 0:
        continue
      rt += 1
  return rt
