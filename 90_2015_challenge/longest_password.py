def validity(word):
  letters = 0
  digits = 0
  l = len(word)
  for char in word:
    ind = ord(char)
    if ord('a') <= ind <= ord('z') or\
       ord('A') <= ind <= ord('Z'):
      letters += 1
    if ord('0') <= ind <= ord('9'):
      digits += 1
  return (letters % 2 == 0 and\
          digits % 2 == 1 and\
          l == letters + digits)

def solution(s):
  lst = s.split()
  rt = -1
  for word in lst:
    if validity(word):
      rt = max(rt, len(word))
  return rt
