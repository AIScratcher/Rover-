# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:58:13 2017

@author: SFZ_Laptop_012
"""

import numpy as np

class NeuronalNetwork(object):

	"""
	Neuronen sind nur Werte und immer wenn sie aktiviert werden
	führen sie die Funktion neuron(siehe uneten)

	"""



    #Evrything a Neuron does if it runs once. 
    def neuron(inp):
    	res = 0;
    	for i in range(0,len(inp)):
    		res += inp[i]
    	res = 1/(1 + np.power(np.e,x))
    	return res


    
            
