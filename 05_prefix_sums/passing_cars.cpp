#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 1000000000;

int solution(vector<int> &a) {
  int n = a.size();
  int ret = 0;
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    if (a[i] == 1){
      ret += cnt;
      if (ret > MAX)
        return -1;
    }
    else
      cnt++;
  }
  return ret;
}
