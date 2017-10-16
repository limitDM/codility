#include <vector>
#include <algorithm>

using namespace std;

int calc_gcd(int a, int b)
{
  int c = max(a, b);
  int d = min(a, b);
  int e;
  while (d != 0){
    e = c % d;
    c = d;
    d = e;
  }
  return c;
}

int remove_factor(int a, int b)
{
  while (a % b == 0){
    a /= b;
  }
  return a;
}

int solution(vector<int> &a, vector<int> &b)
{
  int ret = 0;
  int z = a.size();
  for (int i = 0; i < z; ++i){
    int l = a[i];
    int r = b[i];
    if (l == r){
      ++ret;
      continue;
    }
    int gcd = calc_gcd(l, r);
    for (int j = 2; gcd != 1 || j * j <= gcd; ++j){
      if (gcd % j == 0){
        gcd = remove_factor(gcd, j);
        l = remove_factor(l, j);
        r = remove_factor(r, j);
      }
    }
    if (l == 1 && r == 1)
      ++ret;
  }
  return ret;
}
