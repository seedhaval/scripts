from browser import alert, document, ajax, timer, window
from browser.html import *
import time
import uuid
from browser.widgets.dialog import EntryDialog
from browser import bind
import json
import random
import math
from datetime import datetime

def interp( s, e ):
    return range( s, e, int( math.copysign( 1, e - s ) ) )

def interp_2d( p1, p2 ):
    x1,y1 = p1
    x2,y2 = p2
    dx = x2-x1
    dy = y2-y1
    pts = max( abs(dx), abs(dy) )
    ix = dx * 1.0 / pts
    iy = dy * 1.0 / pts
    return [[int(x1+(ix*i)),int(y1+(iy*i))] for i in range( int(pts+1) )]

def interp_ar( ar ):
    ar2 = [interp( ar[i], ar[i+1] ) for i in range( len(ar) - 1 )]
    ar2.append( interp( ar[-1], ar[0] ) )
    out = [y for x in ar2 for y in x]
    return out

def interp_2d_ar( ar ):
    ar2 = [interp_2d( ar[i], ar[i+1] ) for i in range( len(ar) - 1 )]
    ar2.append( interp_2d( ar[-1], ar[0] ) )
    out = [y for x in ar2 for y in x]
    return out

def gen_rnd_interp( s, e, cnt ):
    ar = [random.randint(s,e) for i in range(cnt)]
    return interp_ar( ar )

def get_angle(ar):
    a,b,c = ar
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang
 
def get_scale(ar):
    a,b,c = ar
    l1 = math.sqrt( (b[0]-a[0])**2 + (b[1]-a[1])**2 )
    l2 = math.sqrt( (c[0]-a[0])**2 + (c[1]-a[1])**2 )
    return l2/l1

class FileUpld():
    def __init__( self, prnt, cb ):
        self.prnt = prnt
        self.cb = cb
        elm = INPUT( 'File', type='file' )
        self.elm = elm
        self.prnt.elm <= elm
        self.elm.bind( 'change', cb )

    def get( self ):
        v = self.elm.value
        if len( v.strip() ) == 0:
            return None
        return v.split('\\')[-1]

    def reset( self ):
        self.elm.value = ''

