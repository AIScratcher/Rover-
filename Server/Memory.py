# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd

"""
Data:
=====
Saves a NeuronalNetwork into a 
CSV or TXT Data.
And can load them.
"""

class Data(object):
    
    def __init__(self,net): #net := The Neuronal Network
        self.__network = net
        
        
    def save_txt(self): # Generate a String and save them in a txt
        """
        TXT CODE:
            1.Time in the Network.
            2.Neurons (A number (Only for Identification in Saving file.) + Using + last Outputs
            3.Inputs (A number + Using + lastOutputs)
            4.Outputs (A number + Using + lastOutputs)
            4.Connections (Number of Input + Number of Output + Weigth + Output Index)
        """
        self.__network.stop() #Stops the Network for saving and starts again after.
        self.__text =  self.__network.getTime() + "," + "<Counts>" + "<Neurons>" + self.__network.getNeuron_Len()
        
    def save_csv(self): # Generate a CSV (Comma-separated values) and save them on Disk.
        
        
        
    
         