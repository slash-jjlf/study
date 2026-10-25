#include <stdio.h>

int main(void)
{
  int value_first;

  value_first = 0;

  scanf("%d", &value_first);

  value_first *= 2;
  value_first *= 2;
  value_first *= 2;
  // value_first = value_first * 2

  printf("%d \n", value_first);
  return 0;
}
