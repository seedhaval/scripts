from bryhelper import *

obj = {}

def newline():
    obj['dmain'].add_br()
    obj['dmain'].add_br()

def get_scn_typ():
    scn_nm = obj['scn'].get()
    scn = obj['data']['scenarios'][scn_nm]
    typ = obj['action_by'].get()
    return (scn, typ)

def get_obj_ar():
    scn, typ = get_scn_typ()
    return list(scn['actions'][typ].keys())

def get_act_ar():
    scn, typ = get_scn_typ()
    act1 = obj['act1'].get()
    return scn['actions'][typ][act1]

def change_action_by( *args, **kwargs ):
    obj['act1'].change( get_obj_ar() )
    load_act2()

def load_act2( *args, **kwargs ):
    obj['act2'].change( get_act_ar() )

def populate_scenarios( *args, **kwargs ):
    ar = list(obj['data']['scenarios'].keys())
    obj['scn'].change( ar )
    
def populate_actors( *args, **kwargs ):
    scn_nm = obj['scn'].get()
    scn = obj['data']['scenarios'][scn_nm]
    obj['action_by'].change( list(scn['actions'].keys()) )
    change_action_by()

def reload_scn():
    populate_scenarios()
    populate_actors()

def data_loaded( rsp ):
    obj['data'] = rsp['action']
    reload_scn()

def set_obj( val ):
    scn, typ = get_scn_typ()
    act1 = obj['act1'].get()
    scn['actions'][typ][val] = scn['actions'][typ][act1]
    del scn['actions'][typ][act1]
    change_action_by()

def edit_obj( *args, **kwargs ):
    inp( set_obj, obj['act1'].get() )

def new_obj( val ):
    scn, typ = get_scn_typ()
    scn['actions'][typ][ val ] = ["test"]
    change_action_by()

def add_obj( *args, **kwargs ):
    inp( new_obj, "New Object" )

def del_obj( *args, **kwargs ):
    scn, typ = get_scn_typ()
    act1 = obj['act1'].get()
    del scn['actions'][typ][act1]
    change_action_by()

def set_actee( val ):
    scn, typ = get_scn_typ()
    scn['actions'][val] = scn['actions'][typ]
    del scn['actions'][typ]
    populate_actors()

def edit_actee( *args, **kwargs ):
    inp( set_actee, obj['action_by'].get() )

def new_actee( val ):
    scn, typ = get_scn_typ()
    scn['actions'][ val ] = {"test": ["test"]}
    populate_actors()

def add_actee( *args, **kwargs ):
    inp( new_actee, "New Actee" )

def del_actee( *args, **kwargs ):
    scn, typ = get_scn_typ()
    del scn['actions'][typ]
    populate_actors()

def set_act( val ):
    scn, typ = get_scn_typ()
    act1 = obj['act1'].get()
    act2 = obj['act2'].get()
    ar = scn['actions'][typ][act1]
    ar[ ar.index( act2 ) ] = val
    load_act2()

def edit_act( *args, **kwargs ):
    inp( set_act, obj['act2'].get() )

def new_act( val ):
    scn, typ = get_scn_typ()
    act1 = obj['act1'].get()
    ar = scn['actions'][typ][act1]
    ar.append( val )
    load_act2()

def add_act( *args, **kwargs ):
    inp( new_act, "New Action" )

def del_act( *args, **kwargs ):
    scn, typ = get_scn_typ()
    act1 = obj['act1'].get()
    act2 = obj['act2'].get()
    scn['actions'][typ][act1].remove( act2 )
    load_act2()

def save_data( *args, **kwargs ):
    post_json( '../update_data', obj['data'], dummy )
    
def del_scn( *args, **kwargs ):
    del obj['data']['scenarios'][ obj['scn'].get() ]
    reload_scn()

def new_scn( val ):
    obj['data']['scenarios'][val] = { "actions": {"test": { "test": [ "test" ] } } }
    reload_scn()
    
def add_scn( *args, **kwargs ):
    inp( new_scn, "New Scene" )

def set_scn( val ):
    scn_nm = obj['scn'].get()
    obj['data']['scenarios'][val] = obj['data']['scenarios'][scn_nm]
    del obj['data']['scenarios'][scn_nm]
    populate_scenarios()

def edit_scn( *args, **kwargs ):
    inp( set_scn, obj['scn'].get() )

def main():
    obj['dmain'] = doc.add_div('d1')
    obj['dmain'].add_br()
    obj['dmain'].elm <= P( '&#x915;&#x94d;&#x930;&#x93f;&#x92f;&#x93e;&#x20;&#x938;&#x942;&#x91a;&#x940;&#x20;&#x92a;&#x94d;&#x930;&#x936;&#x93e;&#x938;&#x928;' )

    obj['scn'] = obj['dmain'].add_dropdown( [], populate_actors, '&#x938;&#x94d;&#x925;&#x93e;&#x928;' )
    obj['dmain'].add_button( "&#x2795;", add_scn )
    obj['dmain'].add_button( "&#x1f58a;&#xfe0f;", edit_scn )
    obj['dmain'].add_button( "&#x274c;", del_scn )
    newline()

    obj['action_by'] = obj['dmain'].add_dropdown( [], change_action_by, '&#x915;&#x930;&#x94d;&#x924;&#x93e;' )
    obj['dmain'].add_button( "&#x2795;", add_actee )
    obj['dmain'].add_button( "&#x1f58a;&#xfe0f;", edit_actee )
    obj['dmain'].add_button( "&#x274c;", del_actee )
    newline()

    obj['act1'] = obj['dmain'].add_dropdown( [], load_act2, '&#x905;&#x935;&#x92f;&#x935;/&#x935;&#x938;&#x94d;&#x924;&#x942;' )
    obj['dmain'].add_button( "&#x2795;", add_obj )
    obj['dmain'].add_button( "&#x1f58a;&#xfe0f;", edit_obj )
    obj['dmain'].add_button( "&#x274c;", del_obj )
    newline()

    obj['act2'] = obj['dmain'].add_dropdown( [], dummy, '&#x915;&#x94d;&#x930;&#x93f;&#x92f;&#x93e;' )
    obj['dmain'].add_button( "&#x2795;", add_act )
    obj['dmain'].add_button( "&#x1f58a;&#xfe0f;", edit_act )
    obj['dmain'].add_button( "&#x274c;", del_act )
    newline()

    obj['dmain'].add_button( "Save", save_data )

    get_json( '../get_data', data_loaded )
    

