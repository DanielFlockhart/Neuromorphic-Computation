import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import sys
sys.path.insert(1, r'C:\Users\green\OneDrive\Documents\GitHub\BrainSimulation\mk2')
from cells.neuron import Neuron





class NetVisuals:
    def __init__(self,screensize):
        self.root = tk.Tk()
        (self.width,self.height) = screensize
        self.canvas = tk.Canvas(self.root,width=1000, height=1000)
        self.canvas.pack()
    def plotgraph(self,x,y):
        plt.plot(x, y)
        
    def showgraph(self):
        plt.show()
    def create_circle(self,x, y, r,type):
        col = "white"
        if(type == "input"):
            col = "black"
        if(type == "output"):
            col = "grey"
        return self.canvas.create_oval(x - r, y - r, x + r, y + r,fill=col)

    def create_line(self,point1,point2,weight):
        return self.canvas.create_line(point1[0], point1[1], point2[0], point2[1],fill="green" if weight > 0 else "red")
    
    def build(self,nodes):
        for node in nodes:
            self.create_circle(self.convert_pos(node.pos)[0],self.convert_pos(node.pos)[1],10,node.type)
        
        for node in nodes:
            for connection in node.connections:
                self.create_line(self.convert_pos(node.pos),self.convert_pos(connection[0].pos),connection[1])
    
    def convert_pos(self,pos):
        return (pos[0]* self.width,pos[1] * self.height)

    def render(self):
        self.root.mainloop()

if __name__ == "__main__":
    net = NetVisuals((1000,1000))
    net.build([Neuron(i,"Neuron") for i in range(100)])
    net.render()
    net.showgraph()