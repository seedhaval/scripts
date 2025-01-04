import pygame
import pygame.freetype
import cfg
import helper
from scene_location import LocationScene

screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))
pygame.init()
gvar = {
    "screen": screen,
    "map": helper.load_map(),
    "font": pygame.freetype.Font(cfg.cfg_dir / "fonts" / "Roboto.ttf", 36)
}

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
    gvar["scenes"] = {
        "location": LocationScene(gvar)
    }
    gvar["current_scene"] = "location"
    gvar["scenes"][gvar["current_scene"]].show()
    start()
