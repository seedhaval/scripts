from helper import GameActionObject
from scene_select_option import get_user_selection


class LocationScene(GameActionObject):
    def __init__(self, gvar):
        super().__init__(gvar)
        self.gvar["location.path"] = []

    def get_location_list(self):
        loc = self.gvar["map"]["location"]
        for elm in self.gvar["location.path"]:
            if elm["type"] == "specific":
                loc = loc["children"][elm["idx"]]
            else:
                loc = self.gvar["map"]["generic_location"][elm["idx"]]
        return [{"idx": k, "img": v["img"], "name": v["name"]} for k,
        v in loc.items()]

    def handle_user_selected_loc(self, sel):
        pass

    def show(self):
        get_user_selection(self.get_location_list(), self.gvar,
                           self.handle_user_selected_loc)
