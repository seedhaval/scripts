import sys
sys.path.append(r"D:\scripts\scripts")

from python_scripts.commonutil.helper import get_choice_from_user
from python_scripts.youtube_video_utilities import create_new_project

ch = get_choice_from_user("Select action",["Create new Youtube project"])

if ch == "Create new Youtube project":
    create_new_project.main()