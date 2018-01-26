# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:59:04 2018

@author: JG
"""

import numpy as  np
import Neuron 
import Connection
#import NeuronnalNetwork

#Input Neurons own  Class
        
class Input_Neuron(Neuron.Neuron):#An Input_Neuron  for simple Controll of the Inputs.(Here the Input of ios would be a int)

    def __init__(self,outp): 
        Neuron.Neuron.__init__(self,1,outp)
        

    def set_input(self,v): 
        Neuron.Neuron.set_input(self,v,0)
       


class pseudoNet():  #A simulation of a Network from  the Perspective of the Connections
    def getTime():
        return 1
class pseudoOutput():  #A simulation of an Output Neuron from the Perspective of the Connections
    def activate(self,i):
        print("ACTIVATED:"+i)
    def set_input(self,v,i):
        print("INPUT:" + v +  "\t" +   i)
psdNet = pseudoNet()

i = Input_Neuron(2)
c = [Connection.Connection(psdNet,inp=i,0),Connection.Connection(psdNet,inp=i)]


i.set_input(21)
i.run()
print(i.get_outputs())