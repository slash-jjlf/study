#include <stdio.h>

/*
int main(void) 
{
  int value = 0;
  int result = 0;

  printf("Enter number: ");
  scanf("%d", &value);

  result = value * 5;
  
  if (result < 10) 
  {
       printf("%d\n", value);
       printf("%d\n", result);
  }
  else
  {
    printf("False!\n");
  }

  printf("Exit!\n");
  return 0;
}
*/

int main(void)
{
  int score = 0;

  printf("Enter your score: ");
  scanf("%d", &score);

  if (score >= 90)
  {
    printf("grade: A \n");
  }
  else if (score >= 80)
  {
    printf("grade: B \n");
  }
  else if (score >= 70)
  {
    printf("grade: C \n");
  }
  else if (score >= 60)
  {
    printf("grade: D \n");
  }
  else
  {
    printf("grade: F \n");
  }
  printf("EXIT!");
  return 0;
}
