#include <stdio.h>  // printf를 쓰기 위해서
#include <unistd.h> // sleep을 쓰기 위해서

int main(void) {
  printf("loading....10%%");
  fflush(stdout);
  sleep(2);

  printf("\rloading....50%%");
  fflush(stdout);
  sleep(2);

  printf("\rroading....100%% completed! \n");

  return 0;
}
