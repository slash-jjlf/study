#include <stdio.h>

/*
int main(void)
{
  int menu;

  printf("Enter number [1-3]: ");
  scanf("%d", &menu);

  switch(menu)
  {
    case 1:
      printf("You select number 1..\n");
      break;
    case 2:
      printf("You select number 2..\n");
      break;
    case 3:
      printf("You select number 3..\n");
      break;
    default:
      printf("wrong number\n");
  }

  printf("End!");
  return 0;
}
*/

int main(void)
{
  char menu;

  printf("Enter a, b, c: ");
  scanf("%c", &menu);

  switch(menu)
  {
    case 'a':
      printf("You select %c \n", menu);
      break;
    case 'b':
      printf("You select %c \n", menu);
      break;
    case 'c':
      printf("You select %c \n", menu);
      break;
    default:
      printf("You choose wrong char...\n");
  }
  
  printf("Exit!");
  return 0;
}
