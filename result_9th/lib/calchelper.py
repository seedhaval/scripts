def oneof(md, nm, txt_ar):
    type, cols = (md['type'], md['cols'])
    if type != 'all' and nm not in cols:
        return
    ar = txt_ar.strip().split()
    if not any([x in md for x in ar]):
        return
    for idx in ar:
        if idx in md and str(md[idx]).strip() != '':
            md[nm] = md[idx]
            return


def add_comment(md, cmnt):
    md['fin.cmnt'] += f"{cmnt}, "


def auto_condo(md, nm, sub):
    if nm not in md:
        return
    if 33 <= md[nm] <= 35:
        add_comment(md, f"Automatic Condonation - {sub}")
        md[nm] = 35


def get_grade(md, nm, base, total=100):
    type, cols = (md['type'], md['cols'])
    if type != 'all' and nm not in cols:
        return
    if base not in md:
        return
    marks = md[base] * (100/total)
    if marks >= 60:
        val = 'अ'
    elif marks >= 45:
        val = 'ब'
    elif marks >= 35:
        val = 'क'
    elif marks >= 0:
        val = 'ड'
    else:
        val = ''
    md[nm] = val


def add(md, nm, txt_ar):
    type, cols = (md['type'], md['cols'])
    if type != 'all' and nm not in cols:
        return
    ar = txt_ar.strip().split()
    if not all([x in md for x in ar]):
        return
    md[nm] = sum([md[x] for x in ar])


def multiply(md, nm, base, mltpl):
    type, cols = (md['type'], md['cols'])
    if type != 'all' and nm not in cols:
        return
    if base not in md:
        return
    md[nm] = round(md[base] * mltpl, 2)


def get_fail_count(md, nm, txt):
    type, cols = (md['type'], md['cols'])
    if type != 'all' and nm not in cols:
        return
    ar = [x.split(':') for x in txt.strip().split()]
    if not all([x[0] in md for x in ar]):
        return
    val = 0
    for row in ar:
        val += 1 if md[row[0]] < float(row[1]) else 0
    md[nm] = val


def get_fail_count_lt(md, cntvar, txtvar, txt_ar, threshold):
    txt_ar2 = ' '.join([f"{x}:{threshold}" for x in txt_ar.split()])
    get_fail_count(md, cntvar, txt_ar2)
    if cntvar not in md or txtvar == '':
        return
    md[txtvar] = 'Pass' if md[cntvar] == 0 else f"F{md[cntvar]}"
