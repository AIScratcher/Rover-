

import numpy as np
import Neuron 
#import NeuronnalNetwork


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

    arguments:
    inp = the Input Neuron ( storage in __input)
    outp = the Output Neuron ( storage in __output )
    oindex = Index in the output.__ios[0]

    Argumente:
    inp = Das Inputneuron zur Verbindung ( wird in __input gespeichert ) #Wenn beim __init__ noch kein Input definiert ist wird input = ""
    outp = Das Outputneuron zur Verbindung ( wird in __output gespeichert ) #Wenn beim __init__ noch kein  Output definiert ist wird output = ""
    oindex = Der Index der Verbindung im Outputneuron ( siehe Neuron._set_input )

    net = Eigenes Neuronales Netz
    Does:
    Init the Variables.

    _connect_():
    arguments:
    self: Object 
    Does:
    Get the Value and give them the output.

    """

    def __init__(self,net,inp = -1,outp = -1,oindex = -1):
       self.__net = net
       self.__index = oindex
       self.__input = inp
       self.__output = outp
       
       if not(self.__input == -1,self.__output == -1): #If the Input and Output isn't set the Connection isn't Working
           self.isWorking = True
       else:
           self.isWorking = False
            
    def set_input(self,inp): #If the input (Neuron Object) is -1 set self.__input = inp
        self.__input = inp
        if not (self.__output == -1):
            self.isWorking = True
    def set_output(self,outp):
        self.__output = outp
        if not (self.__input == -1):
            self.isWorking = True


    
    def _connect_(self): #A Data transfer between IN- and OUTPUT
        if self.isWorking == True:
            o = self.__input.get_outputs()
        
            #Update of the Weigths
            self.__w -= (self.__net.getTime - self.__last_activation)
            self.__last_activation = net.getTime()
            self.__w += 1

            o *= self.__w 
            self.__output.set_input(o,self.__oindex)#Input setzen.
            self.__output.activate(self.__oindex) # Neuron Aktivieren
        

        
        
        