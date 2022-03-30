from hashlib import new
import random,time
from regions import *
from cells import *
from regions.emotion import *
from regions.memory import *
from regions.processing import *
from sensors import *
import numpy as np
import pyautogui
from sensors import sight
import controller

class Brain:
    def __init__(self,input_count,output_count):
        dims = [input_count,output_count]
        self.sensors = [sight.Screen(),sight.Webcam()]
        self.processing = Processor(dims[0],dims[1])
        self.memory = Memory(dims[0],dims[1])
        self.emotion = Emotion(dims[0],dims[1])
        self.encoder = feed_forward_nn.FFNN([dims[0],dims[1]])
        self.decoder = feed_forward_nn.FFNN([dims[1],dims[1]]) 
        self.regions = [self.processing,self.memory,self.emotion]

        self.memory_strength_requirement = 0.9
        self.inputs = []
        # Stored values of the 5 most recent inputs to the brain to use for memory storage
        self.stored_inputs = []

        self.controller = controller.Controller()
        self.fitness = 0

    def build(self):
        for region in self.regions:
            region.build(4)
    
    def mutate(self,rate):
        for region in self.regions:
            region.mutate(rate)

    def process(self):
        outputs = []
        inputs = self.encode(self.inputs)
        self.stored_inputs.append(inputs)
        self.stored_inputs = self.stored_inputs[-5:]
        # First check memory to see if previous inputs are similar (Maybe check similarity of multiple inputs?)
        # If similar, skip processing and use memory
        loaded_memory = self.memory.check_memory(inputs,self.memory_strength_requirement)
        if loaded_memory != None:
            return loaded_memory

        # Temporary Fix for processing
        new_inputs = self.processing.encode(inputs)
        new_inputs = self.processing.getOutputs(new_inputs)
        new_inputs = [item for sublist in new_inputs for item in sublist]
        new_inputs = self.processing.decode(new_inputs)
        outputs.append(new_inputs)
        
        outputs = [item for sublist in outputs for item in sublist]
        outputs = self.decode(outputs)
        # Create Memory if positive state
        self.emotion.assess_state()
        if self.emotion.state > self.memory_strength_requirement:
            print("Created Memory")
            self.memory.create_memory(self.stored_inputs,outputs)
        return outputs


    def encode(self,inputs):
        return self.encoder.forward_pass(inputs)

    def decode(self,inputs):
        return self.normalize(self.decoder.forward_pass(inputs)) # Pass through output network and normalize using softmax function

    def normalize(self,inputs): # If negative make output -1, if positive make output 1, might change this to make continuous output
        out = []
        for i in inputs:
            out.append(i * 2 - 1)
        return out

    def getInputs(self):
        self.inputs = []
        self.sensors[0].run()
        self.sensors[1].run()
        self.inputs.extend([pyautogui.position()[0]/pyautogui.size()[0],pyautogui.position()[1]/pyautogui.size()[1]])
        self.inputs.extend(self.sensors[0].getOutput())
        self.inputs.extend(self.sensors[1].getOutput())
            

'''
Each region has its own areas
each area is made up of a soup neural network
each region has an encoder feed forward neural network that takes the outputs of the soup neural networks as its input

Every feed forward neural network to each region feeds into a larger feed forward neural network that controls the output of the brain
and the action it does

Region:
    - processing
        - Area 1
        - Area 2
    - memory
        - Area 1
        - Area 2
    - emotion
        - Area 1
        - Area 2

'''