import math,random,time
import numpy as np
from brain import Brain
from visualiser import Visualiser

if __name__ == "__main__":
    brain = Brain(512,31)
    brain.build()
    for x in range(100):
        brain.getInputs()
        outputs = brain.process()
        #brain.controller.process(outputs)
        