from helper import ResizableImage
import pygame
import cfg
from pathlib import Path
from random import shuffle

class SelSceneScene:
    def __init__(self, gvar):
        self.gvar = gvar

    def show(self):
        self.ar = []
        x = 0
        y = 0
        fl_ar = sorted([str(x) for x in (cfg.data_dir / "scenes").rglob("00.png")])
        if len(fl_ar) > 24:
            out_ar = fl_ar[:-3]
            shuffle(out_ar)
            out_ar = [*out_ar[:21],*fl_ar[-3:]]
        else:
            out_ar = fl_ar

        for fl in out_ar:
            nm = Path(fl).parent.name
            self.ar.append(ResizableImage(str(fl), x, y, 320, 180, self.gvar,
                                          nm))
            if x >= (cfg.screen_width - 340):
                x = 0
                y += 200
            else:
                x += 340
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
