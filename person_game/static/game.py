from bryhelper import *

obj = {}

def newline():
    obj['dmain'].add_br()
    obj['dmain'].add_br()

def get_scn_typ():
    scn_nm = obj['scn'].get()
    scn = obj['data']['scenarios'][scn_nm]
    typ = obj['prsn_rev'][obj['action_by'].get()]
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
    obj['action_by'].change( [obj[x] for x in list(scn['actions'].keys())] )
    change_action_by()

def reload_scn():
    populate_scenarios()
    populate_actors()

def parse_person( *args, **kwargs ):
    obj['female'],_,obj['male'] = obj['person_jodi'].get().split()
    obj['prsn_rev'] = { obj['male']: 'male', obj['female']: 'female' }
    if obj['scn'].get():
        populate_actors()

def data_loaded( rsp ):
    obj['data'] = rsp['action']
    prsn_jodi = [x.replace(';',' &#x906;&#x923;&#x93f; ') for x in rsp['person']]
    obj['person_jodi'].change( prsn_jodi )
    parse_person()
    reload_scn()

def add_submit_button():
    pbtn = P( "" )
    obj['dmain'].elm <= pbtn
    pbtn <= BUTTON( "&#x915;&#x93e;&#x930;&#x94d;&#x92f;&#x20;&#x915;&#x930;&#x93e;" )

def main():
    obj['dmain'] = doc.add_div('d1')
    obj['dmain'].add_br()
    obj['dmain'].elm <= P( '&#x972;&#x915;&#x94d;&#x936;&#x928;&#x20;&#x917;&#x947;&#x92e;' )

    obj['person_jodi'] = obj['dmain'].add_dropdown( [], parse_person, '&#x91c;&#x94b;&#x921;&#x940;' )
    newline()


    obj['scn'] = obj['dmain'].add_dropdown( [], populate_actors, '&#x938;&#x94d;&#x925;&#x93e;&#x928;' )
    newline()

    obj['action_by'] = obj['dmain'].add_dropdown( [], change_action_by, '&#x915;&#x930;&#x94d;&#x924;&#x93e;' )
    newline()

    obj['act1'] = obj['dmain'].add_dropdown( [], load_act2, '&#x905;&#x935;&#x92f;&#x935;/&#x935;&#x938;&#x94d;&#x924;&#x942;' )
    newline()

    obj['act2'] = obj['dmain'].add_dropdown( [], dummy, '&#x915;&#x94d;&#x930;&#x93f;&#x92f;&#x93e;' )

    add_submit_button()

    get_json( '../get_data', data_loaded )
    

