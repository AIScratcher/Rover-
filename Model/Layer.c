/*
 *	Author: Joris Gutjahr
 *	A Layer receives a Matrix as input an
 *	computes the binary output as Matrix.
 *
 */
#include "Matrix.c"
typedef struct Layer
{
    int size; //Number of Neurons
    Matrix (*run)(Matrix,struct Layer);//Run of the Layer
    void (*load) (size_t,size_t,Matrix,struct Layer)
    Matrix values; //Matrix with all variables for the Neurons
    Matrix net;
} Layer;
Matrix Layer_run(Matrix,Layer);
void Load_Layer(size_t,size_t,Matrix,Layer);

struct Layer Layer_setup(int size,Matrix net)
{
    /*
     * 	It will return l
     * 	and hold  a Matrix with the three
     * 	relevant tresholds for each Neuron;
     */
    Layer l;
    l.size = size;
    l.run = &Layer_run;
    l.load = &Load_Layer;
    l.values = Matrix_setup(3+2*((int)net.total_size - net.total_size/50)+(int))net.total_size/50+2,size);///Layer view on the Network
    l.net = net; ///Network Matrix
    return l;
}




void Load_Layer(size_t start,size_t end,Matrix net,Layer l)
{
    ///start:  first column thats part of the Layer
    ///end: last column thats part of the Layer
    ///net: Network Matrix
    ///l: Layer struct
    for(size_t i = start; i <= end; i++)
    {
        l.values.setDim(i-start,net.getDim(i,net),l.values); ///Move whole column at once
    }
}

Matrix Layer_run(Matrix Neurons,Matrix Connections)
{
    
    int cmd = cmd_queue.Pop();
    int adrs = cmd_queue.Pop();
    
    switch (cmd) {
	    case 1:
			//OUTOF #ADR
			//#ADR Column of Netwok Matrix 
			//GET w,n,t
			
			int adrs = {adrs,0};
			int w = net.get(adrs,net);
			adrs[1]++;
			int n = net.get(adrs,net);
			adrs[1]++;
			int t = net.get(adrs,net);
			