class Canvas():
    def __init__( self, prnt, zidx, cb ):
        self.prnt = prnt
        self.zidx = zidx
        self.brightness = 100
        self.contrast = 100
        self.width = prnt.elm.offsetWidth
        self.height = prnt.elm.offsetHeight
        elm = CANVAS('', width=self.width, height=self.height)
        elm.style.zIndex = zidx
        self.elm = elm

        self.cb = cb

        self.img = None
        self.img_src = None

        self.img_natural_width = None
        self.img_natural_height = None
        self.opq_w = None
        self.opq_h = None

        self.scl = None
        self.ar = None
        self.state = {}
        self.params = {}
        self.params[ 'top' ] = 0
        self.params[ 'left' ] = 0
        self.params[ 'scaleX' ] = 1.0
        self.params[ 'scaleY' ] = 1.0
        self.params[ 'rotate' ] = 0
        self.params[ 'anchor_pt' ] = [0,0]
        self.params['anim_step'] = 15

        self.set_bind( self.cb )
        self.prnt.elm <= elm
        self.ctx = self.elm.getContext('2d')
        self.ctx.canvas.width = self.width
        self.ctx.canvas.height = self.height
        self.elm.bind( 'click', self.click )

    def inc_bright( self ):
        self.brightness += 10
        self.ref_bright_cont()

    def dec_bright( self ):
        self.brightness -= 10
        self.ref_bright_cont()

    def inc_contrast( self ):
        self.contrast += 10
        self.ref_bright_cont()

    def dec_contrast( self ):
        self.contrast -= 10
        self.ref_bright_cont()

    def ref_bright_cont( self ):
        self.elm.style.filter = "brightness(" + str(self.brightness) + "%) contrast(" + str(self.contrast) + "%)"

    def backup_state( self ):
        for p in ('top', 'left', 'scaleX', 'scaleY', 'rotate'):
            self.state[p] = self.params[p]

    def restore_state( self ):
        for p in ('top', 'left', 'scaleX', 'scaleY', 'rotate'):
            self.params[p] = self.state[p]
        self.elm.top = self.params['top']
        self.elm.left = self.params['left']
        self.transform()

    def set_bind( self, f ):
        self.params['click_handler'] = f

    def slow( self ):
        self.params['anim_step'] += 10

    def fast( self ):
        self.params['anim_step'] -= 10

    def click( self, evt ):
        self.params['click_handler']( evt )

    def transform( self ):
        self.elm.style.transform = f'rotate({self.params["rotate"]}deg) scaleX({self.params["scaleX"]}) scaleY({self.params["scaleY"]})'

    def rotate( self, ang ):
        self.params['rotate'] = ( self.params['rotate'] + ang ) % 360
        self.transform()

    def scale( self, x ):
        self.params['scaleX'] = self.params['scaleX'] * x
        self.params['scaleY'] = self.params['scaleY'] * x
        self.transform()

    def flip_h( self ):
        self.params[ 'scaleX' ] *= -1
        self.transform()

    def flip_v( self ):
        self.params[ 'scaleY' ] *= -1
        self.transform()

    def get_img_fit_scale( self ):
        w, h, nw, nh = ( self.width, self.height, self.img_natural_width, self.img_natural_height )
        if w >= nw and h >= nh:
            return 1
        sx = w / nw
        sy = h / nh
        return min( sx, sy )
        
    def draw_img( self, *args, **kwargs ):
        self.img_natural_width = self.img.naturalWidth
        self.img_natural_height = self.img.naturalHeight 
        self.scl = self.get_img_fit_scale()
        self.opq_w = self.img_natural_width * self.scl
        self.opq_h = self.img_natural_height * self.scl
        self.ctx.drawImage( self.img, 0, 0, self.img_natural_width, self.img_natural_height, (self.width - self.opq_w)/2, (self.height - self.opq_h)/2, self.opq_w, self.opq_h )

    def add_img( self, s ):
        self.clear()
        img = IMG()
        img.bind( 'load', self.draw_img )
        img['src'] = s
        self.img = img
        self.img_src = s

    def draw_point( self, x, y ):
        self.ctx.beginPath()
        self.ctx.arc( x, y, 3, 0, 6.28, False )
        self.ctx.fillStyle = 'green'
        self.ctx.fill()
        self.ctx.closePath()

    def draw_poly( self, ar ):
        self.ctx.beginPath()
        self.ctx.moveTo( ar[0][0], ar[0][1] )
        for p in ar[1:]:
            self.ctx.lineTo( p[0], p[1] )
        self.ctx.lineTo( ar[0][0], ar[0][1] )
        self.ctx.stroke()
        self.ctx.closePath()

    def get_bbox( self, ar ):
        minx = min( [x[0] for x in ar] )
        maxx = max( [x[0] for x in ar] )
        miny = min( [x[1] for x in ar] )
        maxy = max( [x[1] for x in ar] )
        return ( minx, miny, maxx, maxy )

    def trim( self, ar ):
        minx, miny, maxx, maxy = self.get_bbox( ar )
        cut = self.ctx.getImageData( minx, miny, maxx - minx, maxy - miny )
        self.clear()
        self.ctx.putImageData( cut, 0, 0 )

    def crop( self, ar ):
        self.ctx.beginPath()
        self.ctx.moveTo( ar[0][0], ar[0][1] )
        for p in ar[1:]:
            self.ctx.lineTo( p[0], p[1] )
        self.ctx.closePath()
        self.ctx.globalCompositeOperation = 'destination-in'
        self.ctx.fill()
        self.ctx.globalCompositeOperation = 'source-over'
        self.trim( ar )

    def draw_multiline( self, ar ):
        self.ctx.beginPath()
        self.ctx.moveTo( ar[0][0], ar[0][1] )
        for p in ar[1:]:
            self.ctx.lineTo( p[0], p[1] )
        self.ctx.stroke()
        self.ctx.closePath()

    def clear( self ):
        self.ctx.clearRect( 0, 0, self.width, self.height )

    def show_path( self ):
        self.clear()
        for x,y in self.ar:
            self.draw_point( x, y )
        self.draw_poly( self.ar )

    def get_xy( self, evt ):
        x = evt.clientX - self.prnt.elm.offsetLeft
        y = evt.clientY - self.prnt.elm.offsetTop
        return ( x, y )

    def push_point( self, evt ):
        x, y = self.get_xy( evt )
        self.ar.append( [x,y] )
        self.show_path()

    def pop_point( self, *args, **kwargs ):
        self.ar.pop()
        self.show_path()

    def reset_points( self, *args, **kwargs ):
        self.ar = []

    def set_draw_poly_mode( self, *args, **kwargs ):
        self.reset_points()
        self.set_bind( self.push_point )

    def add_poly_buttons( self, dpan, cb ):
        dpan.add_button( '🔙', self.pop_point )
        dpan.add_button( '🗑️', self.reset_points )
        dpan.add_button( '✅', cb )
        self.params[ 'draw_path_cb' ] = cb

    def get_b64( self ):
        return self.elm.toDataURL().split(',',1)[1]

    def move( self, x, y ):
        self.params[ 'left' ] += x
        self.params[ 'top' ] += y
        self.elm.left += x
        self.elm.top += y

    def get_dxy( self, evt ):
        ar = self.get_npt( evt, 2 )
        if not ar:
            return ( None, None )
        dx = ar[1][0] - ar[0][0]
        dy = ar[1][1] - ar[0][1]
        return ( dx, dy )

    def get_npt( self, evt, n ):
        x, y = self.get_xy( evt )
        self.ar.append( [x,y] )
        self.show_path()
        if len( self.ar ) == n:
            ar = [x for x in self.ar]
            self.reset_points()
            self.clear()
            return ar

    def move_pt( self, evt ):
        dx, dy = self.get_dxy( evt )
        if dx:
            self.params[ 'move_callback_function' ]( dx, dy )

    def set_move( self, cb ):
        self.params[ 'move_callback_function' ] = cb
        self.reset_points()
        self.set_bind( self.move_pt )

    def angle_pt( self, evt ):
        ar = self.get_npt( evt, 3 )
        if ar:
            self.params[ 'angle_callback_function' ]( get_angle( ar ) )

    def set_angle( self, cb ):
        self.params[ 'angle_callback_function' ] = cb
        self.reset_points()
        self.set_bind( self.angle_pt )

    def scale_pt( self, evt ):
        ar = self.get_npt( evt, 3 )
        if ar:
            self.params[ 'scale_callback_function' ]( get_scale( ar ) )

    def set_scale( self, cb ):
        self.params[ 'scale_callback_function' ] = cb
        self.reset_points()
        self.set_bind( self.scale_pt )

    def set_anchor_pt( self, x, y ):
        nx = x - self.params[ 'left' ]
        ny = y - self.params[ 'top' ]
        self.params[ 'anchor_pt' ] = [nx,ny]

    def anchor_pt( self, evt ):
        x, y = self.get_xy( evt )
        self.params[ 'anchor_callback_function' ]( x, y )

    def set_anchor( self, cb ):
        self.params[ 'anchor_callback_function' ] = cb
        self.set_bind( self.anchor_pt )

    def stop_anim( self ):
        self.params[ 'anim' ] = False
        self.restore_state()

    def get_anim_ref( self, ts, step_size ):
        ar = self.params[ 'anim_ar' ]
        cycle_len = len( ar )
        if not self.params[ 'refts' ]:
            self.params[ 'refts' ] = ts
            self.params[ 'prevstep' ] = 0
        dms = int( ts - self.params[ 'refts' ] )
        dstp = int( dms / step_size ) % cycle_len
        has_chg = dstp != self.params[ 'prevstep' ]
        self.params[ 'prevstep' ] = dstp
        return ( has_chg, ar[dstp] )

    def init_anim( self, ar, f ):
        self.params[ 'anim_ar' ] = ar
        self.params[ 'anim' ] = True
        self.params[ 'refts' ] = None
        self.backup_state()
        window.requestAnimationFrame( f )

    def anim_path_loop( self, ts ):
        has_chg, pt = self.get_anim_ref( ts, self.params['anim_step'] )
        if has_chg and self.params[ 'anim' ]:
            x,y = pt
            self.elm.left = x
            self.elm.top = y
        if self.params['anim']:
            window.requestAnimationFrame( self.anim_path_loop )

    def anim_rot_loop( self, ts ):
        has_chg, rot = self.get_anim_ref( ts, self.params['anim_step'] )
        if has_chg and self.params[ 'anim' ]:
            self.params['rotate'] = rot
            self.transform()
        if self.params['anim']:
            window.requestAnimationFrame( self.anim_rot_loop )

    def anim_scl_loop( self, ts ):
        has_chg, pt = self.get_anim_ref( ts, self.params['anim_step'] )
        if has_chg and self.params[ 'anim' ]:
            x,y = pt
            self.params['scaleX'] = x / 100.0
            self.params['scaleY'] = y / 100.0
            self.transform()
        if self.params['anim']:
            window.requestAnimationFrame( self.anim_scl_loop )

    def animate_path( self, ar ):
        ax,ay = self.params[ 'anchor_pt' ]
        ar2 = [[x-ax,y-ay] for x,y in ar]
        self.init_anim( interp_2d_ar( ar2 ), self.anim_path_loop )

    def animate_rotate( self, a1, a2 ):
        self.init_anim( gen_rnd_interp( a1, a2, 10 ), self.anim_rot_loop )

    def animate_scale( self, scl ):
        p1 = [int(self.params['scaleX']*100), int(self.params['scaleY']*100)]
        p2 = [int(p1[0]*scl),int(p1[1]*scl)]
        self.init_anim( interp_2d_ar( [p1,p2] ), self.anim_scl_loop )

