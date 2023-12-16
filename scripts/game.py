import pygame
import os
from scripts.functions import load_image
class Game():
    def __init__(self):
        self.background=load_image("assets","images","background.png"))
        

    def render(self,surface: pygame.Surface) -> None:
        surface.blit(self.background,(0,0))