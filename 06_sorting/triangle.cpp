#include "vector"
#include "algorithm"

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  sort(a.begin(), a.end());
  for (int i = 0; i < n - 2; i++) {
    if ((long long)a[i] + a[i + 1] > a[i + 2]) {
      return 1;
    }
  }
  return 0;
}
