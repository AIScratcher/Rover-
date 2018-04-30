"""
@author: aiscratch
@version: 1.0.0
"""

import numpy as np
import Connection

class Neuron(object):
    """
        A Neuron is just this set of values:
        float: Theta
        float : Psi
        list : inputs:
        inputs : 0 : W of f
        inputs : 1 : W of c
        inputs : 2 : W of b
        inputs : 3 : N of f
        inputs : 4 : N of c
        inputs : 5 : N of b
        Theta and Psi are Treshholds
        And the list inputs is the storage of the Input
        That's just 6 values who are just the w of the input
        And after that is the size of the (!)connected fields

    """
    def add_output_con(self,con):
        #If a new output connection appends that will note if
        #the output changes
        self.__output_table.append(con)

    def __init__(self,input_layer,layer,
                theta=np.random.uniform(0.01),
                psi=np.random.uniform(0.01)):

                self.theta, self.psi,self.tresh_pool_c = theta,psi,np.random.uniform(0.01) #Hyperparameters
                #Connect to input_layer
                self.__connect_to_layer(input_layer,2,0)
                self.__input_layer, self.__layer = input_layer,layer
                self.output = 0
                
    #Connect to the own layer
    def build_layer(self):
        self.__connect_to_layer(self.__layer,2,1)
    #Connect to next layer
    def after_build(self,output_layer):
        self.__connect_to_layer(output_layer,2,2)
        self.__output_layer = output_layer




    #Common function to connect this Neuron to a layer
    def __connect_to_layer(self,layer,p_not_connect,type):
        #Connect this Neuron to a layer with a percentage of p_not_connect
        #of unconnected neurons
        #Need for connecting later
        input_layer_neurons = list(layer.get_neurons())
        #If this is a connection between the same layer
        #this Neuron should not connect to itself
        if self in input_layer_neurons:
            input_layer_neurons.remove(self)
        #Number of neurons not will connect as int
        number_of_unconnected = int(layer.size()/100*p_not_connect)
        #The group of Neurons indicies in input_layer_neurons
        unconnected_indexs = np.zeros(number_of_unconnected)
        #Find random numbers:
        index = 0
        while(index < number_of_unconnected):
            random_number = np.int(np.random.uniform(0,layer.size()))
            if random_number in unconnected_indexs:
                continue
            unconnected_indexs[index] = random_number
            index += 1
        #Connect to all Neurons ( those who are not in unconnected_indexs)
        for index in range(0,len(input_layer_neurons)):
            if not index in unconnected_indexs:
                #New Connection
                Connection.Connection(type,input_layer_neurons[index],self)

    #If you want to execute a Neuron totaly there are 3 Steps, wich will execute
    #the Layer if it has enough data for this step
    #1.Feedforward predicting
    #2.Context pooling
    #3.Feedback pooling
    #Because each step must run with the whole Layer it's split about 3
    # diffrent methods called by the Layer if it's ready
    #For better explenation see the README.md in the Server directory

    #1.Feedforward predicting
    def r_predicting(self):
        if self.inputs[0] / self.inputs[3] > self.theta: #First Treshold
            self.output = 1
            self.__output_table[:].connect()
        else:
            self.output = 0
        return
    #2.Context pooling
    def r_c_pooling(self):
        #This will only execute if the output is 1
        #Pooling is the process of learning a specific template in the inputs
        #First test if the output and the context are good
        if self.inputs[1] / self.inputs[4] > self.tresh_pool_c:
            #The Context said: Yes we also think thats rigth what you said
            #You can try to decrement a little
            self.theta -= 0.045 #Random number but smaller as the number in else
        else:
            #The Context said you are wrong you must be more critical:
            #Increment the theta
            self.theta += 0.1
    #3.Feedback pooling
    def r_b_pooling(self):
        #Do the same but now work with the tresh_pool_c
        #Now we use a const, the lambada, I'm not lucky with this solution
        #but before this will work in a large scale that and many more things
        #in the theory must be fixed
        #Again that will just execute if the output is 1
        if self.inputs[2] / self.inputs[5] > self.lambada:
            #Again slow down to a perfect value and never stand at one point
            self.tresh_pool_c -= 0.034
        else:
            self.tresh_pool_c += 0.7
        #Feedback Pooling is slower and not so fast changing how the context
