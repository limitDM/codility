#include <vector>

using namespace std;

int solution(int k, vector<int> &a) {
  int n = a.size();
  int rt = 0;
  int tie = 0;
  for (int i = 0; i < n; i++) {
    tie += a[i];
    if (tie >= k) {
      rt++;
      tie = 0;
    }
  }
  return rt;
}
