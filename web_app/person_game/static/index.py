from bryhelper import *

obj = {}

def newline():
    obj['dmain'].add_br()
    obj['dmain'].add_br()

def redirect( url ):
    window.location.href = url

def main():
    obj['dmain'] = doc.add_div('d1')
    obj['dmain'].add_br()
    obj['dmain'].elm <= P( 'Index' )
    obj['dmain'].add_button( "&#x972;&#x915;&#x94d;&#x936;&#x928;&#x20;&#x917;&#x947;&#x92e;", lambda x: redirect( 'game.html') )
    newline()
    obj['dmain'].add_button( "&#x915;&#x94d;&#x930;&#x93f;&#x92f;&#x93e;&#x20;&#x938;&#x942;&#x91a;&#x940;&#x20;&#x92a;&#x94d;&#x930;&#x936;&#x93e;&#x938;&#x928;", lambda x: redirect( 'actadmin.html') )
    newline()
    obj['dmain'].add_button( "Unicode to HTML convertor", lambda x: redirect( 'uni2hex.html') )

