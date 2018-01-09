#include <vector>

using namespace std;

int abs_sum(vector<int> &a) {
  int rt = 0;
  for (auto i : a) {
    rt += abs(i);
  }
  return rt;
}

int solution(vector<int> &a) {
  int n = a.size();
  int s = abs_sum(a);
  int m = s / 2;
  vector<int> dp(m + 1, -1);
  vector<int> cnts(101, 0);
  for (int i = 0; i < n; i++) {
    cnts[abs(a[i])]++;
  }
  dp[0] = 0;
  for (int i = 1; i < 101; i++) {
    if (cnts[i] == 0) {
      continue;
    }
    for (int j = 0; j < m + 1; j++) {
      if (dp[j] >= 0) {
        dp[j] = cnts[i];
      } else if (j >= i && dp[j - i] > 0){
        dp[j] = dp[j - i] - 1;
      }
    }
  }
  for (int i = m; i >= 0; i--) {
    if (dp[i] >= 0) {
      return s - 2 * i;
    }
  }
}
