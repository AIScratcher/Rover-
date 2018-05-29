#include <stdio.h>
#include <stdlib.h>
#include "Matrix.c"
int main(void) {
	printf("Matrix with 3 Dimensions and 4 Rows");
       	Matrix m = Matrix_setup(3,4);
	printf("Set 0,2 to 3\n");
	int adr[2] = {0,2};
	Matrix_set(adr,3,m);
	printf("Value of [0,2] = %d\n",Matrix_get(adr,m));
	return 0;
}
