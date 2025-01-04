from helper import GameActionObject
from scene_select_option import get_user_selection


class LocationScene(GameActionObject):
    def __init__(self, gvar):
        super().__init__(gvar)
        self.gvar["location.path"] = ["root"]

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
        if len(self.gvar["map"]["location"][sel["idx"]]["children"]) == 0:
            self.gvar["current_scene"] = "action"
            self.gvar["scenes"]["action"].show()
        else:
            self.show()

    def show(self):
        get_user_selection(self.get_location_list(), self.gvar,
                           self.handle_user_selected_loc)
