#include <vector>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  int ret = 0;
  for (int i = 0; i < n; i++) {
    ret ^= a[i];
  }
  return ret;
}
