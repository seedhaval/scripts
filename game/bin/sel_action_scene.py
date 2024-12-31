from helper import ResizableImage
import pygame
import cfg


class SelActionScene:
    def __init__(self, gvar):
        self.ar = []
        x = 0
        y = 0
        for fl in (cfg.data_dir / "img/action").glob("*.*"):
            self.ar.append(ResizableImage(str(fl), x, y, 200, 200, gvar))
            if x >= (cfg.screen_width - 200):
                x = 0
                y += 200
            else:
                x += 200
        self.gvar = gvar

    def show(self):
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
