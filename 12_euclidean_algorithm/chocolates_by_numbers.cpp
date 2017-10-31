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

int solution(int n, int m) {
  int g = gcd(n, m);
  return n / g;
}
