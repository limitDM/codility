#include <algorithm>
#include <vector>
#include <string>

using namespace std;

const int MAX = 100010;

vector<int> solution(string &s, vector<int> &p, vector<int> &q) {
  int n = s.length();
  int m = p.size();
  int cnts[4][MAX] = {{0}};
  string criteria = ("ACGT");
  vector<int> ret(m, 0);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 4; j++){
      cnts[j][i+1] = cnts[j][i];
      if (s[i] == criteria[j])
        cnts[j][i+1]++;
    }
  }
  
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < 4; j++){
      if (cnts[j][q[i] + 1] - cnts[j][p[i]] > 0){
        ret[i] = j + 1;
        break;
      }
    }
  }
  return ret;
}
