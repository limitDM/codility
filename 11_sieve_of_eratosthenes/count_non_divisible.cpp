vector<int> solution(vector<int> &a)
{
  int n = a.size();
  vector<int> appearance(2*n+1, 0);
  for (vector<int>::iterator it=a.begin(); it!=a.end(); ++it)
    appearance[*it] += 1;

  vector<int> non_divs(2*n+1, 0);
  non_divs[1] = n - appearance[1];
  for (int i = 0; i < n; ++i){
    if (non_divs[a[i]] != 0 || a[i] == 1)
      continue;
    int div_cnt = n - appearance[1] - appearance[a[i]];
    for (int j = 2; j * j <= a[i]; ++j){
      if (j * j == a[i])
        div_cnt -= appearance[j];
      else if (a[i] % j == 0)
        div_cnt -= appearance[j] + appearance[a[i] / j];
    }
    non_divs[a[i]] = div_cnt;
  }
  vector<int> ret(n, 0);
  for (int i = 0; i < n; ++i)
    ret[i] = non_divs[a[i]];
  return ret;
}
