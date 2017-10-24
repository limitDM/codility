#include "vector"

using namespace std;

int solution(vector<int> &a) {
  int ret = 0;
  int n = a.size();
  int candidate;
  int size = 0;
  int cnt = 0;
  vector<int> cnts(n, 0);
  for (int i = 0; i < n; i++) {
    if (size == 0) {
      candidate = a[i];
      size++;
    }
    else if (candidate == a[i]) {
      size++;
    }
    else {
      size--;
    }
  }
  for (int i = 0; i < n; i++) {
    cnts[i] = cnt;
    if (a[i] == candidate) {
      cnt++;
    }
  }
  for (int i = 1; i < n; i++) {
    if (i / 2 < cnts[i] && (n - i) / 2 < (cnt - cnts[i])) {
      ret++;
    }
  }
  return ret;
}
