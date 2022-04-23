from bryhelper import *

obj = {}

def newline():
    obj['dmain'].add_br()
    obj['dmain'].add_br()

def convert( *args, **kwargs ):
    out = ''.join( [f'&#x{format(ord(x),"x")};' for x in obj['txt_uni'].get()] )
    obj['txt_htm'].set(out)

def main():
    obj['dmain'] = doc.add_div('d1')
    obj['dmain'].add_br()
    obj['dmain'].elm <= P( 'Unicode to HTML' )
    obj['txt_uni'] = obj['dmain'].add_text( 20, 'Unicode', None)
    newline()
    obj['dmain'].add_button( "Convert", convert )
    newline()
    obj['txt_htm'] = obj['dmain'].add_text( 20, 'HTML', None)
    newline()
    obj['dmain'].add_button( "Copy", lambda x: obj['txt_htm'].copy() )

