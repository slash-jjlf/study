#include <stdio.h>

int main()
{
  // 변수 선언
  int age = 48;
  float weight = 75.1f;
  double height = 178.76;
  char type = 'A';

  printf("나의 이름은 %s 입니다.\n", "Junil");
  printf("나이는 %d살 입니다.\n", age);
  printf("몸무게는 %.2fkg 입니다.\n", weight);
  printf("키는 %.2lfcm 입니다.\n", height);
  printf("혈핵형은 %c형 입니다.\n", type);

  return 0;
}
