from src.EntityBase import EntityBase
from src.Dependencies import *
from src.recourses import *

class Player(EntityBase):
    def __init__(self, conf , dungeon= None):
        super(Player, self).__init__(conf)
        self.dungeon = dungeon

    def update(self, dt, events):
        super().update(dt, events)


    def Collides(self, target):
        y, height = self.y + self.height/2, self.height-self.height/2

        return not (self.x + self.width < target.x or self.x > target.x + target.width or
                    y + height < target.y or y > target.y + target.height)

    def PotCollides(self, target):
       return not (
            self.rect.x + self.width < target.rect.x or
            self.rect.x > target.rect.x + target.width or
            self.rect.y + self.height < target.rect.y or
            self.rect.y > target.rect.y + target.height
        )

    def render(self):
        super().render()

    def CreateAnimations(self):
        self.animation_list = gPlayer_animation_list