#include <stdio.h>

// 함수: 1.선언 2.정의 3.사용

void Sum(); // 1. 선언

int main(void)
{
  printf("---Sum 함수 시작 \n");
  Sum(); // 3. 사용(함수 호출)
  printf("---Sum 함수 끝 \n");
  return 0;
}

void Sum() // 2. 정의(;이 없는 것에 주의)
{
  // 함수 영역
  int first_value;
  int second_value;
  int result_value;

  printf("Enter first_value: ");
  scanf("%d", &first_value);
  printf("Enter second_value: ");
  scanf("%d", &second_value);

  printf("\n");
  printf("first_value is %d \n", first_value);
  printf("second_value is %d \n", second_value);
  printf("\n");

  result_value = first_value + second_value;
  printf("Sum is %d \n", result_value);
}
