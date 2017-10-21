#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int solution(vector<int> &a) {
  int ret = 0;
  int n = a.size();
  vector<int> psum(n + 1, 0);
  int cnt = 0;
  double val;
  double this_val;
  for (int i = 0; i < n; i++) {
    cnt += a[i];
    psum[i + 1] = cnt;
  }
  val = (double) psum[2] / 2;
  for (int i = 2; i < 4; i++) {
    for (int j = 0; j < n - i + 1; j++) {
      this_val = (double) (psum[j + i] - psum[j]) / i;
      if (this_val < val){
        val = this_val;
        ret = j;
      }
    }
  }
  return ret;
}
