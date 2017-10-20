#include <vector>

using namespace std;

int solution(vector<int> &a) {
  int n = a.size();
  long long int ret = (long long) (n+1) * (n+2) / 2;
  for (int i = 0; i < n; i++)
    ret -= a[i];
  return (int) ret;
}
