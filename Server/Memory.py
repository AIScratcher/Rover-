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
        self.__network.stop()
        
    def save_txt(self): # Generate a String and save them in a txt
        self.__text = ","self.__network.getTime()
    def save_csv(self): # Generate a CSV (Comma-separated values) and save them on Disk.
        
        
        
    
         