from helper import (GameActionObject, PersistentSelectableImage,
                    ResizableImage, OnOffSwitch)
from scene_select_option import get_user_selection
import pygame
import cfg


class ActionScene(GameActionObject):
    def __init__(self, gvar):
        super().__init__(gvar)
        xtop = int((cfg.screen_width - 600) / 2)
        ytop = int((cfg.screen_height - 600) / 2)
        self.p1 = PersistentSelectableImage(gvar, "plus", "plus", "plus", xtop,
                                            ytop)
        self.p2 = PersistentSelectableImage(gvar, "plus", "plus", "plus",
                                            xtop + 300, ytop)
        self.swap = ResizableImage("oriana", xtop, ytop + 400, 200, 200, gvar)
        self.home = ResizableImage("home", xtop + 200, ytop + 400, 200, 200,
                                   gvar)
        self.doact = OnOffSwitch(gvar, xtop + 400, ytop + 400, 200, 200,
                                 "oriana",
                                 "costa")
        self.doact.off()

    def get_location_list(self):
        loc = self.gvar["map"]["location"][self.gvar["location.path"][-1]][
            "children"]
        ar = []
        for elm in loc:
            ar.append({
                "idx": elm,
                "name": self.gvar["map"]["location"][elm]["name"],
                "img": self.gvar["map"]["location"][elm]["img"]
            })
        return ar

    def handle_user_selected_loc(self, sel):
        self.gvar["location.path"].append(sel["idx"])
        self.gvar["current_scene"] = "location"
        self.show()

    def show(self):
        # get_user_selection(self.get_location_list(), self.gvar,
        #                   self.handle_user_selected_loc)
        self.screen.fill((0, 0, 0))
        self.p1.show()
        self.p2.show()
        self.swap.show()
        self.home.show()
        self.doact.show()
        pygame.display.flip()
