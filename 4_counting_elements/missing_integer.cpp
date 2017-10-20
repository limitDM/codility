#include <vector>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  vector<int> cnts(n + 1, 0);
  for (int i = 0; i < n; i++) {
    if (0 < a[i] && a[i] < n + 1)
      cnts[a[i]] = 1;
  }
  for (int i = 1; i < n + 1; i++) {
    if (cnts[i] == 0)
      return i;
  }
  return n + 1;
}
