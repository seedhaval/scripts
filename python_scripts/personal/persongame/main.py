import tkinter
from commonutil import helper, tkhelper
import random
import string
import time

config_file = "d:/data/config/action_config.json"


class App:
    def __init__(self):
        self.app: tkhelper.MyApp = tkhelper.MyApp("Action", 500, 200)
        self.action_frame: tkhelper.MyFrame = self.app.add_frame("Action", 480, 180, [1, 1, 1, 1])
        self.lbl_data: tkhelper.MyLabel = self.action_frame.add_label("lbl_data", "Hello", 40, 2, [1, 1, 1, 1])
        self.btn_next: tkhelper.MyButton = self.action_frame.add_button("btn_next", "Perform Action",
                                                                        self.refresh_action, [2, 1, 1, 1])
        self.data: dict = helper.File(config_file).load_json()
        self.refresh_action()

    def get_action(self) -> str:
        d: dict = {}
        for k, v in self.data['vars'].items():
            d[k] = random.choice(v)
        return string.Template(random.choice(self.data['action'])).safe_substitute(d)

    def refresh_action(self, *args, **kwargs) -> None:
        time.sleep(3)
        self.lbl_data.set(self.get_action())

    def show(self):
        self.app.show()


app = App()
app.show()
