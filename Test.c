#include "Matrix.c"
#include <stdio.h>

int main(void) {
	printf("Setup Matrix: 3,4\n");
	Matrix m = Matrix_setup(3,4);
	printf("Make a Pointer to a int with 34 in it\n");
	int value = 34;
	int *ptr_value = &value;
	int adr[2] = {2,0};
	printf("Set 2,0 to the Pointer\n");
	Matrix_set(adr,ptr_value,m);
	printf("Value of 2,0: %p", Matrix_get(adr,m));
	return 0;
}
