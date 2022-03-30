import random,math
'''
Superclass of all cells.
Can get all the cells close to it and their distances.
This has basic functionality for all cells
'''
class Cell:
    def __init__(self,id,type):
        self.type = type
        self.id = id
        # In the form of (cell,weight)
        self.conn_f = []

    # Get the cell type
    def getType(self):
        return self.type
    

    def setConnection(self,cell,weight):
        self.conn_f.append((cell,weight))
    
    def mutate(self,rate):
        for con in self.conn_f:
            if random.random() < rate:
                con[1] = random.random()
        

    