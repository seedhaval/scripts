import helper
import pygame


class SelCharScene:
    def __init__(self, gvar):
        self.gvar = gvar
        self.load_avatars()

    def load_avatars(self):
        y = 25
        self.gvar["avatar"] = {}
        self.gvar["pobj"] = {}
        for prsn in self.gvar["people"]:
            self.gvar["pobj"][prsn] = helper.Character(50, y, prsn, self.gvar)
            y += 225

    def show(self):
        self.gvar["screen"].fill((0, 0, 0))
        for v in self.gvar["pobj"].values():
            v.show()
        pygame.display.flip()

    def check_click(self, event):
        for k, v in self.gvar["pobj"].items():
            if v.check_if_point_contains(event.pos):
                self.gvar["char_mode_obj"].update_fl(v.fl, v.nm)
                self.gvar["current_scene"] = "base"
