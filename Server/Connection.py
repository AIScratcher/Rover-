

import numpy as np
import Neuron 
import NeuronalNetwork


class Connection (object):
    """

    Connection
    ==========
    variables:
    __input = Inputneuron for the Connection
    __output = Outputneuron for the Connection
    self = Object 
    function:
    __init__(self, inp, outp, oindex):
<<<<<<< HEAD
    arguments:
    inp = the Input Neuron ( storage in __input)
    outp = the Output Neuron ( storage in __output )
    oindex = Index in the output.__ios[0]
=======
    Argumente:
    inp = Das Inputneuron zur Verbindung ( wird in __input gespeichert ) #Wenn beim __init__ noch kein Input definiert ist wird input = ""
    outp = Das Outputneuron zur Verbindung ( wird in __output gespeichert ) #Wenn beim __init__ noch kein  Output definiert ist wird output = ""
    oindex = Der Index der Verbindung im Outputneuron ( siehe Neuron._set_input )
>>>>>>> 25d34eaaca2adaaae8185779b1a3e319ca877c3b
    net = Eigenes Neuronales Netz
    Does:
    Init the Variables.

    _connect_():
    arguments:
    self: Object 
    Does:
    Get the Value and give them the output.

    """
<<<<<<< HEAD
    def __init__(self,net,inp = -1,outp = -1,oindex = -1):
       self.__net = net
       self.__index = oindex
       self.__input = inp
       self.__output = outp
       
       if not(inp == -1,output == -1):
           self.isWorking = True
       else:
           self.isWorking = False
            
    def _set_input(self,inp):
        self.__input = inp
        if not (self.__output == -1):
            self.isWorking = True
    def _set_output(self,outp):
        self.__output = outp
        if not (self.__input == -1):
            self.isWorking = True
=======
    def __init__(self,net,oindex = "",inp = "",outp =  ""):# inp,outp Fallback

        self.__net = net
        self.__weigth = 0
        self.__oindex = oindex
        self.__last_activation = net.getTime()
        self.__input = inp
        self.__output = outp
    
    def _set_input(self,inp):
        if self.__input == "":
            self.__input = inp
        else:
            return -1 #Input can't change twice
    def _set_output(self,outp,oindex):
        if self.__output == "":
            self.__output = outp
            self.__oindex = oindex
        else:
            return -1 #Output can't change twice too
>>>>>>> 25d34eaaca2adaaae8185779b1a3e319ca877c3b
    
    def _connect_(self):
        if self.isWorking == True:
            o = self.__input._get_outputs()
        
            #Update of the Weigths
            self.__w -= (net.getTime - self.__last_activation)
            self.__last_activation = net.getTime()
            self.__w += 1

            o *= self.__w 
            self.__output._set_input(o,self.__oindex)#Input setzen.
            self.__output.activate(self.__oindex) # Neuron Aktivieren
        

        
        