#include "vector"
#include "algorithm"

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  int ret;
  sort(a.begin(), a.end());
  ret = a[n-1] * a[n-2] * a[n-3];
  if (a[1] < 0) {
    return max(ret, a[0] * a[1] * a[n-1]);
  }
  return ret;
}
