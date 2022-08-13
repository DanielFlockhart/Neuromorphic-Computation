import math,random,time
import numpy as np
from brain import Brain
from visualiser import Visualiser

if __name__ == "__main__":
    brain = Brain(528,10)
    brain.build()
    total = 0
    for x in range(100000):
        brain.getInputs()
        outputs = brain.process()
        print(sum(outputs)/100)
        #brain.controller.process(outputs)
        