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
    
    
    """
    def __init__(self,inp):
        
        self.__ios = np.zeros((inp,1),dtype=np.float32) #self.__ios[0] = Inputs
        
   def _set_input(self,v,i):
       self.__ios[0][i] = v
       
    def __func(self,x):
        """TODO sigmoid durch softmax ersetzen ( bessere Funktion ) """
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
        """Einmal aktiviert."""
        self.__ios[1] = self.__get_result()