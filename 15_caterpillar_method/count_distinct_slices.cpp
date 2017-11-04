#include <vector>

using namespace std;

const int MAX = 1e9;

int solution(int m, vector<int> &a) {
  int n = a.size();
  vector<int> cnts(m + 1, 0);
  int rt = 0;
  int back = 0;
  for (int front = 0; front < n; front++) {
    cnts[a[front]]++;
    while (cnts[a[front]] == 2) {
      cnts[a[back]]--;
      back++;
    }
    rt += front - back + 1;
    if (rt > MAX) {
      return MAX;
    }
  }
  return rt;
}
