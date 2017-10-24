#include "vector"

using namespace std;

int solution(vector<int> &a) {
  int ret = -1;
  int n = a.size();
  int candidate;
  int size = 0;
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    if (size == 0) {
      size++;
      candidate = a[i];
    }
    else if (candidate == a[i]) {
      size++;
    }
    else {
      size--;
    }
  }
  for (int i = 0; i < n; i++) {
    if (a[i] == candidate) {
      ret = i;
      cnt++;
    }
  }
  if (cnt > n / 2) {
    return ret;
  }
  else {
    return -1;
  }
}
