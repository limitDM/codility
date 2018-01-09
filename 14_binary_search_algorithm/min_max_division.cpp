#include <vector>

using namespace std;

bool check(int val, int k, vector<int> &a) {
  int this_sum = 0;
  int n = a.size();
  for (int i = 0; i < n; i++) {
    if (a[i] > val) {
      return 0;
    }
    this_sum += a[i];
    if (this_sum > val) {
      k--;
      this_sum = a[i];
    }
  }
  return (k > 0);
}

int solution(int k, int m, vector<int> &a) {
  int n = a.size();
  int beg = 0;
  int end = m * n;
  int mid;
  int rt = -1;
  while (beg <= end) {
    mid = (beg + end) / 2;
    if (check(mid, k, a)) {
      end = mid - 1;
      rt = mid;
    }
    else {
      beg = mid + 1;
    }
  }
  return rt;
}
