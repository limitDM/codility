int solution(int n, int m)
{
  int a = max(n, m);
  int b = min(n, m);
  int c = 1;
  while (b != 0){
    c = a % b;
    a = b;
    b = c;
  }
  return n / a;
}
