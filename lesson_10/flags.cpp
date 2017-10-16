#include "vector"
#include "algorithm"

using namespace std;

int solution(vector<int> &a)
{
  int n = a.size();
  int start = -1;
  int end = -1;
  vector<bool> peaks(n, 0);
  for (int i = 1; i < n-1; ++i){
    if (a[i] > a[i-1] && a[i] > a[i+1]){
      peaks[i] = 1;
      if (start == -1)
        start = i;
      end = i;
    }
  }

  if (start == -1)
    return 0;
  else if (start == end)
    return 1;

  int max_step = 0;
  while (max_step * (max_step + 1) < n)
    ++max_step;
  

  for (int step = max_step; step > 2; --step){
    int cnt = step - 1;
    for (int i = start + step; i <= end; ++i){
      if (peaks[i]){
        --cnt;
        if (cnt == 0)
          return step;
        i += step - 1;
      }
    }
  }
  return 2;
}
