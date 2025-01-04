import cfg
from helper import GameActionObject, OnOffSwitch, SelectableImage
from calc import reshape_to_3d
import pygame


class OptionSelectScene(GameActionObject):
    def __init__(self, lst, gvar, cb_func):
        super().__init__(gvar)
        self.lst = lst
        self.cb_func = cb_func
        self.rows_per_page = int(cfg.screen_height / 400)
        self.cols_per_row = int((cfg.screen_width - 200) / 400)
        self.xtop = (cfg.screen_width - (self.cols_per_row * 400)) / 2
        self.ytop = (cfg.screen_height - (self.rows_per_page * 400)) / 2
        self.ytop = 0
        self.pages = reshape_to_3d(lst, self.rows_per_page, self.cols_per_row)
        self.cur_page = 0
        self.img_ar = []
        self.load_switches()
        self.load_page()

    def load_switches(self):
        top = int((cfg.screen_height - 100) / 2)
        n_lft = cfg.screen_width - 100
        self.prev = OnOffSwitch(self.gvar, 0, top, 100, 100, "prevon",
                                "prevoff")
        self.nxt = OnOffSwitch(self.gvar, n_lft, top, 100, 100, "nexton",
                               "nextoff")

    def load_page(self):
        self.img_ar = []
        print(self.pages[self.cur_page])
        for ir, row in enumerate(self.pages[self.cur_page]):
            for ic, elm in enumerate(row):
                x = (self.xtop) + (400 * ic)
                y = self.ytop + (400 * ir)
                idx = elm["idx"]
                nm = elm["name"]
                img = elm["img"]
                obj = SelectableImage(self.gvar, idx, img, nm, x, y)
                self.img_ar.append(obj)

    def show_switches(self):
        self.prev.show()
        self.nxt.show()

    def show_images(self):
        for elm in self.img_ar:
            elm.show()

    def show(self):
        self.screen.fill((0, 0, 0))
        self.show_switches()
        self.show_images()
        pygame.display.flip()


def get_user_selection(lst, gvar, cb_func):
    scn = OptionSelectScene(lst, gvar, cb_func)
    gvar["scenes"]["select"] = scn
    gvar["current_scene"] = "select"
    scn = OptionSelectScene(lst, gvar, cb_func)
    scn.show()
