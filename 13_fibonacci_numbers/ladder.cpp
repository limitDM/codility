#include <vector>
#include <cmath>

using namespace std;

int int_pow(int x, int p) {
  if (p == 0) {
    return 1;
  }
  else if (p == 1) {
    return x;
  }
  int tmp = int_pow(x, p/2);
  if (p % 2 == 0) {
    return tmp * tmp;
  }
  else {
    return x * tmp * tmp;
  }  
}

vector<int> fib_check(int l) {
  int a = 1;
  int b = 1;
  int c;
  int mod = int_pow(2, 30);
  vector<int> ret;
  ret.push_back(1);
  for (int i = 0; i < l; i++) {
    ret.push_back(a);
    c = b;
    b = a;
    a = (b + c) % mod;
  }
  return ret;
}

vector<int> solution(vector<int> &a, vector<int> &b) {
  int l = a.size();
  vector<int> fibs = fib_check(l);
  vector<int> ret;
  for (int i = 0; i < l; i++) {
    ret.push_back(fibs[a[i]] % int_pow(2, b[i]));
  }
  return ret;
}
