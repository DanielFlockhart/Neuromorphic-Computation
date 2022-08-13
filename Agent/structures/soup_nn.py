import math,random,time
from this import d
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, r'C:\Users\green\OneDrive\Documents\GitHub\BrainSimulation\mk2')

from cells.motor import Motor_Neuron
from cells.sensor import Sensor_Neuron
from cells.neuron import Neuron

# Dims = [inputs,hidden,outputs]
class SNN:
    def __init__(self,dims):
        # Dictionary of all the cell types
    
        self.dims = [dims[0],random.randint(min(dims[0],dims[1]),max(dims[0]*dims[1],100)),dims[1]]
        self.cell_types = {
            "Sensor":Sensor_Neuron,
            "Neuron":Neuron,
            "Motor":Motor_Neuron
        }
        self.build(self.dims)

    def build(self,dims):
        # Initialize All the Input nodes and output nodes.
        self.nodes = []
        for (index,cell_type) in enumerate(self.cell_types):
            self.nodes.extend([self.cell_types[cell_type](index,cell_type) for x in range(dims[index])])
        self.createConnections()

    def propogate(self):
        # Make all cells pulse
        for node in self.nodes:
            node.pulse()
    
    def createConnections(self,density=0.2):
        # Create connections between nodes
        for node in self.nodes:
            
            for x in range(int(density * self.dims[1] * self.dims[1])):
                # Get a random node
                rand_node = random.choice(self.nodes)
                # If the random node is not the same as the current node and is not a sensor
                if rand_node != node and rand_node.getType() != "Sensor":
                    # If the random node is not already connected to the current node
                    if rand_node not in node.conn_f:
                        # Add the connection
                        node.setConnection(rand_node,random.random())
    def getOutputs(self):
        # Get all the outputs
        output_nodes = []
        for node in self.nodes:
            if node.getType() == "Motor":
                output_nodes.append(node)
        
        return [1 if node.isFire() else 0 for node in output_nodes]
    
    def process(self,inputs):
        for (index,node) in enumerate(self.nodes):
            if node.getType() == "Sensor":
                node.current = inputs[index]
        self.propogate()

    def mutate(self,rate):
        for node in self.nodes:
            node.mutate(rate)

