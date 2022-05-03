from bryhelper import *
from collections import defaultdict

obj = {}

def newline():
    return obj['dmain'].add_br(2)

def ui_data_loaded( rsp ):
    obj['prsn_list'] = [x[0] for x in rsp['person']]
    obj['act_ref'] = {}
    for e in rsp['action']:
        obj['act_ref'][e[0]] = e

    d = defaultdict(int)
    for e in rsp['action']:
        for i in range(e[2],e[3]+1):
            d[i]+=1
    txt = '<br><b>Counts</b><br>'
    txt += '<br>'.join( [f'{k} -> {d[k]}' for k in sorted(d.keys())] )
    txt += f'<br><b>Total :</b>{len(rsp["action"])}<br>'

    obj['count'].set_text( txt )
    obj['table'].set_data( sorted( rsp['action'], key=lambda x: x[2]) )
    obj['edit_prsn'].update_names()
    obj['edit_act'].update_names()

class EditPerson():
    def __init__(self):
        o = obj['dmain']
        o.add_span( 'Person' )
        newline()
        self.dd_act = o.add_dropdown( ['Add','Delete'], self.chg_action, 'Action' )
        newline()
        self.txt_nm = o.add_text( 15, 'Name', dummy )
        self.dd_nm = o.add_dropdown( [], dummy, 'Name' )
        newline()
        o.add_button( '&#x2705;', self.perform_action )
        self.chg_action()

    def chg_action( self, *args, **kwargs ):
        if self.dd_act.get() == 'Add':
            self.txt_nm.clear()
            self.txt_nm.show()
            self.dd_nm.hide()
        else:
            self.txt_nm.hide()
            self.dd_nm.show()

    def perform_action( self, *args, **kwargs ):
        if self.dd_act.get() == 'Add':
            post_json( '../add_prsn', {'person': self.txt_nm.get()}, refresh_data )
            self.txt_nm.clear()
        else:
            post_json( '../del_prsn', {'person': self.dd_nm.get()}, refresh_data )

    def update_names(self):
        self.dd_nm.change( sorted( obj['prsn_list'] ) )

class EditAction():
    def __init__( self ):
        o = obj['dmain']
        o.add_span( 'Actions' )
        newline()
        self.dd_act = o.add_dropdown( ['Add','Edit','Delete'], self.chg_action, 'Action' )
        newline()
        self.dd_nm = o.add_dropdown( [], self.nm_chg, 'Name' )
        self.nl0 = newline()
        self.txt_nm = o.add_text( 20, 'Name', dummy )
        self.nl1 = newline()
        self.threshold = o.add_text( 20, 'Threshold', dummy)
        self.nl2 = newline()
        self.strt_hr = o.add_text( 20, 'Start Hour', dummy)
        self.nl3 = newline()
        self.end_hr = o.add_text( 20, 'End Hour', dummy)
        self.nl4 = newline()
        self.btn_txt = o.add_text( 20, 'Button Text', dummy)
        newline()
        o.add_button( '&#x2705;', self.perform_action )
        o.add_button( '&#x274c;', self.clear )
        o.add_button( '&#x1f50d;', self.filter )

        self.chg_action()

    def chg_action( self, *args, **kwargs ):
        self.hide_all()
        if self.dd_act.get() == 'Add':
            self.txt_nm.show()
            self.nl1.show()
            self.threshold.show()
            self.nl2.show()
            self.strt_hr.show()
            self.nl3.show()
            self.end_hr.show()
            self.nl4.show()
            self.btn_txt.show()
        elif self.dd_act.get() == 'Edit':
            self.dd_nm.show()
            self.nl0.show()
            self.txt_nm.show()
            self.nl1.show()
            self.threshold.show()
            self.nl2.show()
            self.strt_hr.show()
            self.nl3.show()
            self.end_hr.show()
            self.nl4.show()
            self.btn_txt.show()
            self.nm_chg()
        else:
            self.dd_nm.show()

    def perform_action( self, *args, **kwargs ):
        if self.dd_act.get() == 'Add':
            if self.txt_nm.get() in obj['act_ref']:
                alert('Already present')
            else:
                post_json( '../add_actn', self.get_dict(), refresh_data )
        elif self.dd_act.get() == 'Edit':
            post_json( '../upd_actn', self.get_dict(), refresh_data )
        else:
            post_json( '../del_actn', self.get_dict(), refresh_data )

    def nm_chg( self, *args, **kwargs ):
        e = obj['act_ref'][self.dd_nm.get()]
        self.txt_nm.set( e[0] )
        self.threshold.set( e[1] )
        self.strt_hr.set( e[2] )
        self.end_hr.set( e[3] )
        self.btn_txt.set( e[4] )

    def hide_all( self ):
        self.txt_nm.hide()
        self.dd_nm.hide()
        self.nl0.hide()
        self.nl1.hide()
        self.threshold.hide()
        self.nl2.hide()
        self.strt_hr.hide()
        self.nl3.hide()
        self.end_hr.hide()
        self.nl4.hide()
        self.btn_txt.hide()

    def clear( self, *args, **kwargs ):
        self.txt_nm.clear()
        self.threshold.clear()
        self.strt_hr.clear()
        self.end_hr.clear()
        self.btn_txt.clear()
        
    def get_dict(self):
        d = {}
        d['action_nm'] = self.dd_nm.get()
        d['threshold'] = self.threshold.get()
        d['new_nm'] = self.txt_nm.get()
        d['strt_hr'] = self.strt_hr.get()
        d['end_hr'] = self.end_hr.get()
        d['btn_txt'] = self.btn_txt.get()
        return d

    def update_names(self):
        self.dd_nm.change( sorted( obj['act_ref'].keys() ) )
        self.nm_chg()

    def filter(self, *args, **kwargs):
        s = obj['table'].get_filter()
        self.dd_nm.change( [x for x in sorted( obj['act_ref'].keys() ) if s in x] )
        self.nm_chg()

def refresh_data( *args, **kwargs ):
    get_json( '../get_ui_data', ui_data_loaded )

def main():
    obj['dmain'] = doc.add_div('d1')
    newline()
    obj['dmain'].add_br()
    obj['dmain'].elm <= P( '&#x915;&#x94d;&#x930;&#x93f;&#x92f;&#x93e;&#x20;&#x938;&#x942;&#x91a;&#x940;&#x20;&#x92a;&#x94d;&#x930;&#x936;&#x93e;&#x938;&#x928;' )
    obj['edit_prsn'] = EditPerson()
    newline()
    obj['edit_act'] = EditAction()

    newline()
    obj['count'] = obj['dmain'].add_span( 'count' )
    obj['table'] = MyTable( obj['dmain'] )

    refresh_data()
