from pathlib import Path
import os

base_dir = Path(os.path.realpath(__file__)).parent.parent

if os.name == 'nt':
    data_dir = Path("D:/data/Game_Action/data")
    screen_height = 1000
    screen_width = 1000
else:
    data_dir = Path("/sdcard/Game_Action/.data")
    screen_height = 2000
    screen_width = 1000

fps = 20
