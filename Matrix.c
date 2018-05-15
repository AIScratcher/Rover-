//Author: Joris Gutjahr
//Matrix Operations and 2darrays with Data structs
#include <stdio.h>

typedef struct Matrix {
	int dims; //Number of Dimensions
	int total_size;	//Size of a Row = total_size/dims;
	int (*set)(int*,int,struct Matrix); //Function Pointers;
	int (*get)(int*,struct Matrix);
	int* values; //Pointer ot the values array;
} Matrix;

int Matrix_set(int*,int,Matrix);
int Matrix_get(int*,Matrix);
int Matrix_choose(int*,Matrix);
Matrix Matrix_setup(int,int);
 
Matrix Matrix_setup(int dims,int size) {
	Matrix m;
	m.dims = dims;
	m.total_size = dims*size;
	m.set = &Matrix_set;
	m.get = &Matrix_get;
	int a[dims*size];
	m.values = a;
	return m;
}

int Matrix_set(int* adress,int value,Matrix m) {
	m.values[Matrix_choose(adress,m)] = value;
	return 0;
}
int Matrix_get(int* adress,Matrix m) {
	return m.values[Matrix_choose(adress,m)];
}
int Matrix_choose(int* adress,Matrix m) {
	int size = m.total_size/m.dims;
	//Index in the values array
	return (adress[0]-1)*size+adress[1];
}
