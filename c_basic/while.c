#include <stdio.h>

// 구구단 출력 프로그램

/*
int main() 
{
  int i = 1;
  int input;
  int result;
  
  printf("Enter base num: ");
  scanf("%d", &input);

  while (i <=9)
  {
    result = input * i;
    printf("%d * %d = %d \n", input, i, result);
    i++;
  }
  return 0;
}
*/

// 값을 입력 받아 3의 배수 출력

int main()
{
  int i = 1;
  int input = 0;

  printf("Enter num: ");
  scanf("%d", &input);

  while (i <= input)
    {
      if(i % 3 == 0)
        {
          printf("%d \n", i);
        }
    i++;
    }
  return 0;
}
