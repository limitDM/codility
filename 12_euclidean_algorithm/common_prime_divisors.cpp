#include <vector>
#include <algorithm>

using namespace std;

int gcd(int n, int m) {
  int a= max(n, m);
  int b = min(n, m);
  int c;
  while (b != 0) {
    c = a % b;
    a = b;
    b = c;
  }
  return a;
}

int remove_factor(int a, int b) {
  while (a % b == 0) {
    a /= b;
  }
  return a;
}


int solution(vector<int> &a, vector<int> &b) {
  int ret = 0;
  int z = a.size();
  for (int i = 0; i < z; i++) {
    int l = a[i];
    int r = b[i];
    if (l == r){
      ret++;
      continue;
    }
    int g = gcd(l, r);
    for (int j = 2; g != 1 || j * j <= g; j++) {
      if (g % j == 0){
        g = remove_factor(g, j);
        l = remove_factor(l, j);
        r = remove_factor(r, j);
      }
    }
    if (l == 1 && r == 1)
      ret++;
  }
  return ret;
}
