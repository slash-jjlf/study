#include <stdio.h>

int main(void)
{
  printf("정수형 변수 \n\n");
  int a;
  int b;
  a = 10;
  b = 20;

  int result;
  result = a + b;

  printf("%d + %d = %d \n\n", a, b, result);

  printf("실수형 변수 \n\n");
  float num_1;
  float num_2;

  float result_f;

  num_1 = 10.5f;
  num_2 = 1.52f;
  result_f = num_1 + num_2;

  printf("%.2f\n\n", result_f);

  printf("문자형 변수 \n\n");
  // c에서는 문자열 타입은 존재 x -> 배열 문법
  char word;
  word = 'a';
  printf("%c \n", word);

  return 0;
}
