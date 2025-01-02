#!/usr/bin/env python
import os
import random
import subprocess
import cfg
import time
import shutil

input_file = str(list((cfg.data_dir / "vid").glob("*.mp4"))[0])

output_dir = str(cfg.data_dir / "tmp")
shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)


def get_video_duration(video_file):
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        video_file
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)
    return float(result.stdout.strip())


def extract_frames(video_file, start_time, output_path, sample_index):
    cmd = [
        "ffmpeg",
        "-ss", str(start_time),
        "-i", video_file,
        "-q:v", "1",
        "-vf", "fps=10",
        "-frames:v", "2",
        "-start_number", "0",
        os.path.join(output_path, f"%02d.png"),
        "-hide_banner",
        "-loglevel", "error"
    ]
    subprocess.run(cmd)


def main():
    duration = get_video_duration(input_file)
    if duration <= 0:
        print("Invalid video duration. Check the input file.")
        return

    for i in range(1, 101):
        start_time = random.uniform(0, max(0, duration - 2))
        sample_dir = os.path.join(output_dir, f"{(int(time.time()))}_{i}")
        os.makedirs(sample_dir, exist_ok=True)
        print(f"Extracting sample {i} starting at {start_time:.2f} seconds...")
        extract_frames(input_file, start_time, sample_dir, i)

    print("Frame extraction complete.")


if __name__ == "__main__":
    main()
