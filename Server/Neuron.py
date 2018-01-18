# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:33:12 2017
 
@author: JG

class Neuron(object);
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
            self: Object
            inp: Anzahl an Inputs
            outp: Anzahl an Outputs
    """
    def __init__(self,inp,outp):#Tested
        io = [[],[]]
        for i in range(0,inp):
            io[0].append(0)
        for i in range(0,outp):
            io[1].append(0)
        self.__ios = np.array(io,dtype=np.object) 
        
        
    def set_input_connection(self,connection,index):
        self.__ios[0][index] = connection
        self.__ios[0][index]._set_input(self)

    def set_input(self,v,con):
        
    def __func(self,x):
        #TODO sigmoid durch softmax ersetzen ( bessere Funktion ) 
        #Wikipedia: https://en.wikipedia.org/wiki/Softmax_function
        #YT: https://www.youtube.com/watch?v=xRJCOz3AfYY&list=PL2-dafEMk2A7mu0bSksCGMJEmeddU_H4D
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
    
    def activate(index):
        
    def run(self):
        #Einmal aktiviert.
        self.__ios[1] = self.__get_result()
        