import cfg
from helper import ResizableImage, get_card_file
import pygame


class BaseScene:
    def __init__(self, gvar):
        self.gvar = gvar
        menu_top = cfg.screen_height - 200
        self.bigpart = ResizableImage(get_card_file("selopt"), 0, 0,
                                      cfg.screen_width,
                                      cfg.screen_height - 225, gvar)
        self.scene = ResizableImage(get_card_file("action"), 0, menu_top, 200,
                                    200, gvar)
        self.prev_btn = pygame.Rect(225, menu_top, 200, 200)
        self.next_btn = pygame.Rect(450, menu_top, 200, 200)
        self.gvar["scene.idx"] = 0
        self.gvar["scene.file.ar"] = []

    def show(self):
        self.gvar["screen"].fill((0, 0, 0))
        self.bigpart.show()
        self.scene.show()
        pygame.draw.rect(self.gvar["screen"], (224, 215, 255), self.prev_btn)
        pygame.draw.rect(self.gvar["screen"], (250, 255, 199), self.next_btn)
        pygame.display.flip()

    def check_click(self, event):
        if self.prev_btn.collidepoint(event.pos):
            if self.gvar["scene.idx"] > 0:
                self.gvar["scene.idx"] -= 1
                fl = self.gvar["scene.file.ar"][self.gvar["scene.idx"]]
                self.bigpart.update_fl(fl)
        elif self.next_btn.collidepoint(event.pos):
            if self.gvar["scene.idx"] + 1 < len(self.gvar["scene.file.ar"]):
                self.gvar["scene.idx"] += 1
                fl = self.gvar["scene.file.ar"][self.gvar["scene.idx"]]
                self.bigpart.update_fl(fl)
        elif self.scene.check_if_point_contains(event.pos):
            self.gvar["current_scene"] = "sel_scene"
            self.gvar["carousal_mode_obj"] = [self.bigpart]
