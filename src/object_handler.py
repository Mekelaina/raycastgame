from sprite_object import *
from pathlib import Path

class ObjectHandler:
    def __init__(self, game) -> None:
        self.game = game
        self.sprite_list = []
        self.respath = Path(__file__).parent.parent.joinpath('resources').as_posix()
        self.static_sprite_path = self.respath + 'sprites/static_sprites/'
        self.anim_sprite_path = self.respath + 'sprites/animated_sprites/'
        add_sprite = self.add_sprite

        # sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)