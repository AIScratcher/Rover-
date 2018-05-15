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

Matrix Layer_run(Matrix input,Layer this)
{
    ///input: 3D Matrix with the 3 Types of Inputs (f,c,b), where b is the activation of the last iteration
    ///and c is a void
    ///Go through all Neurons , collect there inputs , compare with the using and  tresh of the connection
    ///and compare with the tresh_1 of the Neuron. Then set last output of Neuron to 1 or 0 (last element of  the Matrix this.values.
    Matrix neuron_spec_input = Matrix_setup(3,input.total_size/input.dims);
    for(int i = 0; i < this.values.dims; i++)
    {
        neuron_spec_input.setDim(Layer_collect_inputs(input,this.values.getDim(i),0)); //1) Compare inputs with there using and tresh by ignoring those
                                                                                      //who aren't connected.( Just for f)
        int adr[2] = {i,this.values.total_size/this.values.dims}
        this.values.set()
    }
}
