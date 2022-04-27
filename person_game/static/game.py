from bryhelper import *
from datetime import datetime, timedelta
import random

obj = {}

def newline():
    return obj['dmain'].add_br(2)

def curdate():
    return datetime.now().strftime('%d/%m/%Y')

def maxdone():
    return False
    dt = curdate()
    if list(obj['pref'].values()).count(dt) >= 20:
        return True
    return False

def validwindow( s ):
    strt, nd = [int(x) for x in s[4].split(',')]
    cur = int(datetime.now().strftime('%H'))
    if strt <= cur <= nd:
        return True
    return False

def get_days_since( dt ):
   return ( datetime.now() - datetime.strptime( dt, '%d/%m/%Y' ) ).days
 
def action( actobj, *args, **kwargs ):
    if actobj.typ != 'random':
        dt = curdate()
    else:
        dt = actobj.get_next()
    d = { 'prsn': obj['prsn'].get(), 'newval': dt, 'act': actobj.nm }
    post_json( '../update_act_data', d, prsn_chg )
        
class RandAction():
    def __init__( self, e ):
        self.ar = e
        self.nm = e[0]
        self.btntxt = e[5]
        self.typ = 'random'

        self.txt = obj['dmain'].add_span( e[0] )
        self.button = obj['dmain'].add_button( self.btntxt, lambda *args: action( self ) )
        self.mn, self.mx = [int(x) for x in e[2].split(',')]
        self.nl = newline()

    def get_next(self):
        return (datetime.now() + timedelta(days=random.randint(self.mn,self.mx))).strftime('%d/%m/%Y')

    def hide(self):
        self.button.hide()
        self.txt.hide()
        self.nl.hide()

    def show(self):
        self.button.show()
        self.txt.show()
        self.nl.show()

    def prsn_chg( self ):
        m = maxdone()
        dt = obj['pref'][self.nm]
        if m or get_days_since(dt) < 0:
            self.hide()
            return
        if random.randint(0,2) == 0:
            self.show()
        else:
            self.hide()

class OncePerDay():
    def __init__( self, e ):
        self.ar = e
        self.nm = e[0]
        self.btntxt = e[5]
        self.typ = 'once_per_day'

        self.txt = obj['dmain'].add_span( e[0] )
        self.button = obj['dmain'].add_button( self.btntxt, lambda *args: action( self ) )
        self.nl = newline()

    def hide(self):
        self.button.hide()
        self.txt.hide()
        self.nl.hide()

    def show(self):
        self.button.show()
        self.txt.show()
        self.nl.show()

    def prsn_chg( self ):
        m = maxdone()
        dt = obj['pref'][self.nm]
        if m or not validwindow(self.ar):
            self.hide()
            return
        if dt != curdate():
            self.show()
        else:
            self.hide()

class GrowAndCut():
    def __init__( self, e ):
        self.ar = e
        self.nm = e[0]
        self.btntxt = e[5]
        self.per_day = float(e[2])
        self.thresh = float(e[3])
        self.typ = 'grow_and_cut'

        self.txtbox = obj['dmain'].add_text( 5, self.nm, None )
        self.button = obj['dmain'].add_button( self.btntxt, lambda *args: action( self ) )
        self.nl = newline()

    def hide(self):
        self.button.hide()
        self.txtbox.hide()
        self.nl.hide()

    def show(self):
        self.button.show()
        self.txtbox.show()
        self.nl.show()

    def prsn_chg( self ):
        m = maxdone()
        dt = obj['pref'][self.nm]
        val = self.per_day*get_days_since(dt)
        self.txtbox.set(f'{val:.2f}')
        if m or not validwindow(self.ar):
            self.hide()
            return
        if float(val) >= self.thresh:
            self.show()
        else:
            self.hide()

def ui_data_loaded( rsp ):
    obj['ui'] = rsp['out']
    obj['act_ar'] = []
    for e in rsp['out']:
        if e[1] == 'grow_and_cut':
            obj['act_ar'].append( GrowAndCut(e) )
        elif e[1] == 'once_per_day':
            obj['act_ar'].append( OncePerDay(e) )
        elif e[1] == 'random':
            obj['act_ar'].append( RandAction(e) )
    obj['prsn'].change( sorted( rsp['prsn_list'] ) )
    prsn_chg()

def prsn_data_loaded( rsp ):
    obj['pdata'] = rsp['out']
    obj['pref'] = {}
    for e in obj['pdata']:
        obj['pref'][e[0]] = e[1]
    for e in obj['act_ar']:
        e.prsn_chg()

def prsn_chg( *args, **kwargs ):
    get_json( '../get_person_data/' + obj['prsn'].get(), prsn_data_loaded )
    
def main():
    obj['dmain'] = doc.add_div('d1')
    newline()
    obj['dmain'].elm <= P( '&#x972;&#x915;&#x94d;&#x936;&#x928;&#x20;&#x917;&#x947;&#x92e;' )

    obj['prsn'] = obj['dmain'].add_dropdown( [], prsn_chg, 'Person' )
    newline()
    
    get_json( '../get_ui_data', ui_data_loaded )

