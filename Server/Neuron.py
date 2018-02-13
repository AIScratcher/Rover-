# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:33:12 2017
 
@author: JG

class Neuron(object);
"""

import numpy as np
import Connection


class Neuron:
    
    """ 
    Neuron:
    =======
    A Neuron with Inputs and Outputs. 
    Storages in self._ios.
    
      Functions:
        __init__: 
            self: Object
            inp: Count of Input-Connections
            outp: Count of Output-Connections
     Class Variablen:
         self.using: The Count of uses in the last 1000 loops
         self.__ios: The np Array of Input and Output Connections
         self.__network: The NeuronalNetwork where the Neuron is in.
        
    """


    
    
    

    def __init__(self,inp,outp,net):#Tested!
        io = [[],[]]
        for i in range(0,inp-1):
            io[0].append(0)
        for i in range(0,outp-1):
            io[1].append(0)
        self.__ios = np.array(io,dtype=np.object) 
        self.__network = net
        self.using = 0
        self.__got_input_value = np.zeros(len(self.__ios[1])-1,dtype=np.int16) #Array of Inputs Neuron got


        
        
        
        
    def set_input_connection(self,connection,index):#Tested!
        self.__ios[0][index] = connection

        self.__ios[0][index].set_input(self)
    
    def set_output_connection(self,connection,index):
        if index < len(self.__ios[1]):
            self.__ios[1][index] = connecion
            self.__ios[0][index].set_input(self)
                
        

    def set_input(self,v,i):#Tested!
       self.__ios[0][i] = v
       self.activate(i)
       
       
       
 
    
       
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
    
    def __get_result(self):#
        return self.__func(self.__sum())
    
    
    

        
    def get_outputs(self):
        return self.__res
    
    def get_connections(self,out=True): #For Path following.
        if out == True:
            return self.__ios[1]
        else:
            return self.__ios[0]
    
    def resetUsing(self): #Logic by ANN
        self.using = 0

        
            
    def run(self):#Test
        self.__res = self.__get_result()
        self.__network.isExecuted(self)
        self.using += 1
        for i in self.__ios[1]:
            i._connect_()
    
    
    
    
    def activate(self,index):
        self.__got_input_value[index] = 1
        act_inputs = 0
        for i in self.__got_input_value:
            act_inputs  += i
        if  act_inputs >=  ((len(self.__got_input_value)+1)/4)*3:
            self.run()
            
         
        
        
        
        
        
        
    def add_Input(self,con): #Add a new Input Connection to the Network #TODO TESTING!!!
        self.__ios[0] = np.array((self.__ios[0],con),dtype=np.object)

    
    def add_Output(self,con): #Add a new  Output Connection to the Network  #TODO Testing!!!
        
        self.__ios[0] = np.array((self.__ios[1],con),dtype=np.object)
        print(self.__ios[1])
    
    
    
    

    

    
    