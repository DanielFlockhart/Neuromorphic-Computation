import cell

'''
holds information about a part of a specific memory, 
in the event that the inputs to a brain are similar a previous memory, the neural network that was used to 
learn the previous memory will be used to learn the new memory,
Therefore, there are going to be lots of seperate neural networks

'''

# Stores the inputs of the brain to an array that can be compared to the inputs of other memories when they are created
# Stores the neural network
class Memory_Neuron(cell.Cell):
    def __init__(self,id,type):
        super().__init__(id,type)
        self.charge = 0

        
        