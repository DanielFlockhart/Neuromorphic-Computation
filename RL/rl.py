

from cv2 import sort


class RL:
    def __init__(self,population,mutation_rate):
        self.population = population
        self.mutation_rate = mutation_rate
        self.ais = []

    def nextGeneration(self):
        self.ais = self.cullGeneration(self.ais)


    def sortGeneration(self,ais):
        return ais.sort(key=lambda x: ais[x].fitness, reverse=True)

    def cullGeneration(self,ais):
        new_ais = ais[0:self.population/2]
        new_ais.extend(self.mutateGeneration(ais[0:self.population/2]))
        return new_ais

    def mutateGeneration(self,ais):
        for ai in ais:
            ai.mutate(self.mutation_rate)
        