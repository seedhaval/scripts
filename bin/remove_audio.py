#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path
import json

fldr = Path( "/storage/internal/data/priv_vid/" )

def has_audio_stream( fl ):
    print( fl )
    ret = not 'noaudio' in str(fl)
    print( ret )
    return ret

def remove_audio_stream( fl ):
    ofl = str(fl).replace( '.mp4', '_noaudio.mp4' )
    subprocess.check_output( ['ffmpeg','-i',fl,'-c','copy','-an',ofl] )
    os.remove( fl )

for fl in fldr.glob('*.mp4'):
    if has_audio_stream( fl ):
        remove_audio_stream( fl )
