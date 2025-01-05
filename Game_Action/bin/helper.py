import pygame
import cfg
import json
import pygame.freetype


class GameActionObject:
    def __init__(self, gvar):
        self.gvar = gvar
        self.screen = self.gvar["screen"]


class ResizableImage(GameActionObject):
    def __init__(self, nm, x, y, max_width, max_height, gvar):
        super().__init__(gvar)
        self.nm = nm
        self.x = x
        self.y = y
        self.max_width = max_width
        self.max_height = max_height
        self.recalc()

    def recalc(self):
        self.fl = list((cfg.data_dir / "img").rglob(f"{self.nm}.*"))[0]
        self.img = pygame.image.load(self.fl)
        img_rect = self.img.get_rect()
        scale_width = self.max_width
        scale_height = self.max_height
        aspect_ratio = img_rect.width / img_rect.height
        if self.max_width / self.max_height > aspect_ratio:
            scale_width = int(self.max_height * aspect_ratio)
        else:
            scale_height = int(self.max_width / aspect_ratio)
        self.img = pygame.transform.scale(self.img, (scale_width, scale_height))
        self.offset_x = (self.max_width - scale_width) // 2
        self.offset_y = (self.max_height - scale_height) // 2

    def update_fl(self, nm):
        self.nm = nm
        self.recalc()

    def show(self):
        self.screen.blit(self.img, (self.x + self.offset_x, self.y +
                                    self.offset_y))

    def check_if_point_contains(self, pos):
        return self.img.get_rect(topleft=(self.x, self.y)).collidepoint(pos)


class SelectableImage(GameActionObject):
    def __init__(self, gvar, idx, img, nm, x, y):
        super().__init__(gvar)
        self.idx = idx
        self.img = img
        self.nm = nm
        self.x = x
        self.y = y
        self.frame_obj = ResizableImage("frame1", x, y, 400, 400, gvar)
        self.img_obj = ResizableImage(img, x + 50, y + 10, 300, 300, gvar)

    def show(self):
        self.frame_obj.show()
        if self.img_obj is None:
            return
        self.img_obj.show()
        self.gvar["font"].render_to(self.screen, (self.x + 50, self.y + 340),
                                    self.nm, (255, 255, 255))

    def is_clicked(self, pos):
        if self.img is None:
            return False
        return self.frame_obj.check_if_point_contains(pos)

    def clear(self):
        self.img_obj = None
        self.nm = None

    def set_img(self, idx, img, nm):
        self.idx = idx
        self.img = img
        self.nm = nm
        if self.img is not None:
            self.img_obj.update_fl(img)

    def get_dict(self):
        return {
            "idx": self.idx,
            "name": self.nm,
            "img": self.img
        }


class PersistentSelectableImage(SelectableImage):
    def __init__(self, gvar, idx, img, nm, x, y):
        super().__init__(gvar, idx, img, nm, x, y)
        self.frame_obj = ResizableImage("frame1", x, y, 300, 300, gvar)
        self.img_obj = ResizableImage(img, x + 20, y + 20, 260, 260, gvar)
        self.is_selected = True

    def show(self):
        self.frame_obj.show()
        if self.img_obj is None:
            return
        self.img_obj.show()

    def select(self, hl_typ):
        self.is_selected = True
        if hl_typ == 1:
            self.highlight_type_1()
        elif hl_typ == 2:
            self.highlight_type_2()

    def unselect(self):
        self.is_selected = False
        self.unhighlight()

    def highlight_type_1(self):
        self.frame_obj.update_fl("frame2")

    def highlight_type_2(self):
        self.frame_obj.update_fl("frame3")

    def unhighlight(self):
        self.frame_obj.update_fl("frame1")


class OnOffSwitch(ResizableImage):
    def __init__(self, gvar, x, y, width, height, on_nm, off_nm):
        super().__init__(on_nm, x, y, width, height, gvar)
        self.status = "on"
        self.on_mn = on_nm
        self.off_nm = off_nm

    def on(self):
        self.status = "on"
        self.update_fl(self.on_mn)

    def off(self):
        self.status = "off"
        self.update_fl(self.off_nm)

    def check_if_point_contains(self, pos):
        if self.status == "off":
            return False
        return super().check_if_point_contains(pos)


def load_map():
    ln_ar = (cfg.cfg_dir / "map.txt").read_text().splitlines()
    data = {
        "person": {},
        "location": {},
        "action": {}
    }
    for ln in ln_ar:
        ar = ln.strip().split(",")
        if len(ar) == 0:
            continue
        if ar[0] == "p":
            data["person"][ar[1]] = {
                "gender": ar[2]
            }
        elif ar[0] == "l":
            data["location"][ar[1]] = {
                "name": ar[2],
                "img": ar[3],
                "children": ar[4].split(),
                "actions": ar[5].split()
            }
        elif ar[0] == "a":
            data["action"][ar[1]] = {
                "name": ar[2],
                "img": ar[3],
                "children": ar[4].split(),
                "allowed_genders": ar[5].split()
            }
    return data
