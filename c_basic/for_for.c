#include <stdio.h>

/*
int main(void)
{
  for (int i = 1; i <= 9; i++)
       {
    for (int j = 1; j <= 9; j++)
         {
            printf("%d * %d = %d \n", i, j, i * j);
         }
       }
  return 0;
}
*/

// 3을 입력하면 1에서 3단까지 출력
/*
int main(void)
{ int input = 0;

  printf("Enter number: ");
  scanf("%d", &input);

  for (int i=1; i <= input; i++) {
    for (int j=1; j <=9; j++) {
      printf("%d * %d = %d \n", i, j, i * j);
    }
  }
  return 0;
}
*/

// 구구단을 가로로 출력

int main(void) {
  for (int i = 1; i <=9; i++) {
    for (int j = 2; j <=5; j++) {
      printf("%d * %d = %d \t", j, i, j * i);
    }
    printf("\n");
  }

printf("\n");

  for (int i = 1; i <=9; i++) {
    for (int j = 6; j <=9; j++) {
      printf("%d * %d = %d \t", j, i, j * i);
    }
    printf("\n");
  }
  return 0;
}
