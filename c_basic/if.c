#include <stdio.h>

int main(void) 
{
  int value = 0;
  int result = 0;

  scanf("%d", &value);

  result = value * 5;
  
  if (result < 10) 
      {
       printf("%d\n", value);
       printf("%d\n", result);
      }
  printf("Exit!\n");

  return 0;
}
