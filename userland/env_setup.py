#!/usr/bin/env python3

import os
import shutil

home_dir = '/home/dvs'
scr_dir = '/home/dvs/scripts'
pub_dir = '/storage/internal'

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

def step_5():
    print( 'Creating brython js' )
    os.system( 'sudo pip install brython' )
    os.makedirs( f'{home_dir}/tmp/brython' )
    os.chdir( f'{home_dir}/tmp/brython' ) 
    os.system( 'brython-cli --install' )
    os.chdir( home_dir )
    return 5

def step_6():
    print( 'creating public directories and symlinks' )
    os.makedirs( f'{pub_dir}/bin', exist_ok=True )
    os.makedirs( f'{pub_dir}/data', exist_ok=True )
    os.makedirs( f'{pub_dir}/config', exist_ok=True )
    os.symlink( f'{pub_dir}/bin', f'{home_dir}/bin', True )
    os.symlink( f'{pub_dir}/data', f'{home_dir}/data', True )
    os.symlink( f'{pub_dir}/config', f'{home_dir}/config', True )
    return 6

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

if ckpt < 5:
    ckpt = step_5()
    set_ckpt()

if ckpt < 6:
    ckpt = step_6()
    set_ckpt()

