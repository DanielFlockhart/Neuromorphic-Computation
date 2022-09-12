**Neuro Morphic Computation**
<br>
Work in progress project - Long way off completion
<br>

**_The Soup Neural Network_**

The soup neural network is an attempt at modeling the way data flows in the human brain. Much like the human brain, a SNN Consists of a bunch of neurons with connections to other neurons. Some of the neurons are input neurons and some are output nodes. Much like the idea of NEAT (The Neuro-Evolutionary Algorithm of Augmenting Topologies) where the network not only learns the weights and biases but also the topology, there is not a set structure to the network. 

In contrast to NEAT, data is not propagated all the way through the network each iteration, it performs a breadth-first like pass and does not reset its nodes values every pass. Additionally, it has current spiking style activation; on the motor neurons (output nodes), if the current received is greater than 1, it fires. During the propagation stage, each node propagates a current, relative to the number of connections (conservation of current) multiplied by a weight.

I have had a few ideas for the way the soup neural network should work. For the moment I have settled on the idea mentioned above. This is likely to change.
