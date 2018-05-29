#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
srand(time(NULL));
//Seed
int r = rand() % 2;
printf("%d",r);
}
