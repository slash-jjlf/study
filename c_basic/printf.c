#include <stdio.h>

int main(void) 
{
  printf("Hello Word!\n");

  //data
  //단일문자(변환문자)
  printf("%c \n", 'a'); //단일문자의 경우는 '' 사용
  printf("%c \n", 'c');
  
  //문자열
  printf("나의 이름은 %s입니다. \n", "한준일"); //문자열의 경우는 "" 사용
  printf("저의 직업은 %s이고, 음식은 %s을 좋아합니다. \n", "회사원", "떡복이");

  //숫자
  printf("%d \n", 100); //정수형
  printf("%f \n", 3.12345); //실수형
  printf("%.2f \n", 3.12345); //소주점 이하 자리수 지정

  //연산
  printf("%d + %d = %d \n", 3, 4, 3+4);
  printf("%c + %c = %c%c \n", 'a', 'b', 'a', 'b');

  return 0;
}
