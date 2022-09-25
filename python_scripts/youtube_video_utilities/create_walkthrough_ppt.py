from python_scripts.commonutil.helper import File
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from pygments import lexers

height = 31
max_scroll = 10
buffer = 2
width = 81

fl = File(r"D:\scripts\scripts\python_scripts\commonutil\tkhelper.py")
data = fl.readlines()
data_fmt = [x+' '*(width-len(x))+'.' for x in data]
cnt = len(data)
img_fldr = r"D:\tmp"
start = 0

lexer = lexers.get_lexer_by_name("python", stripnl=False)

for i, ln in enumerate(data, 1):
    ln_strp = ln.strip()
    ln = ln + (' ' * (width - len(ln)))
    if ln_strp.startswith('import ') or ln_strp.startswith('from '):
        pass
    elif ln_strp == '':
        pass
    else:
        if i - start >= max_scroll:
            start = i - 1 - buffer
            if start + height > cnt:
                start = cnt - height
        code = '\n'.join(data_fmt[start:start + height])
        with open(img_fldr + "\\" + ("%03d" % i) + ".png", "wb") as f:
            f.write(highlight(code, lexer,
                              ImageFormatter(line_number_chars=3, line_number_start=start + 1, font_size=28,
                                             hl_lines=[i - start])))
