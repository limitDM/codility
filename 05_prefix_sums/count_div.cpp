int solution(int a, int b, int k) {
  int ret = b / k - a / k;
  if (a % k == 0)
    ret++;
  return ret;
}
