#include "Matrix.c"
#include <stdio.h>


/*
 * Author: Joris Gutjahr
 * This File containes all elements of a good Neural Network
 * totaly represented in a Matrix.
 * To do so I make a Matrix:
 * Where each column is the full description of a Neuron:
 * It's made of three diffrent information parts:
 * #1 Tresholds, three treshold values.
 * #2 Inhibition Area, t and w of every connection to the Neuron:
 * 	#1 Type (0=f,1=c,2=b)
 * 	#2 w
 * 	#3 t
 * #3 Indicies of Elements in the input Matrix the Neuron doesn't have
 * connections to, they will be ignored
 * #4 Number of the Layer
 *
 */


//Important Informations about the Network:
struct Network_hyp {
	int size_of_layer;
	int number_of_layers;
	Matrix Network;//Network Matrix as descripted above
};

struct Network_hyp setup_Network(int layers,int neurons_per_layer);

struct Network_hyp setup_Network(int layers,int neurons_per_layer) {
	struct Network_hyp h;
	h.size_of_layer = neurons_per_layer;
	h.number_of_layers = layers;
	h.Network = Matrix_setup(3+(int) 2*(neurons_per_layer-neurons_per_layer/100*2)+(int) (neurons_per_layer/100*2)+1,neurons_per_layer);
	//Init Treshs
	int adr[2] = {0,0};
	for(int i = 0;i < h. Network.dims-4;i++) {
		adr[0] = i;
		h.Network.set(adr, 0.5,h.Network);
		adr[1] = 1;
		h.Network.set(adr,0.5,h.Network);
		adr[1] = 2;
		h.Network.set(adr,0.5,h.Network);
		adr[1] = 0;
	}
	//Make inhibition ignore
}
Matrix Mask_Layer_output(Layer L,)
