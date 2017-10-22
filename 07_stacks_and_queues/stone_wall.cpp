#include "stack"
#include "vector"

using namespace std;

int solution(vector<int> &h) {
  int ret = 0;
  int n = h.size();
  stack<int> stk;
  stk.push(0);
  for (int i = 0; i < n; i++) {
    while (stk.top() > h[i]) {
      stk.pop();
      ret++;
    }
    if (stk.top() < h[i]) {
      stk.push(h[i]);
    }
  }
  ret += stk.size() - 1;
  return ret;
}
