import time,random,sys
sys.path.insert(1, r'C:\Users\green\OneDrive\Documents\GitHub\BrainSimulation\mk2\Agent\cells')
import cell


class Neuron(cell.Cell):
    def __init__(self,id,type):
        super().__init__(id,type)
        self.current = 0

    # Could either work by connections, or by distance to the cell which would be the magnitude of the current.
    def pulse(self):
        random.shuffle(self.conn_f)
        # For each connection to the cell, add the current to the cell
        for connection in self.conn_f:
            # Conservation of charge law, some of the current is used up and released as heat, kinetic energy etc
            connection[0].current += (self.current/len(self.conn_f)*connection[1])

        # Current is used up
        self.current = 0