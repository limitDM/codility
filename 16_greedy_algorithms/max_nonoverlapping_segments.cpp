#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> &a, vector<int> &b) {
  int rt = 0;
  int last = -1;
  int n = a.size();
  for (int i = 0; i < n; i++) {
    if (a[i] > last) {
      rt++;
      last = b[i];
    }
  }
  return rt;
}
