#!/usr/bin/env python3
import helper
from pathlib import Path

raw_fl_dir = Path( '/home/dvs/scripts/python_raw_info/done/' )
out_fldr = Path( '/home/dvs/tmp/' )

i_cntr = 65

map_tree = {}

def save_ar( ar ):
    global i_cntr
    helper.write_fl( f'{out_fldr}/python_standard_library_{i_cntr}.txt' , '\n'.join( ar ) )
    i_cntr += 1

def generate_map_txt():
    cur_ar = ['python standard library']
    for k in map_tree.keys():
            cur_ar.append( '    ' + k )
            split_flag = False
            for kf in map_tree[k].keys():
                if split_flag:
                    cur_ar.append( '    ' + k )
                    split_flag = False
                cur_ar.append( '        ' + kf )
                for ln in map_tree[k][kf]:
                    cur_ar.append( '            ' + ln )
                if len( cur_ar ) >= 19:
                    save_ar( cur_ar )
                    cur_ar = ['python standard library']
                    split_flag = True

def get_tree( txt ):
    d = {}
    title_flag = True
    for ln in txt.strip().splitlines():
        if ln[0] == '=':
            title_flag = True
        elif title_flag == True:
            title_flag = False
            key = ln.strip()
            d[ key ] = []
        else:
            d[ key ].append( ln.strip() )
    return d

def process_fl( fl ):
    print( 'Processing ' + fl.name )
    map_tree[ fl.stem ] = get_tree( helper.read_fl( fl ) )

for fl in raw_fl_dir.glob( '*.txt' ):
   process_fl( fl )

generate_map_txt()
