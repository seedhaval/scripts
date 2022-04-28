from bryhelper import *
from datetime import datetime, timedelta
import random

obj = {}

def newline():
    return obj['dmain'].add_br(2)

def action( actobj, *args, **kwargs ):
    d = { 'prsn': actobj.prsn, 'act': actobj.nm }
    post_json( '../update_act_data', d, dummy )
    actobj.hide()
        
class PrsnAction():
    def __init__( self, e, prsn ):
        self.ar = e
        self.prsn = prsn
        self.nm = e[0]
        self.btntxt = e[1]
        self.txt = obj['dbody'].add_span( self.ar[0] )
        self.button = obj['dbody'].add_button( self.btntxt, lambda *args: action( self ) )
        self.nl = obj['dbody'].add_br(2)

    def hide(self):
        self.button.hide()
        self.txt.hide()
        self.nl.hide()

def refresh_data( rsp ):
    obj['dbody'].clear()
    obj['ar'] = []
    for prsn,act in rsp.items():
        obj['dbody'].add_span( '<b>' + prsn + '</b>' )
        obj['dbody'].add_br(2)
        for e in act:
            obj['ar'].append( PrsnAction(e,prsn) )

def main():
    obj['dmain'] = doc.add_div('d1')
    newline()
    obj['dmain'].elm <= P( '&#x972;&#x915;&#x94d;&#x936;&#x928;&#x20;&#x917;&#x947;&#x92e;' )
    obj['dmain'].add_button( '&#x1f501;', lambda *args: get_json( '../get_all_person_data', refresh_data ) )
    newline()
    newline()
    obj['dbody'] = obj['dmain'].add_div('d2')

    get_json( '../get_all_person_data', refresh_data )

