

import numpy as np



class Connection (object):
    """

    Connection
    ==========
    Variabeln:
    __input = Inputneuron zur Verbindung
    __output = Outputneuron zur Verbindung
    self = Objekt-Instanz
    Funktionen:
    __init__(self, inp, outp, oindex):
    Argumente:
    inp = Das Inputneuron zur Verbindung ( wird in __input gespeichert ) #Wenn beim __init__ noch kein Input definiert ist wird input = ""
    outp = Das Outputneuron zur Verbindung ( wird in __output gespeichert ) #Wenn beim __init__ noch kein  Output definiert ist wird output = ""
    oindex = Der Index der Verbindung im Outputneuron ( siehe Neuron._set_input )
    net = Eigenes Neuronales Netz
    Tut:
    Initalisiert die Variablen 

    _connect_():
    Argumente:
    self: Objektinstanz
    Tut:
    holt den Wert vom Input-Neuron multipliziert den mit seinem Weigth  und gibt ihm 
    dem 

    """
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
    
    def _connect_(self):
        o = self.__input._get_outputs()
        #Update des Weigths
        self.__w -= (net.getTime - self.__last_activation)
        self.__last_activation = net.getTime()
        self.__w += 1

        o *= self.__w 
        self.__output._set_input(o,self.__oindex)#Input setzen.
        self.__output.run() # Neuron Aktivieren