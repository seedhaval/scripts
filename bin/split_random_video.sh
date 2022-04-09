#!/bin/bash
set -e -u -o pipefail

cd ~/data/
rm -f tmp/*
mv "$( ls -1 priv_vid/*.mp4 | shuf -n 1 )" tmp/a.mp4
cd tmp
ffmpeg -i a.mp4 -c copy -map 0 -segment_time 00:00:01 -f segment -reset_timestamps 1 out_%07d.mp4
rm a.mp4
