# -*- coding: utf-8 -*-

import numpy as np
import Neuron 
import Input_Neuron
import Connection
import Memory









class NeuronalNetwork(object):
    
    
    """
	INIT-Plan:
    
        1.Build the Neurons 
        2.Define Input and Output Neurons
        3.Connect from the Input to the Output over (Number of Neurons/Input Neurons)
    RUN-Plan:
        If a Connection 
	"""
    def build(self,inputs,outputs,datatype="txt"):
        """
    	inputs: Count of the Input Neurons in the Network 
    	outputs: Count of the Output Neurons in the Network 
    	"""
        io = [[],[]]
        for i in range(0,inputs):
            io[0].append(Input_Neuron.Input_Neuron(outputs,self))
        for i in range(0,outputs):
            io[1].append(Neuron.Neuron(outputs/2,1,self))
        
    	
    #def load(self,data): 
        
    def __run(self,i):
        
        #Start Iterations
        self.__time = int(0)
        while(True): 
            self.__loop(i)
            self.__time += 1
            if self.finish == True:
            	break
        return 0
    
    def getTime(self):
        return self.__time
    
    def set_inputs(self,value_array):
    	self.__inp_values = value_array

    def get_outputs(self):
    	return self.__out_values
    def __loop(self,waiting_time):
        #Code runs every iteration
        """
        1.Set Inputs to self.__inp_values
        1.2. Clear the isExecuted Array.
        2.Activate the Input Neurons
        3.Wait for the activation of the Outputs
        """
        #1.Set the Inputs to self.__inp_values
        for i in range(0,len(self.__neurons[0])):
            self.__neurons[0][i].set_input(self.__inp_values[i]) #Input_Neurons
        
        #2.Activate the Inputs
        
    def 
        
    def save():
        data = Memory.Data()
        data.save_txt()
        
        



        
        