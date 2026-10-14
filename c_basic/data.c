#include <stdio.h>

int main() {
  /*
    //%d와 같은 키워드를 형식문자라 함
    //%d(정수), %f(실수), %c(단일문자), %s(문자열)
    printf("100\n");     // 일영영 출력
    printf("%d\n", 100); // 정수값 100 출력
    // d는 decimal
  */
  /*
    printf("%d\n", 200);
    printf("%d\n", 1000);
    printf("실수 출력 : %.4f\n", 5.1512);
    printf("실수 철력 : %.2f\n", 3.14);
    printf("단일문자 출력 : %c\n", 'a'); // 단일문자 경우 ''
    printf("단일문자 출력 : %c\n", 'P');
    printf("문자열 출력 : %s\n", "Hello!"); // 문자열의 경우 ""
  */

printf("나의 이름은 %s 입니다.\n", "junil");
printf("나의 나이는 %d 입니다.\n", 20);
printf("나의 혈액형은 %c형 입니다.\n", 'B');
printf("나의 키는 %.2fcm 입니다.\n", 177.5);

  return 0;
}
