from helper import ResizableImage
import pygame
import cfg


class SelSceneScene:
    def __init__(self, gvar):
        self.gvar = gvar

    def show(self):
        self.ar = []
        x = 0
        y = 0
        for fl in (cfg.data_dir / f"scenes").rglob("00.png"):
            nm = fl.parent.name
            self.ar.append(ResizableImage(str(fl), x, y, 200, 200, self.gvar,
                                          nm))
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
        file_ar = []
        for elm in self.ar:
            if elm.check_if_point_contains(event.pos):
                for obj in self.gvar["carousal_mode_obj"]:
                    obj.update_fl(elm.fl)
                    file_ar = (cfg.data_dir / "scenes" / elm.nm).glob("*.*")
                self.gvar["current_scene"] = "base"
                self.gvar["scene.idx"] = 0
                self.gvar["scene.file.ar"] = sorted([str(x) for x in file_ar])
