
'''
The main processing region the brain

Continuous activation spiking neural network
Regional Biases

'''
import sys
sys.path.insert(1, r'C:\Users\green\OneDrive\Documents\GitHub\BrainSimulation\mk2')
from structures import soup_nn,feed_forward_nn
from regions import region

class Processor(region.Region):
    def __init__(self,inputs,outputs):
        super().__init__(inputs,outputs)