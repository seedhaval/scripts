#!/usr/bin/env python3

import os
import shutil
import subprocess

home_dir = '/home/userland'
scr_dir = '/home/userland/scripts/shell_scripts'
pub_dir = '/storage/internal'

ckpt_fl = f'{home_dir}/.install_ckpt'

if not os.path.exists( ckpt_fl ):
    ckpt = 0
else:
    with open(ckpt_fl,'r') as f:
        ckpt = int(f.read())

def exec_cmd( txt ):
    p = subprocess.Popen(txt, shell=True)
    p.wait()
    if p.returncode > 0:
        exit()

def set_ckpt():
    with open( ckpt_fl, 'w' ) as f:
        f.write(str(int(ckpt)))

def step_1():
    print( 'copying bashrc, vimrc, inputrc' )
    shutil.copy( f'{scr_dir}/rc_scripts/.bashrc_custom', f'{home_dir}/' )
    shutil.copy( f'{scr_dir}/rc_scripts/.vimrc', f'{home_dir}/' )
    shutil.copy( f'{scr_dir}/rc_scripts/.inputrc', f'{home_dir}/' )
    with open( f'{home_dir}/.bashrc', 'a' ) as f:
        f.write( '\n. ~/.bashrc_custom\n' )
    os.makedirs( f'{home_dir}/.vim/undo' )
    return 1

def step_2():
    print( 'setting termux keyboard' )
    os.makedirs( f'/host-rootfs/data/data/tech.ula/files/home/.termux' )
    shutil.copy( f'{scr_dir}/termux/termux.properties', '/host-rootfs/data/data/tech.ula/files/home/.termux/termux.properties' )
    return 2

def step_3():
    print( 'installing ffmpeg, imagemagick, vim, pip' )
    exec_cmd( 'sudo apt-get install ffmpeg imagemagick vim python3-pip' )
    return 3

def step_4():
    print( 'installing python libraries' )
    exec_cmd( 'sudo pip3 install pillow blessed flask flask_login moviepy progressbar sqlalchemy pyyaml aggdraw getch imagehash numpy' )
    return 4

if ckpt < 1:
    ckpt = step_1()
    set_ckpt()

if ckpt < 2:
    ckpt = step_2()
    set_ckpt()

if ckpt < 3:
    ckpt = step_3()
    set_ckpt()

if ckpt < 4:
    ckpt = step_4()
    set_ckpt()

