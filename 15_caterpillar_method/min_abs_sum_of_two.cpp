#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  int rt = (int) 2e9;
  int beg = 0;
  int end = n - 1;
  sort(a.begin(), a.end());
  while (beg < end) {
    rt = min(rt, abs(a[beg] + a[end]));
    if (-a[beg] == a[end]) {
      return 0;
    } else if (abs(a[beg]) < abs(a[end])) {
      end--;
    } else {
      beg++;
    }
  }
  return min(rt, abs(a[beg] + a[end]));
}
