#include <stdio.h>
// standard input output. h헤더파일 - 미리 만들어진 기능의 모음

// 함수 이름 앞에 자료 형이 있다면,
// 함수가 종료될 때, 그자료형과 관련된 값을 반환해야함
int main(void) {
  printf("Hello World!\n");
  printf("\n");
  printf("name : junil\tage : 48\n"); // 이스케이프 문자 \n(줄바꿈), \t(탭)
  printf("\n");
  printf("이름\t학년\t점수\n");
  printf("Junil\t3\t97\n");
  printf("han\t2\t80\n");
  return 0;
}
