#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  int s = 0;
  int ret;
  for (int i = 1; i < n; i++)
    s += a[i];
  s -= a[0];
  ret = abs(s);
  for (int i = 1; i < n-1; i++) {
    s -= 2 * a[i];
    ret = min(ret, abs(s));
  }
  return ret;
}
