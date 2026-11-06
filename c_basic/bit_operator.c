#include <stdio.h>

/*
&: 비트 AND 연산, 모두 1일때 1반환
|: 비트 OR 연산, 둘 중 하나라도 1이면 1반환
^: 비트 XOR 연산, 대응되는 비트가 서로 다르면 1을 반환
~: 비트 NOT 연산, 비트가 1이면 0, 0이면 1로 반전
<<: 입력한 수만큼 비트들을 왼쪽으로 이동
>>: 부호를 유지하면서 지정한 수 만큼 비트를 오른쪽으로 이동
*/

int main(void) {
  int result, first_value, second_value;

  first_value = 6;
  second_value = 7;
  result = first_value & second_value;
  printf("%d \n", result);

  result = first_value | second_value;
  printf("%d \n", result);
  
  result = ~first_value;
  printf("%d \n", result);

  return 0;
}
