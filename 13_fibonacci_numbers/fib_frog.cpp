#include <vector>

using namespace std;

vector<int> fib_under(int n) {
  vector<int> rt;
  int a = 1;
  int b = 1;
  int c;
  while (a <= n) {
    rt.push_back(a);
    c = b;
    b = a;
    a = b + c;
  }
  return rt;
}

int solution(vector<int> &a) {
  a.push_back(1);
  int n = a.size();
  vector<int> fibs = fib_under(n);
  vector<int> steps(n, n + 2);
  for (int i = 0; i < n; i++) {
    if (a[i] == 0) {
      continue;
    }
    for (vector<int>::iterator it = fibs.begin(); it != fibs.end(); it++) {
      if (i - *it < -1) {
        break;
      }
      else if (i - *it == -1) {
        steps[i] = 1;
      }
      else if (steps[i - *it] != n + 2) {
        steps[i] = min(steps[i], steps[i - *it] + 1);
      }
    }
  }
  if (steps[n - 1] == n + 2) {
    return -1;
  }
  else {
    return steps[n - 1];
  }
}