class DropDown():
    def __init__( self, prnt, ar, cb, lbl ):
        self.prnt = prnt
        self.ar = ar
        self.cb = cb
        self.id = str(uuid.uuid4())
        elm = SELECT('')
        elm['id'] = self.id
        lbl = LABEL( lbl )
        lbl['for'] = self.id
        self.prnt.elm <= lbl
        self.prnt.elm <= elm
        self.elm = elm
        self.lbl = lbl
        for o in ar:
            e = OPTION( o, value=o )
            self.elm <= e
        self.elm.bind( 'change', cb )

    def get( self ):
        if len( self.ar ) == 0:
            return ""
        return self.elm.options[ self.elm.selectedIndex ].value

    def set( self, txt ):
        self.elm.value = txt

    def clear( self ):
        for i in range( len(self.elm.options) )[::-1]:
            self.elm.remove( i )

    def change( self, ar ):
        self.ar = ar
        self.clear()
        for o in ar:
            e = OPTION( o, value=o )
            self.elm <= e

    def hide( self ):
        self.elm.style.display = 'none'
        self.lbl.style.display = 'none'

    def show( self ):
        self.elm.style.display = 'inline'
        self.lbl.style.display = 'inline'

class MultiSelectDropDown():
    def __init__( self, prnt, ar, sz, lbl ):
        self.prnt = prnt
        self.ar = ar
        self.sz = sz
        self.id = str(uuid.uuid4())
        elm = SELECT('')
        elm['id'] = self.id
        elm['size'] = self.sz
        elm['multiple'] = 'multiple'
        lbl = LABEL( lbl )
        lbl['for'] = self.id
        self.prnt.elm <= lbl
        self.prnt.elm <= elm
        self.elm = elm
        for o in ar:
            e = OPTION( o, value=o )
            self.elm <= e

    def get( self ):
        if len( self.ar ) == 0:
            return []
        out = []
        for i in range( len(self.elm.options) ):
            opt = self.elm.options[i]
            if opt.selected:
                out.append( opt.value )
        return out

    def clear( self ):
        for i in range( len(self.elm.options) )[::-1]:
            self.elm.remove( i )

    def change( self, ar ):
        self.ar = ar
        self.clear()
        for o in ar:
            e = OPTION( o, value=o )
            self.elm <= e

    def set( self, ar ):
        if len( self.ar ) == 0:
            return
        for i in range( len(self.elm.options) ):
            opt = self.elm.options[i]
            if opt.value in ar:
                opt.selected = True
            else:
                opt.selected = False

