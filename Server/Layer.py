# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 18:44:51 2018

@author: SFZ_Laptop_012
"""
import numpy as np

class Neuron(object):
    """
        A Neuron is just this set of values:
        float: Theta
        float : Psi
        list : inputs:
        inputs : 0 : W of f
        inputs : 1 : W of c
        inputs : 2 : W of b
        inputs : 3 : N of f
        inputs : 4 : N of c
        inputs : 5 : N of b
        Theta and Psi are Treshholds
        And the list inputs is the storage of the Input
        That's just 6 values who are just the w of the input
        And after that is the size of the (!)connected fields

    """
    def __init__(self,input_f,input_c,input_b,
                theta=np.random.uniform(0.01),
                psi=np.random.uniform(0.01)):
                self.theta, self.psi = theta,psi
                #Define inputs and fill it temporaly
                #with the whole inhibition area
                self.inputs = [input_f + input_c + input_b]
                #Then initilize the connections by telling them that we will be
                #her output
                for i in self.inputs:
                    i.set_output(self)
                #The inputs will now store the values seen above
                self.inputs = [0,0,0,0,0,0]
                self.output = 0 #Last activation value


    #If you want to execute a Neuron totaly there are 3 Steps, wich will execute
    #the Layer if it has enough data for this step
    #1.Feedforward predicting
    #2.Context pooling
    #3.Feedback pooling
    #Because each step must run with the whole Layer it's split about 3
    # diffrent methods called by the Layer if it's ready
    #For better explenation see the README.md in the Server directory

    #1.Feedforward predicting
    def r_predicting(feedforward_w,feedforward_n):
        if feedforward_w / feedforward_n > self.theta: #First Treshold
            self.output = 1
    #2.Context pooling
    def r_c_pooling(context_w,context_n):

    #3.Feedback pooling
    def r_b_pooling(feedback_w,feedback_n):




class Layer (object):
    """
    Layer is the processing group
    of Neurons
    ==============================

    """
