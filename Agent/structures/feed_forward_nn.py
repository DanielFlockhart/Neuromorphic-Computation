
import math,random,time
class FFNN:
    def __init__(self,dims):
        self.layers = dims
        # Initialize weights and biases
        self.weights = [[[random.uniform(-1.0,1.0) for z in range(dims[layer])] for x in range(dims[layer+1])] for layer in range(len(dims)-1)]
        self.biases = [[random.uniform(-1.0,1.0) for x in range(dims[layer+1])] for layer in range(len(dims)-1)]

    # Activation Function to create non linear behavior
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))


    # Iterate through each layer with the output of one layer being the input of the next
    def forward_pass(self,inputs):
        for layer in range(len(self.layers)-1):
            inputs = [self.sigmoid(sum([input * weight for input,weight in zip(inputs,self.weights[layer][node])])+self.biases[layer][node])for node in range(self.layers[layer+1])]
            
        return inputs

    # Iterate through the weights and biases, randomly mutate them depending on random chance.
    def mutate(self,mutation_rate):
        for layer in range(len(self.weights)):
            for weights in range(len(self.weights[layer])):
                if random.random() < mutation_rate:
                    self.biases[layer][weights] = random.uniform(-1.0,1.0)   
                for weight in range(len(self.weights[layer][weights])):
                    if random.random() < mutation_rate:
                        self.weights[layer][weights][weight] = random.uniform(-1.0,1.0)

