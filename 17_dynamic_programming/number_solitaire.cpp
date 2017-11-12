#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  vector<int> dp(n, 0);
  dp[0] = a[0];
  for (int i = 1; i < n; i++) {
    dp[i] = dp[i - 1];
    for (int j = 2; j <= min(i, 6); j++) {
      dp[i] = max(dp[i], dp[i - j]);
    }
    dp[i] += a[i];
  }
  return dp[n - 1];
}
