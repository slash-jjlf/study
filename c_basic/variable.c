#include <stdio.h>

int main()
{
  int value;
  value = 100;
  printf("%d\n", value);

  int index;
  index=200;
  printf("정수형 변수 출력: %d\n", index);

  float height = 177.5f;
  float weight = 75.2f;
  //float형 변수 정수 선언
  printf("실수형 변수 출력 : %.1f\n", height);
  printf("몸무게 출력 : %.2f\n", weight);

  double value_d = 1.12345678;
  //double형 변수 선언(double형은 float형보다 더 긴 소수점 표현가능)
  printf("더블형 변수 출력 :%.8lf", value_d);

  return 0;
}
