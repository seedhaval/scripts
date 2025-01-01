import pygame
import cfg
import json
import pygame.freetype


class ResizableImage:
    def __init__(self, fl, x, y, max_width, max_height, gvar, nm=None):
        self.x = x
        self.y = y
        self.max_width = max_width
        self.max_height = max_height
        self.fl = fl
        self.nm = nm
        self.recalc()
        self.gvar = gvar

    def recalc(self):
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

    def update_fl(self, fl, nm=None):
        self.fl = fl
        self.nm = nm
        self.recalc()

    def show(self):
        self.gvar["screen"].blit(self.img, (self.x + self.offset_x, self.y +
                                            self.offset_y))

    def check_if_point_contains(self, pos):
        return self.img.get_rect(topleft=(self.x, self.y)).collidepoint(pos)


def get_card_file(nm):
    return f"{cfg.data_dir}/card/{nm}.png"
