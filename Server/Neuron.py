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
    A Neuron with Inputs and Outputs. 
    Storages in self.__ios.
    
      Functions:
        __init__: 
            self: Object
            inp: Index of Input-Connections
            outp: Index of Output-Connections
    """
    def __init__(self,inp,outp):#Tested!
        io = [[],[]]
        for i in range(0,inp):
            io[0].append(0)
        for i in range(0,outp):
            io[1].append(0)
        self.__ios = np.array(io,dtype=np.object) 
        self.__act_count = 0 #If this == len(self.__ios[0]) execute run()
        
    def set_input_connection(self,connection,index):#Tested!
        self.__ios[0][index] = connection

        self.__ios[0][index]._set_input(self)


        

    def _set_input(self,v,i):#Tested!
       self.__ios[0][i] = v
       self.__activate()
 
       
    def __func(self,x):#Tested!

        #TODO sigmoid durch softmax ersetzen ( bessere Funktion ) 
        #Wikipedia: https://en.wikipedia.org/wiki/Softmax_function
        #YT: https://www.youtube.com/watch?v=xRJCOz3AfYY&list=PL2-dafEMk2A7mu0bSksCGMJEmeddU_H4D
        return x/(np.sqrt(1 + x**2))
    
    def __sum(self):#Tested
        sum = float()
        for i in range(0,len(self.__ios[0])):
            sum += self.__ios[0][i]
        return sum
    
    def __get_result(self):#__get_result
        return self.__func(self.__sum())
        
    def _get_outputs(self):
        return self.__ios[1]
    
    def __activate(self,index):
       self.__act_count += 1
       if self.__act_count == len(self.__ios[0]):
           self.run()
        
    def run(self):
        self.__ios[1] = self.__get_result()
        