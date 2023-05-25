import pygame as pg
from settings import *
from pathlib import Path

class ObjectRenderer:
    def __init__(self, game) -> None:
        self.game = game
        self.screen = game.screen
        self.respath = Path(__file__).parent.parent.joinpath('resources')
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_game_objects()

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return {
            1: self.get_texture(self.respath.joinpath('textures/1.png')),
            2: self.get_texture(self.respath.joinpath('textures/2.png')),
            3: self.get_texture(self.respath.joinpath('textures/3.png')),
            4: self.get_texture(self.respath.joinpath('textures/4.png')),
            5: self.get_texture(self.respath.joinpath('textures/5.png')),
        }