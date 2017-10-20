#include <vector>

using namespace std;

int solution(int x, vector<int> &a) {
  int n = a.size();
  vector<int> leaves(x + 1, 0);
  int ret = 0;
  for (int i = 0; i < n; i++) {
    if (leaves[a[i]] == 0) {
      leaves[a[i]] = 1;
      ret++;
      if (ret == x)
        return i;
    }
  }
  return -1;
}
