int solution(int n) {
  int ret = 2 * (n + 1);
  for (int i = 2; i * i <= n; i++) {
    if (n % i == 0) {
      ret = 2 * (i + n/i);
    }
  }
  return ret;
}
