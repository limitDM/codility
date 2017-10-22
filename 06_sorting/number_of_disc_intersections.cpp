#include "vector"
#include "algorithm"

using namespace std;

const int MAX = 1e7;

int solution(vector<int> &a) {
  int ret = 0;
  int n = a.size();
  vector<int> lpts(n, 0);
  vector<long long int> rpts(n, 0);
  int cnt = -1;
  int status = 0;
  for (int i = 0; i < n; i++) {
    lpts[i] = i - a[i];
    rpts[i] = (long long) i + a[i];
  }
  sort(lpts.begin(), lpts.end());
  sort(rpts.begin(), rpts.end());
  for (int i = 0; i < n; i++) {
    while (status < n && lpts[status] <= rpts[i]){
      cnt++;
      status++;
    }
    ret += cnt;
    if (ret > MAX) {
      return -1;
    }
    cnt--;
  }
  return ret;
}
