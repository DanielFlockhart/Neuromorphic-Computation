import numpy as np
from PIL import Image,ImageDraw
import random,math


class Visualiser:
    def __init__(self,WIDTH,HEIGHT):
        self.im = Image.new('RGB', (WIDTH, HEIGHT), (0,0,255))
        self.draw = ImageDraw.Draw(self.im)
        self.w = WIDTH
        self.h = HEIGHT
    
    def save_image(self):
        self.im.save(f'output.png', 'PNG')

    def set_image(self,pixels):
        self.im = Image.new('RGB', (self.w, self.h), (0,0,255))
        self.draw = ImageDraw.Draw(self.im)
        for y in range(self.h):
            for x in range(self.w):
                self.draw.point([x,y], (pixels[y][x],pixels[y][x],pixels[y][x]))
        self.save_image()