#include <algorithm>

using namespace std;

int solution(int N) {
  int ret = 0;
  int cnt = 0;

  while (N%2 == 0) N /= 2;

  while (N>0) {
    if (N%2 == 1) {
      ret = max(ret, cnt);
      cnt = 0;
    }
    else cnt++;
    N /= 2;
  }
  return ret;
}
