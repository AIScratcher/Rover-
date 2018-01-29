# -*- coding: utf-8 -*-

import numpy as np
import Neuron 
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
    def build(self,neurons,inputs,outputs,datatype="txt"):
        """
    	neurons: Count of Neurons in the Network
    	inputs: Count of the Input Neurons in the Network (Not a part of the neurons-Count) 
    	outputs: Count of the Output Neurons in the Network (Not a part of the neurons-Count)
    	"""
    	#Generate Neurons
    	hidden = [] 
    	for i in range(0,neurons):#Hidden
    		hidden.append(Neuron.Neuron(1,1))#First Connections
    	inp = []
    	for i in range(0,inputs):
    		inp.append(Input_Neuron.Input_Neuron(1))
    	outp = []
    	for i in range(0,outputs):
    		outp.append(Neuron.Neuron(1,1))

    	self.__neurons = np.array((inp,hidden,outp),dtype=np.object)
    	#Connect:
    	#Inputs with the same number of hidden (First Layer...)
    	for i in range(0,len(self.__neurons[0])):
    		connection = Connection.Connection(self,inp=self.__neurons[0][i],outp=self.__neurons[1][i])

    	self.__run(neurons	/ inp *10)
    	self.__inp_values = np.zeros(inputs)
    	self.__out_values = np.zeros(outputs)
        
        self.__datatype = datatype #Datatype: Type of the File 
    	return selfs

    def load(self,data): #Load a old NeuronalNetwork
    
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
        #2.Activate the Neurons
        for i in range(0,len(self.__neurons[0])):
            self.__neurons[0][i].set_input(self.__inp_values[i]) #Input_Neurons
        #3.Wait for the activation of the Outputs
        
        
        
        
        
    def save():
        data = Memory.Data()
        
        



        