class VideoControl():
    def __init__( self, prnt, vid ):
        self.prnt = prnt
        self.vid = vid
        self.elm = self.prnt.elm
        self.add_play()
        self.add_pause()
        self.add_rewind()
        self.add_forward()
        self.add_slow()
        self.add_fast()

    def play( self, *args, **kwargs ):
        self.vid.elm.play()

    def pause( self, *args, **kwargs ):
        self.vid.elm.pause()

    def forward( self, *args, **kwargs ):
        self.vid.elm.currentTime += 50

    def rewind( self, *args, **kwargs ):
        self.vid.elm.currentTime -= 50

    def slow( self, *args, **kwargs ):
        self.vid.elm.playbackRate -= 0.25

    def fast( self, *args, **kwargs ):
        self.vid.elm.playbackRate += 0.25

    def add_play( self ):
        Button( self, '▶️', self.play )

    def add_pause( self ):
        Button( self, '⏸️', self.pause )

    def add_rewind( self ):
        Button( self, '⏪', self.rewind )

    def add_forward( self ):
        Button( self, '⏩', self.forward )
    def add_slow( self ):
        Button( self, '🚲', self.slow )

    def add_fast( self ):
        Button( self, '🚂', self.fast )

class Button():
    def __init__( self, prnt, txt, cb ):
        self.prnt = prnt
        self.txt = txt
        self.cb = cb
        elm = BUTTON( txt )
        self.prnt.elm <= elm
        elm.bind( 'click', cb )
        self.elm = elm

    def add_class( self, cls ):
        self.elm.classList.add( cls )

    def hide( self ):
        self.elm.style.display = 'none'

    def show( self ):
        self.elm.style.display = 'inline'

