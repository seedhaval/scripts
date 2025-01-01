from helper import ResizableImage
import pygame
import cfg

class SelPartScene:
    def __init__(self, gvar):
        self.gvar = gvar
    def show(self):
        nm = self.gvar["scenes"]["base"].actee.nm
        self.ar = []
        x = 0
        y = 0
        for fl in (cfg.data_dir / f"img/bp/{nm}/").glob("*.*"):
            self.ar.append(ResizableImage(str(fl), x, y, 200, 200, self.gvar))
            if x >= (cfg.screen_width - 200):
                x = 0
                y += 200
            else:
                x += 200
        self.gvar["screen"].fill((0, 0, 0))
        for elm in self.ar:
            elm.show()
        pygame.display.flip()

    def check_click(self, event):
        for elm in self.ar:
            if elm.check_if_point_contains(event.pos):
                for obj in self.gvar["carousal_mode_obj"]:
                    obj.update_fl(elm.fl)
                self.gvar["current_scene"] = "base"