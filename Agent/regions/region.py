import sys
sys.path.insert(1, r'C:\Users\green\OneDrive\Documents\GitHub\BrainSimulation\mk2')
from structures import soup_nn,feed_forward_nn

class Region:
    def __init__(self,inputs,outputs):
        self.areas = []
        self.inputs = inputs
        self.outputs = outputs
        self.encoder = feed_forward_nn.FFNN([self.inputs,self.outputs]) # width = inputs to network, height = outputs from network (arbitrary)
        self.decoder = feed_forward_nn.FFNN([self.outputs,self.outputs])

    def build(self,areas):
        for x in range(areas):
            self.areas.append(soup_nn.SNN([self.outputs,self.outputs]))

    def getOutputs(self,inputs):
        outputs = []
        for net in self.areas:
            net.process(inputs)
            outputs.append(net.getOutputs())
        return outputs

    def encode(self,inputs):
        return self.encoder.forward_pass(inputs)

    def decode(self,inputs):
        return self.decoder.forward_pass(inputs)

    def mutate(self,rate):
        for net in self.areas:
            net.mutate(rate)
        self.encoder.mutate(rate)
        self.decoder.mutate(rate)