# -*- coding: utf-8 -*-

import numpy as np

class NeuronalNetwork(object):


	"""
    INIT-Plan:
        1.Build the Neurons 
        2.Define Input and Output Neurons
        3.Connect from the Input to the Output over (Number of Neurons/Input Neurons)
    RUN-Plan:
        If a Connection 
	"""




    def __init__(self,neurons,inputs,outputs): 
        #neurons: Number of Neurons  in the net
        #inputs: The Number of Neurons who will be inputs (a part of neurons)
        #outputs: The Number of Neuron who will be outputs (a part of neurons)
            
        
    
    def getTime(self):
        
            
        #Start Iterations
        self.__time = int(0)
        while(True): 
            self.run()
            self.__time += 1
    
    def getTime(self):
        return self.__time
    
    def run(self):
        #Code runs evry iteration
        