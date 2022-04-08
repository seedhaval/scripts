#!/usr/bin/env python3

import os
import shutil

home_dir = '/home/dvs'
scr_dir = '/home/dvs/scripts'
ckpt_fl = f'{home_dir}/.install_ckpt'

if not os.path.exists( ckpt_fl ):
    ckpt = 0
else:
    with open(ckpt_fl,'r') as f:
        ckpt = int(f.read())

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
    os.makedirs( f'{home_dir}/.vim/ undo' )
    return 1

def step_2():
    print( 'setting termux keyboard' )
    shutil.copy( f'{scr_dir}/termux/termux.properties', '/host-rootfs/data/data/tech.ula/files/home/.termux/' )
    return 2

def step_3():
    print( 'installing ffmpeg, imagemagick, vim' )
    os.system( 'sudo apt-get install ffmpeg imagemagick vim' )
    return 3

def step_4():
    print( 'installing python libraries' )
    os.system( 'sudo pip install pillow blessed flask flask_login moviepy progressbar sqlalchemy pyyaml aggdraw getch imagehash numpy' )
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

