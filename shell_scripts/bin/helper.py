#!/usr/bin/env python

def read_fl( fl ):
    with open( fl ) as f:
        return f.read()

def write_fl( fl, txt ):
    with open( fl, 'w' ) as f:
        f.write( txt )
