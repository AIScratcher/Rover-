# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:33:12 2017
 
@author: JG

class Neuron(object);
"""

import numpy as np
import Connenction


class Neuron(object):
    
    """ 
    Neuron:
    =======
    A Neuron with Inputs and Outputs. 
    Storages in self.__ios.
    
      Functions:
        __init__: 
            self: Object
            inp: Count of Input-Connections
            outp: Count of Output-Connections
    """
    def __init__(self,inp,outp):#Tested!
        io = [[],[]]
        for i in range(0,inp):
            io[0].append(0)
        for i in range(0,outp):
            io[1].append(0)
        self.__ios = np.array(io,dtype=np.object) 

        
    def set_input_connection(self,connection,index):#Tested!
        self.__ios[0][index] = connection

        self.__ios[0][index]._set_input(self)


        

    def _set_input(self,v,i):#Tested!
       self.__ios[0][i] = v
 
       
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
    
        
    def run(self):
        res = self.__get_result()
        for i in range(0,len(self.__ios[1])):
            self.__ios[1][i].set_input(res)
        self.__network.isExecuted(self)
    def add_Input(self,con): #Add a new Input Connection to the Network #TODO TESTING!!!
        self.__ios[0] = np.array(self.__ios[0] + con,dtype=np.object)
        return len(self.__ios[0])-1
    def add_Output(self,con): #Add a new 
        