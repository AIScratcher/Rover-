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
    def build(self,neurons,inputs,outputs,datatype="txt"):
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
            
    	self.__inp_values = np.zeros(inputs)
    	self.__out_values = np.zeros(outputs)
        
        self.__datatype = datatype #Datatype: Type of the File 
    	return self

    def load(self,data): #Load a old NeuronalNetwork
    

    def __run(self,i):
        

    
    def __new_connection_for(self,neuron,x):
        i = n 
        for j in range(1,x):
            i = n.get_connections()
            highest_weigth = i[0]
            for k in range(1,len(i)):
                
            i = i[]
        
        
    
    def getTime(self):
        return self.__time
    
    def set_inputs(self,value_array):
    	self.__inp_values = value_array

    def get_outputs(self):
    	return self.__out_values

    def save():
        data = Memory.Data()
        data.save_txt()

        #2.Activate the Neurons
        for i in range(0,len(self.__neurons[0])):
            self.__neurons[0][i].set_input(self.__inp_values[i]) #Input_Neurons
        #3.Wait for the activation of the Outputs
        
        
        
        
        
    def save():
        data = Memory.Data()

        
        



        
        