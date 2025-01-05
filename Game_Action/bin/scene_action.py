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
        self.swap = ResizableImage("swap", xtop, ytop + 400, 200, 200, gvar)
        self.home = ResizableImage("home", xtop + 200, ytop + 400, 200, 200,
                                   gvar)
        self.doact = OnOffSwitch(gvar, xtop + 400, ytop + 400, 200, 200,
                                 "play",
                                 "reject")
        self.doact.off()
        self.cur_prsn = 0
        self.get_person_list()

    def get_action_list(self):
        self.gender_combo = self.gvar["map"]["person"][self.p1.nm]["gender"] + \
                            self.gvar["map"]["person"][self.p2.nm]["gender"]
        ar = []
        cur_loc = self.gvar["map"]["location"][self.gvar["location.path"][-1]]
        for elm in cur_loc["actions"]:
            d_act = self.gvar["map"]["action"][elm]
            if self.gender_combo in d_act["allowed_genders"]:
                ar.append({
                    "idx": elm,
                    "img": d_act["img"],
                    "name": d_act["name"]
                })
        self.action_ar = ar

    def get_person_list(self):
        ar = []
        for prsn in self.gvar["map"]["person"]:
            ar.append({
                "idx": prsn,
                "name": prsn,
                "img": prsn
            })
        self.person_ar = ar

    def handle_user_selected_person(self, sel):
        if self.cur_prsn == 0:
            self.p1.set_img(sel["idx"], sel["img"], sel["name"])
        else:
            self.p2.set_img(sel["idx"], sel["img"], sel["name"])
        self.gvar["current_scene"] = "action"
        self.show()

    def show_doact(self):
        self.get_action_list()
        if len(self.action_ar) > 0:
            self.doact.on()
        else:
            self.doact.off()
        self.doact.show()

    def show(self):
        self.screen.fill((0, 0, 0))
        self.p1.show()
        self.p2.show()
        self.swap.show()
        self.home.show()
        self.show_doact()
        pygame.display.flip()

    def handle_user_selected_action(self, sel):
        idx = sel["idx"]
        ar = []
        for elm in self.gvar["map"]["action"].get(sel["idx"], [])["children"]:
            d_act = self.gvar["map"]["action"][elm]
            ar.append({
                "idx": elm,
                "img": d_act["img"],
                "name": d_act["name"]
            })
        if len(ar) == 0:
            self.gvar["current_scene"] = "action"
            return
        get_user_selection(ar, self.gvar,
                           self.handle_user_selected_action)

    def check_click(self, event):
        pos = event.pos
        if self.home.check_if_point_contains(pos):
            self.gvar["current_scene"] = "location"
            self.gvar["location.path"] = ["root"]
        elif self.p1.is_clicked(pos):
            self.cur_prsn = 0
            get_user_selection(self.person_ar, self.gvar,
                               self.handle_user_selected_person)
        elif self.p2.is_clicked(pos):
            self.cur_prsn = 1
            get_user_selection(self.person_ar, self.gvar,
                               self.handle_user_selected_person)
        elif self.swap.check_if_point_contains(pos):
            cur_p1 = self.p1.nm
            cur_p2 = self.p2.nm
            self.p2.set_img(cur_p1, cur_p1, cur_p1)
            self.p1.set_img(cur_p2, cur_p2, cur_p2)
        elif self.doact.check_if_point_contains(pos):
            get_user_selection(self.action_ar, self.gvar,
                               self.handle_user_selected_action)
