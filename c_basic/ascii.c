#include <stdio.h>

int main() {
  char input;

  printf("변환할 문자를 입력: ");
  scanf("%c", &input);

  printf("입력한 문자 %c의 ascii값은 %d입니다.\n", input, input);
  return 0;
}
