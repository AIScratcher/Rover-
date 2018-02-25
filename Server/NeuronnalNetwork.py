# -*- coding: utf-8 -*-

import numpy as np
import Neuron 
import Input_Neuron
import Connection
import Memory
        

class NeuronalNetwork(object):
    
    """
    The class of an Neuronal Network,
    explained in  NeuronalesNetwerk..odt 
    """
    #def build(self,):
    #def load(self):
    def __run(self):
        """
        1.Read the outputs
        2.Set the inputs 
        3.Sort the neurons in a,b,c
        """
        #1.Read the outputs
        outputs = []
        for i in range(0,len(self.__neurons[2])):
            outputs[i] = self.__neurons[2].get_outputs()
        self.__out_values = np.array(outputs)
        
        #2.Set the inputs
        for  i,j in zip(self.__neurons[0],range(0,len(self.__neurons[0]))):
            i.set_input(self.__inp_values[j])
        
        #3.Sort the neurons in a,b,c
        
        
    def __new_connection_for(self,neuron,x):
        i = neuron 
        for j in range(1,x):
            i = n.get_connections()
            h_weigth = 0
            for k in i:
                if k._get_Weigth > h_Weigth:
                    next_neuron = k
        
    
    def getTime(self):
        return self.__time
    
    def set_inputs(self,value_array):
    	self.__inp_values = value_array

    def get_outputs(self):
    	return self.__out_values
    
    
    def main(self):
        

    def save():
        data = Memory.Data()
        if self.__dtype == 'txt':
            data.save_txt()
    
        



        
        