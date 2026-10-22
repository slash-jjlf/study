#include <stdio.h>

int main(void)
{
	/*
	int index;
	index = 0;

	scanf("%d", &index); //변수앞에 &는 메모리 주소를 의미함
	printf("%d\n", index);
	*/

	char index;
	index = '\0';

	scanf("%c", &index);
	printf("%c \n", index);

	return 0;
}
