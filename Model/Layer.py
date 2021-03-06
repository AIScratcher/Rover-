# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 18:44:51 2018

@author: aiscratch
@version: 0.0.5
"""
import numpy as np
from Neuron import Neuron
from Connection import Connection
class Layer (object):
    """
    Layer is the processing group
    of Neurons
    ==============================
    It contains one row of neurons that work all on the same
    input space, the Layer under and beyond and thereself .
    Every Neuron will predicte and pool together when the Layer  said it's rigth
    """

    def size(self): #Returns the size of the Layer
        return len(self.__neurons)

    def get_neurons(self):
        return self.__neurons


    def __init__(self,count_neurons,input_layer,output_layer):
        self.__output_layer = output_layer
        self.__input_layer = input_layer
        self.__neurons = np.zeros(count_neurons,dtype=np.object)
        for i in range(len(self.__neurons)):
            self.__neurons[i] = Neuron(self.__input_layer, self)

    def after_build(self,output_layer): #EXECUTE after the output_layer inits
        self.__output_layer = output_layer
        for i in range(len(self.__neurons)):
            self.__neurons[i].build_layer()
        for i in range(len(self.__neurons)):
            self.__neurons[i].after_build(output_layer)

    def run(self):
        #1. r_predicting
        for i in range8
