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

int solution(vector<int> &a) {
  a = remove_duplicate(a);
  int n = a.size();
  int rt = n;
  int beg, end;
  if (a[0] >= 0 || a[n - 1] <= 0) {
    return rt;
  }
  end = n - 1;
  beg = 0;
  while (a[end] >= 0 and a[beg] < 0) {
    if (a[beg] > - a[end]) {
      // because of overflow issue, compare between negative numbers
      // |MIN_INT| > MAX_INT
      end--;
    } else if (a[beg] < - a[end]) {
      beg++;
    } else {
      end--;
      rt--;
    }
  }
  return rt;
}
