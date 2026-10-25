#include <stdio.h>

int main(void)
{
  int value;
  int result;
  value = 0;
  result = 0;

  scanf("%d", &value);

  result = value++;

  printf("%d \n", result);
  printf("%d \n", value);

  return 0;
}
