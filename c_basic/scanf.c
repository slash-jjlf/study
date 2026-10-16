#include <stdio.h>

int main() {
  int value = 0;
  printf("정수값 입력: ");
  scanf("%d", &value);
  printf("입력한 값은: %d\n", value);

  float value_float = 0.0f;
  printf("float 값 입력: ");
  scanf("%f", &value_float);
  printf("입력한 값은: %.2f\n", value_float);

  double value_double = 0.0;
  printf("double 값 입력: ");
  scanf("%lf", &value_double);
  printf("입력한 값은: %.3lf\n", value_double);

  return 0;
}
