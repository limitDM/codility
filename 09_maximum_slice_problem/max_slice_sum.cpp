#include <vector>
#include <algorithm>

using namespace std;

vector<long long> prefix_sum(vector<int> &a) {
  int n = a.size();
  vector<long long> ret(n + 1, 0);
  for (int i = 0; i < n; i++) {
    ret[i + 1] = (long long) ret[i] + a[i];
  }
  return ret;
}

int solution(vector<int> &a) {
  int n = a.size();
  vector<long long> psum = prefix_sum(a);
  long long left_end = 0;
  long long ret = psum[1];
  for (int i = 0; i < n; i++) {
    left_end = min(left_end, psum[i]);
    ret = max(ret, psum[i + 1] - left_end);
  }
  return (int) ret;
}
