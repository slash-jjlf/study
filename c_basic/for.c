#include <stdio.h>

/*
int main(void)
{
  // 반복문 for
  // for(초기화;조건;증감연산)
  int i;
  for (i = 0; i <= 9; i++)
  {
    printf("2 * %d = %d \n", i, 2 * i);
  }
  return 0;
}
*/

// 입력을 받아서 구구단을 출력

/*
int main(void){
  int i;
  int input;
  int result;

  printf("Enter number(only int): ");
  scanf("%d", &input);

  for (i = 1; i <= 9; i ++)
    {
      result = input * i;
      printf("%d * %d = %d \n", input, i, result);
    }
  printf("End!");
  return 0;
}
*/

// 1~입력받은 수까지 짝수만 출력

int main(void) {

  int input;

  printf("Enter number u want(onl int): ");
  scanf("%d", &input);

  for (int i = 1; i <= input; i++)
  {
    if (i % 2 == 0)
    {
      printf("%d \n", i);
    }
  }
  return 0;
}
