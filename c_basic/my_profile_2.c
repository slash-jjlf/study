#include <stdio.h>

int main() {
  /*
   나의 이름은 ?입니다.
   나의 나이는 ?살입니다.
   나의 키는 ?cm 입니다.
   나의 몸무게는 ?kg 입니다.
   나의 혈핵형은 ?B형 입니다.
   */

  //변수 선언
  int age = 0;
  float height = 0.0f;
  double weight = 0.0;
  char blood_type = '\0';

  printf("나이는? ");
  scanf("%d", &age);
  printf("키는? ");
  scanf("%f", &height);
  printf("몸무게는? ");
  scanf("%lf", &weight);
  printf("혈액형은? ");
  scanf(" %c", &blood_type);

  printf("\n");
  printf("나의 이름은 %s입니다.\n", "한준일");
  printf("나의 나이는 %d살 입니다.\n", age);
  printf("나의 키는 %.2fcm 입니다.\n", height);
  printf("나의 몸무게는 %.2lfkg 입니다.\n", weight);
  printf("나의 혈행형은 %c형 입니다.\n", blood_type);

  return 0;
}
