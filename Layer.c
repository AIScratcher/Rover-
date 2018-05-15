/*
 *	Author: Joris Gutjahr
 *	A Layer receives a Matrix as input an 
 *	computes the binary output as Matrix.
 *
 */
#include "Matrix.c"
typedef struct Layer {
	int size; //Number of Neurons
	Matrix (*run)(Matrix,struct Layer);//Run of the Layer
	Matrix values; //Matrix with all variables for the Neurons
};
typedef struct Layer Layer;
Matrix Layer_run(Matrix,Layer);
Matrix Layer_run(Matrix,Layer);


struct Layer Layer_setup(int size) {
	/*
	 * 	It will return l
	 * 	and hold  a Matrix with the three
	 * 	relevant tresholds for each Neuron;
	 */
	Layer l;
	l.size = size;
	l.run = &Layer_run;
	l.values = Matrix_setup(3,size);//Layer view on the Network
	return l;
}

Matrix Layer_run(Matrix input,Layer l) {
	/*
	 *	 The input:
	 *	 2D Matrix with the variables
	 *	 n and w for each  input
	 */
	//The second aren't set now
	int outputs[l.size];//Output Array
	for(int i = 0;i < l.size;i++) {
		//Each column is a Neurons tresholds
		
	}
}
