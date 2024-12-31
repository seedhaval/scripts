import cfg
from helper import ResizableImage, get_card_file
import pygame

class BaseScene:
    def __init__(self, gvar):
        self.gvar = gvar
        menu_top = cfg.screen_height - 125
        self.bigpart = ResizableImage(get_card_file("selopt"), 0, 0,
                                      cfg.screen_width,
                                      cfg.screen_height - 150,gvar)
        self.actor = ResizableImage(get_card_file("actor"), 0, menu_top, 100,
                                    100,gvar)
        self.actee = ResizableImage(get_card_file("actee"), 125, menu_top, 100,
                                    100,gvar)
        self.part = ResizableImage(get_card_file("part"), 250, menu_top, 100,
                                   100,gvar)
        self.action = ResizableImage(get_card_file("action"), 375, menu_top,
                                     100,
                                     100,gvar)

    def show(self):
        self.gvar["screen"].fill((0, 0, 0))
        self.bigpart.show()
        self.actor.show()
        self.actee.show()
        self.part.show()
        self.action.show()
        pygame.display.flip()

    def check_click(self, event):
        if self.actor.check_if_point_contains(event.pos):
            self.gvar["char_mode_obj"] = self.actor
            self.gvar["current_scene"] = "sel_char"
        elif self.actee.check_if_point_contains(event.pos):
            self.gvar["char_mode_obj"] = self.actee
            self.gvar["current_scene"] = "sel_char"
        elif self.action.check_if_point_contains(event.pos):
            self.gvar["carousal_mode_obj"] = [self.action]
            self.gvar["current_scene"] = "sel_action"
        elif self.part.check_if_point_contains(event.pos):
            self.gvar["carousal_mode_obj"] = [self.part, self.bigpart]
            self.gvar["current_scene"] = "sel_part"


