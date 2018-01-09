#include <vector>

using namespace std;

bool check(int v, vector<int> &a, vector<int> &b, vector<int> &c) {
  int n = a.size();
  int m = c.size();
  vector<int> nail_cnts(2 * m + 1, 0);
  for (vector<int>::iterator it = c.begin(); it != c.begin() + v; it++) {
    nail_cnts[*it] = 1;
  }
  for (int i = 1; i < 2 * m + 1; i++) {
    nail_cnts[i] += nail_cnts[i - 1];
  }
  for (int i = 0; i < n; i++) {
    if (nail_cnts[b[i]] - nail_cnts[a[i] - 1] == 0) {
      return 0;
    }
  }
  return 1;
}

int solution(vector<int> &a, vector<int> &b, vector<int> &c) {
  int m = c.size();
  
  int beg = 1;
  int end = m;
  int mid;
  int rt = -1;
  while (beg <= end) {
    mid = (beg + end) / 2;
    if (check(mid, a, b, c)) {
      rt = mid;
      end = mid - 1;
    }
    else {
      beg = mid + 1;
    }
  }
  return rt;
}
