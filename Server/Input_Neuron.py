# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:59:04 2018

@author: JG
"""

import numpy as  np
import Neuron 
import Connection
import NeuronnalNetwork

#Input Neurons own  Class
        
class Input_Neuron(Neuron.Neuron):#An Input_Neuron  for simple Controll of the Inputs.(Here the Input of ios would be a int)

    def __init__(self,outp,net): 
        Neuron.Neuron.__init__(self,1,outp,net)
        

    def set_input(self,v): 
        Neuron.Neuron.set_input(self,v,0)
    
    def run(self):
        Neuron.Neuron.run()
       


#Debugging Classes
class pseudoNet():  #A simulation of a Network from  the Perspective of the Connections
    def getTime():
        return 1
    def isExecuted(self,neuron):
        print("A Neuron has Executed")
class pseudoOutput():  #A simulation of an Output Neuron from the Perspective of the Connections
    def activate(self,i):
        print("ACTIVATED:"+i)
    def set_input(self,v,i):
        print("INPUT:" + v +  "\t" +   i)
