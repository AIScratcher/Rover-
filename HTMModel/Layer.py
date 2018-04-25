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
        return self:__neurons

    def set_output(self,output_layer):
        #The network can't build all layers at once. So it's possible that the
        #output layer doesn't exsist by executing init
        self.__output_layer = output_layer


    def __init__(self,count_neurons,input_layer,output_layer):
        self.__output_layer = output_layer
        self.__input_layer = input_layer
        self.__neurons = []
        self.__count_neurons = count_neurons
        # Do nothing until the network ( the largest authority in the system wants)
        # that the neurons will generate.

    #These three functions will build the entire Neuron and
    #will also be executed
    def build_input(self,f_field):
        #f_field is a list of connections connected as input with the last
        #

        #Instance the input field f_field

        #Define two percente of the input space as impossible to connect
        #and do so with everything else
        len_input = len(f_field)
        two_percent_of_input  = int(( len_input/100 )* 2)
        #Find two_percent_of_input times random numbers and add them to
        #not_inhibition_area
        not_inhibition_area = []
        while len(not_inhibition_area) < two_percent_of_input :
            rand_number = int(np.random.uniform(0,len_input))
            if not rand_number in not_inhibition_area:
                not_inhibition_area.append(rand_number)
        #Build the Neuron
        #Build the connections from the neurons of the input layer
        f_field = []
        f_neurons = self.__input.get_neurons()
        for i in range(0,len(f_neurons)):
            if not i in not_inhibition_area:
                f_field += Connection(0,f_neurons[i])

        del len_input, f_neurons, two_percent_of_input, not_inhibition_area,rand_number
