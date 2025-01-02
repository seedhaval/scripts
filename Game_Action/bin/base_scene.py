import shutil

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
        self.go_btn = pygame.Rect(675, menu_top, 200, 200)
        self.gvar["scene.idx"] = 0
        self.gvar["scene.file.ar"] = []
        self.is_animating = False
        self.speed_ar = [0.5, 1, 0.25]
        self.speed_idx = 0
        self.recalc_wait_parms()
        self.cur_nm = ""

    def recalc_wait_parms(self):
        self.wait_sec = self.speed_ar[self.speed_idx]
        self.wait_counter_ref = cfg.fps * self.wait_sec
        self.wait_counter = self.wait_counter_ref

    def show(self):
        self.gvar["screen"].fill((0, 0, 0))
        self.bigpart.show()
        self.scene.show()
        pygame.draw.rect(self.gvar["screen"], (224, 215, 255), self.prev_btn)
        pygame.draw.rect(self.gvar["screen"], (250, 255, 199), self.next_btn)
        pygame.draw.rect(self.gvar["screen"], (186, 255, 201), self.go_btn)
        if self.is_animating:
            self.wait_counter -= 1
            if self.wait_counter < 0:
                self.wait_counter = self.wait_counter_ref
                self.gvar["scene.idx"] = (self.gvar["scene.idx"] + 1) % len(
                    self.gvar["scene.file.ar"])
                fl = self.gvar["scene.file.ar"][self.gvar["scene.idx"]]
                self.bigpart.update_fl(fl)
        pygame.display.flip()

    def start_animation(self):
        self.is_animating = True
        self.wait_counter = self.wait_counter_ref

    def stop_animation(self):
        self.is_animating = False

    def load_next_tmp_scene(self):
        self.stop_animation()
        fldr = [x for x in (cfg.data_dir / "tmp").glob("*") if x.is_dir()][0]
        fls = [str(x) for x in fldr.glob("*.png")]
        self.gvar["scene.file.ar"] = fls
        self.gvar["scene.idx"] = 0
        self.cur_nm = fldr.name
        self.start_animation()

    def check_click(self, event):
        if self.prev_btn.collidepoint(event.pos):
            if self.cur_nm != "":
                shutil.rmtree(cfg.data_dir / "tmp" / self.cur_nm)
            self.load_next_tmp_scene()
        elif self.next_btn.collidepoint(event.pos):
            if self.cur_nm != "":
                shutil.copytree(cfg.data_dir / "tmp" / self.cur_nm,
                                cfg.data_dir / "scenes" / self.cur_nm)
                shutil.rmtree(cfg.data_dir / "tmp" / self.cur_nm)
            self.load_next_tmp_scene()
        elif self.scene.check_if_point_contains(event.pos):
            self.gvar["current_scene"] = "sel_scene"
            self.gvar["carousal_mode_obj"] = [self.bigpart]
            self.stop_animation()
        elif self.go_btn.collidepoint(event.pos):
            self.speed_idx = (self.speed_idx + 1) % len(self.speed_ar)
            self.recalc_wait_parms()
            self.start_animation()
