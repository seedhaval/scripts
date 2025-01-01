from pathlib import Path
import os

base_dir = Path(os.path.realpath(__file__)).parent.parent

if os.name == 'nt':
    data_dir = Path("D:/data/Game/data")
    screen_height = 1000
    screen_width = 800
else:
    data_dir = Path("/sdcard/Game/.data")
    screen_height = 2000
    screen_width = 1000

RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 20
SPEED = 10  # pixels per second
