#include <stdio.h>

int main(void)
{
  int a, b;
  int result_first;
  int result_second;
  result_first = 0;
  result_second = 0;

  printf("A값을 입력해 주세요 : ");
  scanf("%d", &a);
  printf("B값을 입력해 주세요 : ");
  scanf("%d", &b);

  result_first = a <= b;
  result_second = a == b;

  printf("result_first와 result_second의 AND 연산결과는 : %d \n", result_first && result_second);
  printf("result_first와 result_second의 OR 연산결과는 : %d \n", result_first || result_second);

  return 0;
}
