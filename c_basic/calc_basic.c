#include <stdio.h>

int main() {

  int first_value;
  int second_value;
  int result = 0;

  printf("첫번째 값 입력 : ");
  scanf("%d", &first_value);
  printf("두번째 값 입력 : ");
  scanf("%d", &second_value);

  result = first_value + second_value;
  printf("덧셈 : %d\n", result);

  result = first_value - second_value;
  printf("뺄셈 : %d \n", result);

  result = first_value * second_value;
  printf("곱셈 : %d \n", result);

  result = first_value / second_value;
  printf("나눗셈 : %d \n", result);

  result = first_value % second_value;
  printf("나머지 : %d \n", result);

  return 0;
}
