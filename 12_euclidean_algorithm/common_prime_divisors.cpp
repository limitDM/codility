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

bool check(int a, int b) {
  int g = gcd(a, b);
  a /= g;
  b /= g;
  for (int i = 2; (a != 1 || b != 1) && g != 1 && i <= g; i++) {
    if (g % i == 0) {
      g = remove_factor(g, i);
      a = remove_factor(a, i);
      b = remove_factor(b, i);
    }
  }
  return (a == 1 && b == 1);
}

int solution(vector<int> &a, vector<int> &b) {
  int ret = 0;
  int z = a.size();
  for (int i = 0; i < z; i++) {
    ret += check(a[i], b[i]);
  }
  return ret;
}
