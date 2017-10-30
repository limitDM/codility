#include <vector>

using namespace std;

vector<int> prime_check(int n) {
  vector<int> ret(n + 1, 1);
  ret[0] = 0;
  ret[1] = 0;
  for (int i = 2; i < n; i++) {
    if (ret[i] == 1) {
      for (int j = 2; i * j < n + 1; j++) {
        ret[i * j] = 0;
      }
    }
  }
  return ret;
}

vector<int> semiprime_cnts(int n) {
  vector<int> pcheck = prime_check(n);
  vector<int> ret(n + 1, 1);
  int cnt = 0;
  ret[0] = 0;
  ret[1] = 0;
  for (int i = 2; i < n; i++) {
    if (pcheck[i] == 1) {
      ret[i] = 0;
    }
    else if (ret[i] == 1) {
      for (int j = 2; i * j < n + 1; j++) {
        ret[i * j] = 0;
      }
    }
  }
  for (int i = 0; i < n + 1; i++) {
    if (ret[i] == 1) {
      cnt++;
    }
    ret[i] = cnt;
  }
  return ret;
}

vector<int> solution(int n, vector<int> &p, vector<int> &q) {
  int m = p.size();
  vector<int> ret(m, 0);
  vector<int> cnts = semiprime_cnts(n);
  for (int i = 0; i < m; i++) {
    ret[i] = cnts[q[i]] - cnts[p[i] - 1];
  }
  return ret;
}
