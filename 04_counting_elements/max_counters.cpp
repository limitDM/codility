#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, vector<int> &a) {
  int m = a.size();
  vector<int> cnts(n + 1, 0);
  int largest = 0;
  int milestone = 0;
  
  for (int i = 0; i < m; i++) {
    if (a[i] < n + 1) {
      cnts[a[i]] = max(cnts[a[i]], milestone) + 1;
      largest = max(largest, cnts[a[i]]);
    }
    else
      milestone = largest;
  }
  cnts.erase(cnts.begin());
  for (int i = 0; i < n; i++) {
    cnts[i] = max(cnts[i], milestone);
  }
  return cnts;
}
