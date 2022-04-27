from bryhelper import *

obj = {}

def newline():
    return obj['dmain'].add_br(2)

def ui_data_loaded( rsp ):
    obj['prsn_list'] = rsp['prsn_list']
    obj['act_ref'] = {}
    for e in rsp['out']:
        obj['act_ref'][e[0]] = e

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
        self.dd_typ = o.add_dropdown( ['once_per_day','grow_and_cut','random'], dummy, 'Type' )
        self.nl2 = newline()
        self.inc_rate = o.add_text( 20, 'Inc Rate', dummy)
        self.nl3 = newline()
        self.threshold = o.add_text( 20, 'Threshold', dummy)
        self.nl4 = newline()
        self.window = o.add_text( 20, 'Window', dummy)
        self.nl5 = newline()
        self.symbol = o.add_text( 20, 'Symbol', dummy)
        newline()
        o.add_button( '&#x2705;', self.perform_action )
        o.add_button( '&#x274c;', self.clear )

        self.chg_action()

    def chg_action( self, *args, **kwargs ):
        self.hide_all()
        if self.dd_act.get() == 'Add':
            self.txt_nm.show()
            self.nl1.show()
            self.dd_typ.show()
            self.nl2.show()
            self.inc_rate.show()
            self.nl3.show()
            self.threshold.show()
            self.nl4.show()
            self.window.show()
            self.nl5.show()
            self.symbol.show()
        elif self.dd_act.get() == 'Edit':
            self.dd_nm.show()
            self.nl0.show()
            self.txt_nm.show()
            self.nl1.show()
            self.dd_typ.show()
            self.nl2.show()
            self.inc_rate.show()
            self.nl3.show()
            self.threshold.show()
            self.nl4.show()
            self.window.show()
            self.nl5.show()
            self.symbol.show()
            self.nm_chg()
        else:
            self.dd_nm.show()

    def perform_action( self, *args, **kwargs ):
        if self.dd_act.get() == 'Add':
            post_json( '../add_actn', self.get_dict(), refresh_data )
        elif self.dd_act.get() == 'Edit':
            post_json( '../upd_actn', self.get_dict(), refresh_data )
        else:
            post_json( '../del_actn', self.get_dict(), refresh_data )

    def nm_chg( self, *args, **kwargs ):
        e = obj['act_ref'][self.dd_nm.get()]
        self.txt_nm.set( e[0] )
        self.dd_typ.set( e[1] )
        self.inc_rate.set( e[2] )
        self.threshold.set( e[3] )
        self.window.set( e[4] )
        self.symbol.set( e[5] )

    def hide_all( self ):
        self.txt_nm.hide()
        self.dd_nm.hide()
        self.nl0.hide()
        self.nl1.hide()
        self.dd_typ.hide()
        self.nl2.hide()
        self.inc_rate.hide()
        self.nl3.hide()
        self.threshold.hide()
        self.nl4.hide()
        self.window.hide()
        self.nl5.hide()
        self.symbol.hide()

    def clear( self, *args, **kwargs ):
        self.txt_nm.clear()
        self.inc_rate.clear()
        self.threshold.clear()
        self.window.clear()
        self.symbol.clear()
        
    def get_dict(self):
        d = {}
        d['nm'] = self.dd_nm.get()
        d['values'] = [
            self.txt_nm.get()
            ,self.dd_typ.get()
            ,self.inc_rate.get()
            ,self.threshold.get()
            ,self.window.get()
            ,self.symbol.get()
        ] 
        return d

    def update_names(self):
        self.dd_nm.change( sorted( obj['act_ref'].keys() ) )
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

    refresh_data()
