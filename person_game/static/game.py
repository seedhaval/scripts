from bryhelper import *

obj = {}

def newline():
    obj['dmain'].add_br()
    obj['dmain'].add_br()

def get_scn_typ():
    scn_nm = obj['scn'].get()
    scn = obj['data']['scenarios'][scn_nm]
    typ = obj['action_to'].get()
    return (scn, typ)

def get_obj_ar():
    scn, typ = get_scn_typ()
    return list(scn['actions'][typ].keys())

def get_act_ar():
    scn, typ = get_scn_typ()
    act1 = obj['act1'].get()
    return scn['actions'][typ][act1]

def change_action_to( *args, **kwargs ):
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
    obj['action_to'].change( list(scn['actions'].keys()) )
    change_action_to()

def reload_scn():
    populate_scenarios()
    populate_actors()

def data_loaded( rsp ):
    obj['data'] = rsp
    reload_scn()

def add_submit_button():
    pbtn = P( "" )
    obj['dmain'].elm <= pbtn
    pbtn <= BUTTON( "&#x915;&#x93e;&#x930;&#x94d;&#x92f;&#x20;&#x915;&#x930;&#x93e;" )

def main():
    obj['dmain'] = doc.add_div('d1')
    obj['dmain'].add_br()
    obj['dmain'].elm <= P( '&#x972;&#x915;&#x94d;&#x936;&#x928;&#x20;&#x917;&#x947;&#x92e;' )

    obj['person_1'] = obj['dmain'].add_text( 23, '&#x92a;&#x94d;&#x932;&#x947;&#x905;&#x930;&#x20;&#x967;', dummy )
    newline()

    obj['person_2'] = obj['dmain'].add_text( 23, '&#x92a;&#x94d;&#x932;&#x947;&#x905;&#x930;&#x20;&#x968;', dummy )
    newline()

    obj['scn'] = obj['dmain'].add_dropdown( [], populate_actors, '&#x938;&#x94d;&#x925;&#x93e;&#x928;' )
    newline()

    obj['action_to'] = obj['dmain'].add_dropdown( [], change_action_to, '&#x909;&#x92a;&#x92d;&#x94b;&#x917;&#x924;&#x93e;' )
    newline()

    obj['act1'] = obj['dmain'].add_dropdown( [], load_act2, '&#x905;&#x935;&#x92f;&#x935;/&#x935;&#x938;&#x94d;&#x924;&#x942;' )
    newline()

    obj['act2'] = obj['dmain'].add_dropdown( [], dummy, '&#x915;&#x94d;&#x930;&#x93f;&#x92f;&#x93e;' )

    add_submit_button()

    get_json( '../get_data', data_loaded )
    

