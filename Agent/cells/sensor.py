import time,random
from .cell import Cell
'''
Input cells
'''

class Sensor_Neuron(Cell):
    def __init__(self,id,type):
        super().__init__(id,type)
        self.current = 0
    
    def update(self,input):
        self.current = input
        # Either Update whenever the input changes, or when the entire brain does. Threading or naw.
        self.pulse()
        
    def pulse(self):
        random.shuffle(self.conn_f)
        # For each connection to the cell, add the current to the cell
        for connection in self.conn_f:
            # Conservation of charge law, some of the current is used up and released as heat, kinetic energy etc
            connection[0].current += (self.current/len(self.conn_f)*connection[1])
        # Current is used up
        self.current = 0