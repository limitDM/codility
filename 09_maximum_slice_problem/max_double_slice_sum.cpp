#include <vector>
#include <algorithm>

using namespace std;

vector<int> prefix_sum(vector<int> &a) {
  int n = a.size();
  vector<int> ret(n + 1, 0);
  for (int i = 0; i < n; i++) {
    ret[i + 1] = ret[i] + a[i];
  }
  return ret;
}

int solution(vector<int> &a) {
  int ret = 0;
  int n = a.size();
  vector<int> psum = prefix_sum(a);
  int min_sum = psum[1];
  int least = a[1];
  int saved = min_sum + least;
  for (int i = 2; i < n-1; i++) {
    if (min_sum > psum[i]) {
      min_sum = psum[i];
      least = a[i];
    }
    least = min(least, a[i]);
    saved = min(saved, min_sum + least);
    ret = max(ret, psum[i + 1] - saved);
  }
  return ret;
}
