#!/usr/bin/env python3

import subprocess

def get_mobile_ip():
    for i in range(10):
        address = f'192.168.1.{100+i}'
        res = subprocess.call( ['nc', '-w', '1', '-z', address, '2022'] )
        if res == 0:
            print( f'ping to {address} succedded' )
            return address
        else:
            print( f'ping to {address} failed' )

with open( '/home/dvs/.mobile.ip', 'w' ) as f:
    f.write( get_mobile_ip() )
