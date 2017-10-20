#include <vector>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  vector<int> check(n+1, 0);
  int ret = 1;
  for (int i = 0; i < n; i++) {
    if (a[i] < n+1)
      check[a[i]] = 1;
  }
  for (int i = 1; i < n+1; i++) {
    ret *= check[i];
  }
  return ret;
}
