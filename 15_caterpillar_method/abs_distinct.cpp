#include <vector>

using namespace std;

vector<int> remove_duplicate(vector<int> &a) {
  vector<int> rt;
  int last = a[0] + 1;
  for (auto &i : a) {
    if (i != last) {
      last = i;
      rt.push_back(i);
    }
  }
  return rt;
}

int search_smallest_nonnegative(vector<int> &a) {
  int n = a.size();
  int end = n - 1;
  int beg = 0;
  int mid;
  int rt = 0;
  while (beg <= end) {
    mid = (beg + end) / 2;
    if (a[mid] >= 0) {
      rt = mid;
      end = mid - 1;
    } else {
      beg = mid + 1;
    }
  }
  return rt;
}

int solution(vector<int> &a) {
  a = remove_duplicate(a);
  int n = a.size();
  int rt = n;
  int beg, end;
  if (a[n - 1] <= 0 || a[0] >= 0) {
    return rt;
  }
  end = search_smallest_nonnegative(a);
  beg = end - 1;
  while (beg >= 0 and end < n) {
    if (- a[beg] < a[end]) {
      beg--;
    }
    else if (- a[beg] > a[end]) {
      end++;
    }
    else {
      rt--;
      end++;
    }
  }
  return rt;
}
