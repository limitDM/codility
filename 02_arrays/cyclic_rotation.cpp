#include <vector>

using namespace std;

vector<int> solution(vector<int> &a, int k) {
  int n = a.size();
  vector<int> ret(n, 0);
  for (int i = 0; i < n; i++) {
    ret[(i + k) % n] = a[i];
  }
  return ret;
}
