import sys
sys.path.append(r"D:\scripts\scripts")

from python_scripts.commonutil.helper import get_choice_from_user
from python_scripts.youtube_video_utilities import create_new_project, create_walkthrough_ppt

ch = get_choice_from_user("Select action",["Create new Youtube project",
                                           "Create walkthrough PPT"])

if ch == "Create new Youtube project":
    create_new_project.main()
elif ch == "Create walkthrough PPT":
    create_walkthrough_ppt.main()