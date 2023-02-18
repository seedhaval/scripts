from pathlib import Path
import os


def get_desktop_path():
    userprofile = Path(os.environ['USERPROFILE'])
    onedrivepth = list(userprofile.glob("OneDrive*/Desktop"))
    if onedrivepth:
        return onedrivepth[0]
    else:
        return str(userprofile / "Desktop")
