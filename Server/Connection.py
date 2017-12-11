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
    Tut:
    Initalisiert die Variablen 

    """
    def __init__(self,inp,outp,oindex):
        self.__weigth = 0
        self.__input = inp
        self.__output = outp
        self.__oindex = oindex
    
    def _connect_(self):
        o = self.__input._get_outputs()
        self.__output._set_input(o,oindex):