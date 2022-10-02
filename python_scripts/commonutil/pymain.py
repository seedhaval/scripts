import sys

sys.path.append(r"D:\scripts\scripts")

from python_scripts.commonutil.helper import get_choice_from_user
from python_scripts.youtube_video_utilities import create_new_project, \
    create_walkthrough_ppt, generate_video, generate_benime_file, \
    create_audacity_files, add_noaudio_file_name

ch_ar = ["Create new Youtube project",
         "Create walkthrough PPT",
         "Generate Benime file",
         "Generate video",
         "Create audacity file",
         "Add _noaudio to file name"]

while True:
    ch = get_choice_from_user("Select action", ch_ar)
    if ch == "Create new Youtube project":
        create_new_project.main()
    elif ch == "Create walkthrough PPT":
        create_walkthrough_ppt.main()
    elif ch == "Generate video":
        generate_video.main()
    elif ch == "Generate Benime file":
        generate_benime_file.main()
    elif ch == "Create audacity file":
        create_audacity_files.main()
    elif ch == "Add _noaudio to file name":
        add_noaudio_file_name.main()
