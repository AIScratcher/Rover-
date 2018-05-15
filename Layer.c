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
    Matrix net;
};
typedef struct Layer Layer;
Matrix Layer_run(Matrix,Layer);
Matrix Layer_run(Matrix,Layer);


struct Layer Layer_setup(int size,Matrix net) {
	/*
	 * 	It will return l
	 * 	and hold  a Matrix with the three
	 * 	relevant tresholds for each Neuron;
	 */
	Layer l;
	l.size = size;
	l.run = &Layer_run;
	l.values = Matrix_setup(3+2*((int)net.total_size - net.total_size/50)+(int))net.total_size/50+1,size);///Layer view on the Network
    l.net = net; ///Network Matrix
	return l;
}

void Load_Layer(size_t start,size_t end,Matrix net,Layer l) {
    ///start:  first column thats part of the Layer
    ///end: last column thats part of the Layer
    ///net: Network Matrix
    ///l: Layer struct
    for(size_t i = start;i <= end;i++) {
       l.values.setDim(i-start,net.getDim(i,net),l.values); ///Move whole column at once
    }
}
