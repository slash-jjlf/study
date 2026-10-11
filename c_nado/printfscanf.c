#include <stdio.h>
int main(void)
{
  // 정수형 변수에 대한 예제
  /*int age = 12;
  printf("%d\n", age);
  age = 13;
  printf("%d\n", age);*/
  
  // 실수형 변수에 대한 예제
  /*float f = 46.5;
  printf("%.2f\n", f);
  double d = 4.428;
  printf("%.2lf\n", d);*/
  //const int YEAR = 2000;
  //rintf("%d\n", YEAR);
  
  //printf
  //int add = 3 + 7;
  //printf("3 + 7 = %d\n", add);
  //printf("%d x %d = %d\n", 30, 79, 30 * 79);
  
  // scanf
  // 키보드 입력을 받아서 저장
  /*int input;
  printf("값을 입력하세요: ");
  scanf("%d", &input);
  printf("입력값: %d\n", input);*/

  /*int one,two,three;
  printf("3개의 정수를 입력하세요 : ");
  scanf("%d %d %d", &one,&two,&three);
  printf("첫번째 값: %d\n", one);
  printf("두번째 값: %d\n", two);
  printf("세번째 값: %d\n", three);*/

  // 문자(한 글자), 문자열(한 글자 이상의 여러 글자)
  /*char c = 'A';
  printf("%c\n", c);*/

  /*char str[256];
  scanf("%255s", str);
  printf("%s\n", str);*/
  
  // 프로젝트
  // 경찰관이 범죄자의 정보를 입수 (조서작성)
  // 이름? 나이? 몸무게? 키? 범죄명?

  char name[256];
  printf("이름이 뭐에요? ");
  scanf("%255s", name);

  int age;
  printf("나이가 몇살이에요? ");
  scanf("%d", &age);

  float weight;
  printf("몸무게가 몇 kg 이에요? ");
  scanf("%f", &weight);

  float height;
  printf("키가 몇 cm 이에요? ");
  scanf("%f", &height);

  char crime[256];
  printf("어떤 잘못을 했나요? ");
  scanf("%255s", crime);

  printf("\n\n------조 서------\n\n");
  printf("이름      : %s\n", name);
  printf("나이      : %d세\n", age);
  printf("몸무게    : %.2fkg\n", weight);
  printf("키        : %.2fcm\n", height);
  printf("범죄      : %s\n", crime);

  return 0;
}
