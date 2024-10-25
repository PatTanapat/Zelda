import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import *

g_state_manager = StateMachine()

sprite_collection = SpriteManager().spriteCollection


gPlayer_animation_list = {"down": sprite_collection["character_walk_down"].animation,
                         "right": sprite_collection["character_walk_right"].animation,
                         "up": sprite_collection["character_walk_up"].animation,
                         "left": sprite_collection["character_walk_left"].animation,
                        "attack_down": sprite_collection["character_attack_down"].animation,
                        "attack_right": sprite_collection["character_attack_right"].animation,
                        "attack_up": sprite_collection["character_attack_up"].animation,
                        "attack_left": sprite_collection["character_attack_left"].animation,
                        "lift_pot_left": sprite_collection["character_lift_pot_left"].animation,
                        "lift_pot_right": sprite_collection["character_lift_pot_right"].animation,
                        "lift_pot_up": sprite_collection["character_lift_pot_up"].animation,
                        "lift_pot_down": sprite_collection["character_lift_pot_down"].animation,
                        "walk_pot_left": sprite_collection["character_walk_pot_left"].animation,
                        "walk_pot_right": sprite_collection["character_walk_pot_right"].animation,
                        "walk_pot_up": sprite_collection["character_walk_pot_up"].animation,
                        "walk_pot_down": sprite_collection["character_walk_pot_down"].animation
                        # "throw_pot_down": sprite_collection["character_throw_pot_down"].animation,
                        # "throw_pot_right": sprite_collection["character_right"].animation,
                        # "throw_pot_up": sprite_collection["character_up"].animation,
                        # "throw_pot_left": sprite_collection["character_left"].animation
                        
}

gSkeleton_animation_list = {"down": sprite_collection["skeleton_walk_down"].animation,
                         "right": sprite_collection["skeleton_walk_right"].animation,
                         "up": sprite_collection["skeleton_walk_up"].animation,
                         "left": sprite_collection["skeleton_walk_left"].animation,
}

gpot_image_list =[sprite_collection['pot_1'].image,sprite_collection["pot_2"].image]


gHeart_image_list = [sprite_collection["heart_0"].image,sprite_collection["heart_2"].image,
                    sprite_collection["heart_4"].image]

gRoom_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16)
gDoor_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16, colorkey=(13, 7, 17, 255))
gSwitch_image_list = Util.GenerateTiles("./graphics/switches.png", 16, 18)

gSounds = {
    'music': pygame.mixer.Sound('sounds/music.mp3'),
    'sword':  pygame.mixer.Sound('sounds/sword.wav'),
    'hit_enemy':  pygame.mixer.Sound('sounds/hit_enemy.wav'),
    'hit_player':  pygame.mixer.Sound('sounds/hit_player.wav'),
    'door':  pygame.mixer.Sound('sounds/door.wav'),
    'shield_defense_up':  pygame.mixer.Sound('sounds/powerup.wav'),
    'healing':  pygame.mixer.Sound('sounds/heal.mp3')

}

gFonts = {
    'small': pygame.font.Font('fonts/font.ttf', 24),
    'medium': pygame.font.Font('fonts/font.ttf', 48),
    'large': pygame.font.Font('fonts/font.ttf', 96),
    'zelda_small': pygame.font.Font('fonts/zelda.otf', 96),
    'zelda': pygame.font.Font('fonts/zelda.otf', 192),
    'gothic_medium': pygame.font.Font('fonts/GothicPixels.ttf', 48),
    'gothic_large': pygame.font.Font('fonts/GothicPixels.ttf', 96),

}