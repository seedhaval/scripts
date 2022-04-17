from bryhelper import *

obj = {}

def newline():
    obj['dmain'].add_br()
    obj['dmain'].add_br()

def change_action_to( *args, **kwargs ):
    scn_nm = obj['scn'].get()
    scn = [x for x in obj['data']['scenarios'] if x['name'] == scn_nm][0]
    typ = f"to_{obj['action_to'].get().lower()}"
    act1_ar = [y for x in scn['actions'][typ] for y in x['act1']]
    obj['act1'].change( act1_ar )
    load_act2()

def load_act2( *args, **kwargs ):
    scn_nm = obj['scn'].get()
    scn = [x for x in obj['data']['scenarios'] if x['name'] == scn_nm][0]
    typ = f"to_{obj['action_to'].get().lower()}"
    act1 = obj['act1'].get()
    act2_ar = [y for x in scn['actions'][typ] for y in x['act2'] if act1 in x['act1']]
    obj['act2'].change( act2_ar )

def populate_scenarios():
    ar = [x['name'] for x in obj['data']['scenarios']]
    obj['scn'] = obj['dmain'].add_dropdown( ar, change_action_to, 'Scenario' )
    newline()
    
def populate_actors():
    obj['action_to'] = obj['dmain'].add_dropdown( ['Male', 'Female'], change_action_to, 'Action To' )
    newline()
    obj['act1'] = obj['dmain'].add_dropdown( [], load_act2, 'Object' )
    newline()
    obj['act2'] = obj['dmain'].add_dropdown( [], dummy, 'Action' )
    change_action_to()

def add_submit_button():
    pbtn = P( "" )
    obj['dmain'].elm <= pbtn
    pbtn <= BUTTON( "Perform action" )

def data_loaded( rsp ):
    obj['data'] = rsp
    populate_scenarios()
    populate_actors()
    add_submit_button()

def main():
    obj['dmain'] = doc.add_div('d1')
    obj['dmain'].add_br()
    obj['dmain'].elm <= P( 'ACTION GAME' )
    obj['person_1'] = obj['dmain'].add_text( 23, 'Player 1', dummy )
    newline()
    obj['person_2'] = obj['dmain'].add_text( 23, 'Player 2', dummy )
    newline()
    get_json( '../get_data', data_loaded )
    

