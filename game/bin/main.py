import pygame

import cfg

import base_scene
import sel_char_scene
import sel_part_scene
import sel_action_scene
import helper

screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))
pygame.init()
gvar = {"screen": screen}


def start():
    running = True
    updated = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                gvar["scenes"][gvar["current_scene"]].check_click(event)
                updated = True
        if updated:
            gvar["scenes"][gvar["current_scene"]].show()
            updated = False
    pygame.quit()


if __name__ == '__main__':
    helper.load_static_values(gvar)
    gvar["scenes"] = {
        "sel_char": sel_char_scene.SelCharScene(gvar),
        "base": base_scene.BaseScene(gvar),
        "sel_action": sel_action_scene.SelActionScene(gvar),
        "sel_part": sel_part_scene.SelPartScene(gvar)
    }
    gvar["current_scene"] = "base"
    gvar["scenes"][gvar["current_scene"]].show()
    start()
