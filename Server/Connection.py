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
    inp = Das Inputneuron zur Verbindung ( wird in __input gespeichert )
    outp = Das Outputneuron zur Verbindung ( wird in __output gespeichert )
    oindex = Der Index der Verbindung im Outputneuron ( siehe Neuron._set_input )
    net = Eigenes Neuronales Netz
    Tut:
    Initalisiert die Variablen 

    _connect_():
    Argumente:
    self: Objektinstanz
    Tut:
    holt den Wert vom Input-Neuron multipliziert den mit seinem Weigth 

    """
    def __init__(self,inp = "",outp =  "",oindex,net):
        if inp != "" and outp != "":
            self.__net = net;
            self.__weigth = 0
            self.__input = inp
            self.__output = outp
            self.__oindex = oindex
            self.__last_activation = net.getTime();
    
    def _connect_(self):
        o = self.__input._get_outputs()
        #Update des Weigths
        self.__w -= (net.getTime - self.__last_activation)
        self.__last_activation = net.getTime()
        self.__w += 1

        o *= self.__w 
        self.__output._set_input(o,self.__oindex)#Input setzen.
        self.__output.run() # Neuron Aktivieren