class NewLine():
    def __init__( self, prnt, cnt ):
        self.prnt = prnt
        self.ar = []
        for i in range(cnt):
            elm = BR()
            self.prnt.elm <= elm
            self.ar.append( elm )

    def hide( self ):
        for e in self.ar:
            e.style.display = 'none'

    def show( self ):
        for e in self.ar:
            e.style.display = 'inline'

class SpanText():
    def __init__( self, prnt, lbl ):
        self.prnt = prnt
        self.lbl = lbl
        elm = SPAN(lbl)
        self.prnt.elm <= elm
        self.elm = elm

    def hide( self ):
        self.elm.style.display = 'none'

    def show( self ):
        self.elm.style.display = 'inline'

class Text():
    def __init__( self, prnt, sz, lbl, cb ):
        self.prnt = prnt
        self.sz = sz
        self.cb = cb
        self.lbl = lbl
        elm = INPUT( '', size=sz, type="text")
        self.id = str(uuid.uuid4())
        elm['id'] = self.id
        lbl = LABEL( lbl )
        lbl['for'] = self.id
        self.prnt.elm <= lbl
        self.lbl = lbl
        self.prnt.elm <= elm
        self.elm = elm
        self.elm.bind( 'input', cb )

    def clear( self ):
        self.elm.value = ""

    def get( self ):
        return self.elm.value

    def set( self, val ):
        self.elm.value = val

    def copy( self ):
        self.elm.select()
        document.execCommand('copy')

    def hide( self ):
        self.elm.style.display = 'none'
        self.lbl.style.display = 'none'

    def show( self ):
        self.elm.style.display = 'inline'
        self.lbl.style.display = 'inline'

