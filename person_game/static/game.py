from bryhelper import *
from datetime import datetime

obj = {}

def newline():
    obj['dmain'].add_br()
    obj['dmain'].add_br()

def curdate():
    return datetime.now().strftime('%d/%m/%Y')

def validwindow( s ):
    strt, nd = [int(x) for x in s[3].split(',')]
    cur = int(datetime.now().strftime('%H'))
    if strt <= cur <= nd:
        return True
    return False

def get_days_since( dt ):
   return ( datetime.now() - datetime.strptime( dt, '%d/%m/%Y' ) ).days
 
def action( actobj, *args, **kwargs ):
    d = { 'prsn': obj['prsn'].get(), 'newval': curdate(), 'act': actobj.typ }
    post_json( '../update_act_data', d, prsn_chg )
        
class OncePerDay():
    def __init__( self, e ):
        self.ar = e
        self.typ = e[0]
        self.btntxt = e[4]

        obj['dmain'].elm <= SPAN( e[0] )
        self.button = obj['dmain'].add_button( self.btntxt, lambda *args: action( self ) )
        newline()

    def prsn_chg( self ):
        dt = obj['pref'][self.typ]
        if not validwindow(self.ar):
            self.button.hide()
            return
        if dt != curdate():
            self.button.show()
        else:
            self.button.hide()

    @staticmethod
    def isvalid( ref ):
        if ref[2] == 'once_per_day':
            return True
        return False

class GrowAndCut():
    def __init__( self, e ):
        self.ar = e
        self.typ = e[0]
        self.btntxt = e[4]
        self.per_day = float(e[1].split('=')[1])
        self.thresh = float(e[2].split('=')[1].split('m')[0])

        self.txtbox = obj['dmain'].add_text( 5, self.typ, None )
        self.button = obj['dmain'].add_button( self.btntxt, lambda *args: action( self ) )
        newline()

    def prsn_chg( self ):
        dt = obj['pref'][self.typ]
        val = self.per_day*get_days_since(dt)
        self.txtbox.set(f'{val:.2f}')
        if not validwindow(self.ar):
            self.button.hide()
            return
        if float(val) >= self.thresh:
            self.button.show()
        else:
            self.button.hide()

    @staticmethod
    def isvalid( ref ):
        if ref[5] == 'date' and ref[6] == 'length':
            return True
        return False

def ui_data_loaded( rsp ):
    obj['ui'] = rsp['out']
    obj['act_ar'] = []
    for e in rsp['out']:
        if GrowAndCut.isvalid( e ):
            obj['act_ar'].append( GrowAndCut(e) )
        elif OncePerDay.isvalid(e):
            obj['act_ar'].append( OncePerDay(e) )
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
    obj['dmain'].add_br()
    obj['dmain'].elm <= P( 'Action Game' )

    prsn = ['dpm', 'ga', 'pdjm', '0pg', 'wgad.', '0a_dd', 'gma_pwg', '0a_pmgj', 'ga_.a', 'dg_m.']
    obj['prsn'] = obj['dmain'].add_dropdown( prsn, prsn_chg, 'Person' )
    newline()
    

    get_json( '../get_ui_data', ui_data_loaded )

