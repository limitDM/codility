def check_oneside(a):
  last_peak = 0
  lowest = 0
  rt = 0
  for i in a:
    if i >= last_peak:
      rt = max(rt, last_peak - lowest)
    if i > last_peak:
      last_peak = i
      lowest = i
    else:
      lowest = min(lowest, i)
  return rt
    
def solution(a):
  return max(check_oneside(a),
             check_oneside(a[::-1]))