class Video():
    def __init__( self, prnt ):
        self.prnt = prnt
        elm = VIDEO( '', controls='controls', autoplay='autoplay', muted='muted', loop='loop' )
        src = SOURCE( '', type="video/mp4", src='' )
        elm <= src
        self.elm = elm
        self.src = src
        self.prnt.elm <= elm

class Div():
    def __init__( self, prnt, cls ):
        self.prnt = prnt
        self.cls = cls
        elm = DIV( '', Class=cls)
        self.elm = elm
        self.prnt.elm <= elm

    def add_video( self ):
        return Video( self )

    def add_vid_cntrl( self, vid ):
        VideoControl( self, vid )

    def add_button( self, txt, cb ):
        return Button( self, txt, cb )

    def add_text( self, sz, lbl, cb ):
        return Text( self, sz, lbl, cb )

    def add_textarea( self, rows, cols ):
        return TextArea( self, rows, cols )

    def add_dropdown( self, ar, cb, lbl ):
        return DropDown( self, ar, cb, lbl )

    def add_file_upld( self, cb ):
        return FileUpld( self, cb )

    def add_canvas( self, zidx, cb ):
        return Canvas( self, zidx, cb )

    def add_multi_select_dropdown( self, ar, sz, lbl ):
        return MultiSelectDropDown( self, ar, sz, lbl )

    def set( self, txt ):
        self.elm.innerText = txt

    def clear( self ):
        self.elm.innerHTML = ''

    def add_br( self, cnt=1 ):
        return NewLine( self, cnt )

    def add_span( self, txt ):
        return SpanText( self, txt )

    def add_hr( self ):
        self.elm <= HR('')

    def add_div( self, cls ):
        return Div( self, cls )

    def add_space( self, cnt ):
        self.elm <= SPAN( "&nbsp;"*cnt )

class TextArea():
    def __init__( self, prnt, rows, cols ):
        self.prnt = prnt
        self.rows = rows
        self.cols = cols
        elm = TEXTAREA( '', rows=rows, cols=cols )
        self.prnt.elm <= elm
        self.elm = elm

    def clear( self ):
        self.elm.value = ""

    def get( self ):
        return self.elm.value

    def set( self, val ):
        self.elm.value = val

    def clip_copy( self ):
        self.elm.focus()
        self.elm.select()
        document.execCommand( 'copy' )

class Doc():
    def __init__( self ):
        self.elm = document

    def add_div( self, cls ):
        return Div( self, cls )

    def add_br( self ):
        self.elm <= BR('')

def cache_bust():
    return 'cb=' + str(round(time.time()*1000))

def get( url, mthd ):
    req = ajax.ajax()
    req.bind( 'complete', mthd )
    req.open( 'GET', '../' + url, False )
    req.send()

def get_json( url, cb ):
    def cb_wrap( rsp ):
	if rsp.status in (0,200):
            cb( rsp.json )
	elif rsp.status == 500:
	  alert( 'API error' )

    req = ajax.ajax()
    req.bind( 'complete', cb_wrap )
    req.open( 'GET', '../' + url, False )
    req.send()

def post_json( url, inp, cb ):
    def cb_wrap( rsp ):
	if rsp.status in (0,200):
            cb( rsp.json )
	elif rsp.status == 500:
	  alert( 'API error' )

    data = json.dumps( inp, ensure_ascii=False )
    ajax.post( '../' + url, data=data, headers={"Content-Type": "application/json"}, oncomplete=cb_wrap )

def inp( cb, title, top=100, left=80 ):
	d = EntryDialog( title, "Name" , top=top, left=left)
	@bind( d, "entry" )
	def entry( ev ):
		val = d.value
		d.close()
		cb( val )

def dummy( *args, **kwargs ):
    return 1

class DebugInfo():
    def __init__(self):
        self.txt = ''

    def add( self, txt ):
        self.txt += datetime.now().strftime('%H:%M:%S.%f')[:-3] + " " + txt + "\n"

    def show( self ):
        alert( self.txt )

doc = Doc()
debug = DebugInfo()
