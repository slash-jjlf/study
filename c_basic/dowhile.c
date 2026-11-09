#include <stdio.h>

// do_while example

int main(void)
{
  int i = 1;
  int input = 0;

  printf("Enter num: ");
  scanf("%d", &input);

  do {
    printf("%d * %d = %d \n", input, i, input * i);
    i++;
  } 
  while (i <=9);

  return 0;
}
