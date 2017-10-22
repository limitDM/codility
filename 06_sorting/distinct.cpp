#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  int ret = 0;
  sort(a.begin(), a.end());
  if (n < 2) {
    return n;
  }
  else {
    ret = 1;
    for (int i = 1; i < n; i++) {
      if (a[i] != a[i-1]) {
        ret++;
      }
    }
  }
  return ret;
}
