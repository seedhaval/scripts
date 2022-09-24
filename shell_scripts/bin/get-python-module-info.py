#!/usr/bin/env python3

import inspect

def show_info( elm, pnm, nm ):
    print( f'{"="*30}' )
    print( f'{pnm}.{nm}' )
    try:
        print( f'{inspect.signature( elm )}' )
    except:
        pass
    print( str(inspect.getdoc( elm )).replace('. ','\n') )
    print( '' )

def get_info( obj, pnm ):
    for nm, elm in inspect.getmembers( obj ):
        if not nm.startswith('_') and not nm == nm.upper():
            show_info( elm, pnm, nm )
            if inspect.isclass( elm ):
                get_info( elm, pnm + '.' + nm )

import os
get_info( os, 'os' )
