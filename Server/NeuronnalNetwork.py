# -*- coding: utf-8 -*-

import numpy as np

class NeuronalNetwork(object):

    def __init__(inputs_shape,outputs_shape):

            
        for i in range(0,inputs_shape):
            
            
        #Start Iterations
        self.__time = int(0)
        while(True): 
            self.run()
            self.__time += 1
    
    def getTime(self):
        return self.__time
    
    def run(self):
        #Code runs evry iteration
        