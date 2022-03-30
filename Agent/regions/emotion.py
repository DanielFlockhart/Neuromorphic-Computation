

'''
The fitness classifier of the performance of the brain
Represents the current state of the brain, meta classification
'''
import sys
sys.path.insert(1, r'C:\Users\green\OneDrive\Documents\GitHub\BrainSimulation\mk2')
from structures import soup_nn,feed_forward_nn
from regions import region

class Emotion(region.Region):
    def __init__(self,inputs,outputs):
       super().__init__(inputs,outputs)
       self.state = 0

    def assess_state(self):
        pass
