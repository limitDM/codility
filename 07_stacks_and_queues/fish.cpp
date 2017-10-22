#include "vector"
#include "stack"

using namespace std;

int solution(vector<int> &a, vector<int> &b) {
  int ret = 0;
  int n = a.size();
  stack<int> stk;
  for (int i = 0; i < n; i++) {
    if (b[i] == 1) {
      stk.push(a[i]);
    }
    else if (stk.size() == 0) {
      ret++;
    }
    else {
      while (stk.size() > 0 && stk.top() < a[i]) {
        stk.pop();
      }
      if (stk.size() == 0) {
        ret++;
      }
    }
  }
  return ret + stk.size();
}
