#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  if (n == 0) {
    return 0;
  }
  int ret = 0;
  int least = a[0];
  for (int i = 0; i < n; i++) {
    least = min(least, a[i]);
    ret = max(ret, a[i] - least);
  }
  return ret;
}
