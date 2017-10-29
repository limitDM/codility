#include <vector>

using namespace std;

vector<int> peak_cnts(vector<int> &a) {
  int n = a.size();
  int cnt = 0;
  vector<int> ret(n + 1, 0);
  for (int i = 1; i < n - 1; i++) {
    if (a[i] > a[i - 1] && a[i] > a[i + 1]) {
      cnt++;
    }
    ret[i + 1] = cnt;
  }
  ret[n] = ret[n - 1];
  return ret;
}

bool satisfiable(vector<int> &pcnts, int k) {
  int n = pcnts.size() - 1;
  if (n % k != 0) {
    return 0;
  }
  for (int i = 0; i < n / k; i++) {
    if ((pcnts[(i + 1) * k] - pcnts[i * k]) == 0) {
      return 0;
    }
  }
  return 1;
}

int solution(vector<int> &a) {
  int n = a.size();
  vector<int> pcnts = peak_cnts(a);
  for (int k = 1; k <= n; k++) {
    if (satisfiable(pcnts, k)) {
      return n / k;
    }
  }
  return 0;
}
