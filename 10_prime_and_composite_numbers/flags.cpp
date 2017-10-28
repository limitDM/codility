#include <vector>

using namespace std;

vector<int> peak_gaps(vector<int> &a) {
  int n = a.size();
  int cnt = 0;
  vector<int> ret;
  for (int i = 1; i < n - 1; i++) {
    cnt++;
    if (a[i] > a[i - 1] && a[i] > a[i + 1]) {
      ret.push_back(cnt);
      cnt = 0;
    }
  }
  return ret;
}

int solution(vector<int> &a) {
  int ret = 0;
  int n = a.size();
  vector<int> pgaps = peak_gaps(a);
  int m = pgaps.size();
  int remained, step;
  while (ret < m && ret * (ret + 1) < n) {
    ret++;
  }
  if (ret < 3) {
    return ret;
  }
  for (; ret > 2; ret--) {
    remained = ret - 1;
    step = 0;
    for (int i = 1; i < m; i++) {
      step += pgaps[i];
      if (step >= ret) {
        step = 0;
        remained--;
        if (remained == 0) {
          return ret;
        }
      }
    }
  }
  return ret;
}
