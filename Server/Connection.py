"""
@author: aiscratch
@version: 0.0.1
"""
import numpy as np
class Connection(object):
    """
    Connection
    ==========
    Transfers information between two neurons
    if the random tresh is reached by the using

    """
    def set(self,neuron,type=True):
        #If the input or the output wasn't already at init of this connection
        #neuron is the to connecting neuron and type said if it's an input or output
        if type == True:
            self.__input = neuron
        else:
            self.__output = neuron

    def __init__(self,type, input=None,output=None,tresh=np.random.uniform(0.01),
                using=np.random.uniform(0.01)):
                self.__type = type #Is it f or c or b connection ( usefull for connect )
                self.__input,self.__output = input,output
                self.__tresh,self.__using = tresh,using
                self.__connected = tresh < using

    def connect(self):
        #If the input changes it's input to 1 it will execute this and
        #connect will test the tresh and using to increment one of the elements
        #in the input array at the output neuron
        if self.__using > self.__tresh:
            self.__output.inputs[type] += 1
            if not self.__connected: #The first time using reached tresh
                self.__output.inputs[type+3] += 1
        elif self.__connected: #using doesn't reach anymore
            self.__outputs.inputs[type+3] -= 1
        if not self.__using == 1:
            self.__using + 0.015 # 1.5 % per every activation
