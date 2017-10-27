int solution(int n) {
  int ret = 0;
  int i;
  for (i = 1; i < n / i; i++) {
    if (n % i == 0) {
      ret += 2;
    }
  }
  if (i * i == n) {
    ret++;
  }
  return ret;
}
