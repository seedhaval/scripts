import pygame
import cfg
import base_scene
import sel_scene_scene

screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))
pygame.init()
gvar = {"screen": screen}

def start():
    running = True
    updated = False
    while running:
        clock = pygame.time.Clock()
        clock.tick(cfg.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                gvar["scenes"][gvar["current_scene"]].check_click(event)
                updated = True
        if updated or gvar["scenes"]["base"].is_animating:
            gvar["scenes"][gvar["current_scene"]].show()
            updated = False
    pygame.quit()


if __name__ == '__main__':
    gvar["scenes"] = {
        "sel_scene": sel_scene_scene.SelSceneScene(gvar),
        "base": base_scene.BaseScene(gvar)
    }
    gvar["current_scene"] = "base"
    gvar["scenes"][gvar["current_scene"]].show()
    start()
