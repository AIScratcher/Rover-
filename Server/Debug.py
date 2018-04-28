import numpy as np

class psd_layer(object):

    def __init__(self, size):
        #size = total length of the Layer
        self.__size = size
    def size(self):
        return self.__size
    def get_neurons(self):
        return np.zeros(self.__size)
