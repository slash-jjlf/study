#include <stdio.h>

int main(void)
{
  //float 실수형 소수점 6자리
  //double 실수형 소수점 15자리

  double value;

  value = 1.2094810830840184108;
  printf("%lf \n", value);
  printf("%.15lf \n", value);

  return 0;
}
