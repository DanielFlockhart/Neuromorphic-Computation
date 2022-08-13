import re
from shutil import register_unpack_format
import time,random
from .cell import Cell

'''
Output cells
'''
class Motor_Neuron(Cell):
    def __init__(self,id,type):
        super().__init__(id,type)
        self.current = 0

    def pulse(self):
        pass
    
    def isFire(self):
        
        if self.current >= 1:
            self.current = 0
            return True
        elif self.current < 0:
            #self.current = 0
            return False