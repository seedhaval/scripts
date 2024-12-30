import pygame
import cfg
import json
import pygame.freetype

gvar = {}
screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))
pygame.init()

game_font = pygame.freetype.Font(
    f"{cfg.data_dir}/fonts/air_mitalic.ttf", 48)


def get_card_file(nm):
    return f"{cfg.data_dir}/img/card/{nm}.png"


def load_static_values():
    gvar.update(json.loads((cfg.data_dir / "config.json").read_text()))


class Character():
    def __init__(self, x, y, prsn):
        super().__init__()
        self.fl = f"{cfg.data_dir}/img/avatars/{prsn}.png"
        self.img = pygame.image.load(self.fl).convert_alpha()
        self.x = x
        self.y = y
        self.person_name = prsn
        self.font_clr = (255, 255, 255)

    def check_if_point_contains(self, pos):
        return self.img.get_rect(topleft=(self.x, self.y)).collidepoint(pos)

    def show(self):
        screen.blit(self.img, (self.x, self.y))
        game_font.render_to(screen, (self.x + 225, self.y + 75),
                            self.person_name, self.font_clr)


class ResizableImage:
    def __init__(self, fl, x, y, max_width, max_height):
        self.x = x
        self.y = y
        self.max_width = max_width
        self.max_height = max_height
        self.fl = fl
        self.recalc()

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

    def update_fl(self, fl):
        self.fl = fl
        self.recalc()

    def show(self):
        screen.blit(self.img, (self.x + self.offset_x, self.y + self.offset_y))

    def check_if_point_contains(self, pos):
        return self.img.get_rect(topleft=(self.x, self.y)).collidepoint(pos)


class BaseScene:
    def __init__(self):
        menu_top = cfg.screen_height - 125
        self.bigpart = ResizableImage(get_card_file("selopt"), 0, 0, cfg.screen_width,
                                      cfg.screen_height - 150)
        self.actor = ResizableImage(get_card_file("actor"), 0, menu_top, 100,
                                    100)
        self.actee = ResizableImage(get_card_file("actee"), 125, menu_top, 100,
                                    100)
        self.part = ResizableImage(get_card_file("part"), 250, menu_top, 100,
                                   100)
        self.action = ResizableImage(get_card_file("action"), 375, menu_top,
                                     100,
                                     100)

    def show(self):
        screen.fill((0, 0, 0))
        self.bigpart.show()
        self.actor.show()
        self.actee.show()
        self.part.show()
        self.action.show()
        pygame.display.flip()

    def check_click(self, event):
        if self.actor.check_if_point_contains(event.pos):
            gvar["char_mode_obj"] = self.actor
            gvar["current_scene"] = "sel_char"
        elif self.actee.check_if_point_contains(event.pos):
            gvar["char_mode_obj"] = self.actee
            gvar["current_scene"] = "sel_char"
        elif self.action.check_if_point_contains(event.pos):
            gvar["carousal_mode_obj"] = self.action
            gvar["current_scene"] = "sel_action"


class SelActionScene:
    def __init__(self):
        self.ar = []
        x = 0
        y = 0
        for fl in (cfg.data_dir / "img/action").glob("*.*"):
            self.ar.append(ResizableImage(str(fl), x, y, 200, 200))
            if x >= (cfg.screen_width - 200):
                x = 0
                y += 200
            else:
                x += 200

    def show(self):
        screen.fill((0, 0, 0))
        for elm in self.ar:
            elm.show()
        pygame.display.flip()

    def check_click(self, event):
        for elm in self.ar:
            if elm.check_if_point_contains(event.pos):
                gvar["carousal_mode_obj"].update_fl(elm.fl)
                gvar["current_scene"] = "base"


class SceneSelectCharacter:
    def __init__(self):
        self.load_avatars()

    def load_avatars(self):
        y = 25
        gvar["avatar"] = {}
        gvar["pobj"] = {}
        for prsn in gvar["people"]:
            gvar["pobj"][prsn] = Character(50, y, prsn)
            y += 225

    def show(self):
        screen.fill((0, 0, 0))
        for v in gvar["pobj"].values():
            v.show()
        pygame.display.flip()

    def check_click(self, event):
        for k, v in gvar["pobj"].items():
            if v.check_if_point_contains(event.pos):
                gvar["char_mode_obj"].update_fl(v.fl)
                gvar["current_scene"] = "base"


def start():
    running = True
    updated = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                gvar["scenes"][gvar["current_scene"]].check_click(event)
                updated = True
        if updated:
            gvar["scenes"][gvar["current_scene"]].show()
            updated = False
    pygame.quit()


if __name__ == '__main__':
    load_static_values()
    gvar["scenes"] = {
        "sel_char": SceneSelectCharacter(),
        "base": BaseScene(),
        "sel_action": SelActionScene()
    }
    gvar["current_scene"] = "base"
    gvar["scenes"][gvar["current_scene"]].show()
    start()
