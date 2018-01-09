#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  sort(a.begin(), a.end());
  int rt = 0;
  int k;
  for (int i = 0; i < n - 2; i++) {
    k = i + 2;
    for (int j = i + 1; j < n - 1; j++) {
      while(k < n && a[k] < a[i] + a[j]) {
        k++;
      }
      rt += k - j - 1;
    }
  }
  return rt;
}
