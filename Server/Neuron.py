# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:33:12 2017
 
@author: JG
"""

import numpy as np


class Neuron(object):
    
    """ 
    Neuron:
    =======
    Ein Neuron mit mehreren Inputs (inp,ios[[]]).
    Und mehreren Outputs (outp,ios)

    Funktionen:
        __init__: 
    """
    def __init__(self,inp,outp):
        self.__ios = np.zeros((inp,1),dtype=np.object) #self.__ios[0] = Inputs  self.__ios[1] = Outputs
        
    def set_input_connection(self,connection,index):
        self.__ios[1][index] = connection
        self.__ios[1][index]._set_input = self
        self.__ios[]

   def _set_input(self,v,i):
       self.__ios[0][i] = v
       
    def __func(self,x):
        #TODO sigmoid durch softmax ersetzen ( bessere Funktion ) 
        #Wikipedia: www.wikipedia.org/softmax-function
        return 1/(1 + np.power(np.e,x))
    
    def __sum(self):
        sum = float()
        for i in range(0,len(self.__ios[0])):
            sum += self.__ios[0][i]
        return sum
    
    def __get_result(self):
        return self.__func(self.__sum())
        
    def _get_outputs(self):
        return self.__ios[1]
    
    def run(self):
        #Einmal aktiviert.
        self.__ios[1] = self.__get_result()
