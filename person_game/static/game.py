from bryhelper import *
import random

obj = {}

def newline():
    return obj['dmain'].add_br(2)

def action( actobj, *args, **kwargs ):
    d = { 'prsn': actobj.prsn, 'act': actobj.nm, 'btn_txt': actobj.btntxt}
    post_json( '../update_act_data', d, dummy )
    actobj.hide()
        
class PrsnAction():
    def __init__( self, e ):
        self.ar = e
        self.prsn = e[0]
        self.nm = e[1]
        self.btntxt = e[2]
        self.div = obj['dbody'].add_div('d2')
        self.div.add_br(1)
        self.div.add_span( '<b>' + self.prsn + '</b>' )
        self.div.add_br(2)
        self.div.add_span( self.ar[1] )
        self.div.add_br(2)
        self.div.add_button( self.btntxt, lambda *args: action( self ) )
        self.div.add_br(1)

    def hide(self):
        self.div.remove()

def refresh_data( rsp ):
    obj['dbody'].clear()
    for e in rsp['out']:
        obj['dbody'].add_br(1)
        PrsnAction(e)

def main():
    obj['dmain'] = doc.add_div('d1')
    obj['dmain'].add_br(1)
    obj['dmain'].elm <= P( '&#x972;&#x915;&#x94d;&#x936;&#x928;&#x20;&#x917;&#x947;&#x92e;' )
    obj['dmain'].add_button( '&#x1f501;', lambda *args: get_json( '../get_all_person_data', refresh_data ) )
    obj['dmain'].add_br(1)
    obj['dbody'] = obj['dmain'].add_div('d3')

    get_json( '../get_all_person_data', refresh_data )

