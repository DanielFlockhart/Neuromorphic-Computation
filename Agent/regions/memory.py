

'''
Storing information in memory

every cell is connected to every other cell, but there is an exponential drop off in the connection strength
'''
import sys

from sklearn.metrics import accuracy_score
sys.path.insert(1, r'C:\Users\green\OneDrive\Documents\GitHub\BrainSimulation\mk2')
from structures import soup_nn,feed_forward_nn
from regions import region
class Memory(region.Region):
    def __init__(self,inputs,outputs):
        super().__init__(inputs,outputs)
        self.memories = []

    def create_memory(self,inputs,outputs):
        memory = [inputs,outputs]
        self.memories.append(memory)

    # If a set of inputs to the brain are similar to that of memory of inputs, the corresponding neural network will be used to process the memory
    def check_memory(self,inputs,sensitivity = 0.9):
        for memory in self.memories:
            if self.get_similarity(inputs,memory[0],sensitivity):
                return memory[1]
        return None

    def get_similarity(self,inputs,mem_inputs,sensitivity):
        for i in range(len(mem_inputs)):
            accuracy_score = 0
            for x in range(len(inputs)):
                accuracy_score += abs(mem_inputs[i][x] - inputs[i])
            accuracy_score = accuracy_score / len(inputs)
            if accuracy_score < 1-sensitivity:
                return True
        return False