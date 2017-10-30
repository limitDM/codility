#include <vector>

using namespace std;

vector<int> elt_counter(vector<int> &a) {
  int n = a.size();
  vector<int> ret(2 * n + 1, 0);
  for (int i = 0; i < n; i++) {
    ret[a[i]]++;
  }
  return ret;
}

vector<int> solution(vector<int> &a) {
  int n = a.size();
  vector<int> elt_cnts = elt_counter(a);
  vector<int> non_divs(2 * n + 1, n);
  vector<int> ret(n, 0);
  for (int i = 1; i < 2 * n + 1; i++) {
    if (elt_cnts[i] != 0) {
      for (int j = 1; i * j < 2 * n + 1; j++) {
        if (elt_cnts[i * j] == 0) {
          non_divs[i * j] -= elt_cnts[i];
        }
      }
    }
  }
  for (int i = 0; i < n; i++) {
    ret[i] = non_divs[a[i]];
  }
  return ret;
}
