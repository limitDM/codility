#include "string"
#include "stack"

using namespace std;

int solution(string &s) {
  int n = s.length();
  stack<char> stk;
  for (int i = 0; i < n; i++) {
    if (stk.size() > 0 && stk.top() == s[i]) {
      stk.pop();
    }
    else if (s[i] == '(') {
      stk.push(')');
    }
    else if (s[i] == '{') {
      stk.push('}');
    }
    else if (s[i] == '[') {
      stk.push(']');
    }
    else {
      return 0;
    }
  }
  if (stk.size() == 0) {
    return 1;
  }
  else {
    return 0;
  }
}
