def oneof(txt, md):
    for idx in txt.strip().split():
        if idx in md and str(md[idx]).strip() != '':
            return md[idx]
    return ''


def auto_condo(mrk):
    if 33 <= mrk <= 35:
        return 35
    return mrk


def get_grade(marks):
    if marks >= 60:
        return 'अ'
    elif marks >= 45:
        return 'ब'
    elif marks >= 35:
        return 'क'
    elif marks >= 0:
        return 'ड'
    return ''


def add(md, type, cols, nm, txt_ar):
    if type != 'all' and nm not in cols:
        return
    ar = txt_ar.strip().split()
    if not all([x in md for x in ar]):
        return
    md[nm] = sum([md[x] for x in ar])


def multiply(md, type, cols, nm, base, mltpl):
    if type != 'all' and nm not in cols:
        return
    if base not in md:
        return
    md[nm] = md[base] * mltpl


def calc_marathi(md, type, cols):
    add(md, type, cols, "mar.1", "3 4 5 6")
    add(md, type, cols, "mar.2", "2 mar.1")
    add(md, type, cols, "mar.3", "9 10 11 12")
    add(md, type, cols, "mar.4", "8 mar.3")
    add(md, type, cols, "mar.5", "mar.2 mar.4")
    multiply(md, type, cols, "mar.6", "mar.5", 0.5)


def calc_maths(md, type, cols):
    add(md, type, cols, "mat.1", "72 74 76")
    add(md, type, cols, "mat.2", "73 75 77")
    add(md, type, cols, "mat.3", "mat.1 mat.2")
    add(md, type, cols, "mat.4", "80 82 84")
    add(md, type, cols, "mat.5", "81 83 85")
    add(md, type, cols, "mat.6", "mat.4 mat.5")
    add(md, type, cols, "mat.7", "mat.3 mat.6")
    multiply(md, type, cols, "mat.8", "mat.7", 0.5)


def calc_sanskrit(md, type, cols):
    add(md, type, cols, "snsk.1", "15 16 17 18")
    add(md, type, cols, "snsk.2", "14 snsk.1")
    add(md, type, cols, "snsk.3", "21 22 23 24")
    add(md, type, cols, "snsk.4", "20 snsk.3")
    add(md, type, cols, "snsk.5", "snsk.2 snsk.4")
    multiply(md, type, cols, "snsk.6", "snsk.5", 0.5)


def calc_hindi(md, type, cols):
    add(md, type, cols, "hin.1", "27 28 29 30")
    add(md, type, cols, "hin.2", "26 hin.1")
    add(md, type, cols, "hin.3", "33 34 35 36")
    add(md, type, cols, "hin.4", "32 hin.3")
    add(md, type, cols, "hin.5", "hin.2 hin.4")
    multiply(md, type, cols, "hin.6", "hin.5", 0.5)


def calc_english(md, type, cols):
    add(md, type, cols, "eng.1", "60 61 62 63")
    add(md, type, cols, "eng.2", "59 eng.1")
    add(md, type, cols, "eng.3", "66 67 68 69")
    add(md, type, cols, "eng.4", "65 eng.3")
    add(md, type, cols, "eng.5", "eng.2 eng.4")
    multiply(md, type, cols, "eng.6", "eng.5", 0.5)


def calc_hindi_sanskrit_combo(md, type, cols):
    add(md, type, cols, "ssh.1", "39 41 43 45")
    add(md, type, cols, "ssh.2", "40 42 44 46")
    add(md, type, cols, "ssh.3", "ssh.1 ssh.2")
    add(md, type, cols, "ssh.4", "49 51 53 55")
    add(md, type, cols, "ssh.5", "50 52 54 56")
    add(md, type, cols, "ssh.6", "ssh.4 ssh.5")
    add(md, type, cols, "ssh.7", "ssh.1 ssh.4")
    multiply(md, type, cols, "ssh.7", "ssh.7", 0.5)
    add(md, type, cols, "ssh.8", "ssh.2 ssh.5")
    multiply(md, type, cols, "ssh.8", "ssh.8", 0.5)
    add(md, type, cols, "ssh.9", "ssh.7 ssh.8")


def calc_science(md, type, cols):
    add(md, type, cols, "sci.1", "88 90 91 92")
    add(md, type, cols, "sci.2", "89 93 94 95")
    add(md, type, cols, "sci.3", "sci.1 sci.2")
    add(md, type, cols, "sci.4", "98 100 101 102")
    add(md, type, cols, "sci.5", "99 103 104 105")
    add(md, type, cols, "sci.6", "sci.4 sci.5")
    add(md, type, cols, "sci.7", "sci.3 sci.6")
    multiply(md, type, cols, "sci.8", "sci.7", 0.5)


def calc_social_science(md, type, cols):
    if (type == 'all' or 'smj.1' in cols) and isvalid('101 102', md):
        md['smj.1'] = md['101'] + md['102']
    if (type == 'all' or 'smj.2' in cols) and isvalid('103 104', md):
        md['smj.2'] = md['103'] + md['104']
    if (type == 'all' or 'smj.3' in cols) and isvalid('105', md):
        md['smj.3'] = md['105'] / 2
    if (type == 'all' or 'smj.4' in cols) and isvalid('106', md):
        md['smj.4'] = md['106'] / 2
    if (type == 'all' or 'smj.5' in cols) and isvalid('107', md):
        md['smj.5'] = md['107'] / 2
    if (type == 'all' or 'smj.6' in cols) and isvalid('108', md):
        md['smj.6'] = md['108'] / 2
    if (type == 'all' or 'smj.7' in cols) and isvalid('smj.3 smj.4 smj.5 smj.6',
                                                      md):
        md['smj.7'] = md['smj.3'] + md['smj.4'] + md['smj.5'] + md['smj.6']
    if (type == 'all' or 'smj.8' in cols) and isvalid('smj.2 smj.7', md):
        md['smj.8'] = md['smj.2'] + md['smj.7']
    if (type == 'all' or 'smj.9' in cols) and isvalid('109 110', md):
        md['smj.9'] = md['109'] + md['110']
    if (type == 'all' or 'smj.10' in cols) and isvalid('111 112', md):
        md['smj.10'] = md['111'] + md['112']
    if (type == 'all' or 'smj.11' in cols) and isvalid('113', md):
        md['smj.11'] = md['113'] / 2
    if (type == 'all' or 'smj.12' in cols) and isvalid('114', md):
        md['smj.12'] = md['114'] / 2
    if (type == 'all' or 'smj.13' in cols) and isvalid('115', md):
        md['smj.13'] = md['115'] / 2
    if (type == 'all' or 'smj.14' in cols) and isvalid('116', md):
        md['smj.14'] = md['116'] / 2
    if (type == 'all' or 'amj.15' in cols) and isvalid(
            'smj.11 smj.12 smj.13 smj.14', md):
        md['amj.15'] = md['smj.11'] + md['smj.12'] + md['smj.13'] + md['smj.14']
    if (type == 'all' or 'smj.16' in cols) and isvalid('smj.10 amj.15', md):
        md['smj.16'] = md['smj.10'] + md['amj.15']
    if (type == 'all' or 'smj.17' in cols) and isvalid('smj.8 smj.16', md):
        md['smj.17'] = md['smj.8'] + md['smj.16']
    if (type == 'all' or 'smj.18' in cols) and isvalid('smj.17', md):
        md['smj.18'] = md['smj.17'] / 2


def calc_technical(md, type, cols):
    if (type == 'all' or 'tec.1' in cols) and isvalid('117 118 119', md):
        md['tec.1'] = md['117'] + md['118'] + md['119']
    if (type == 'all' or 'tec.2' in cols) and isvalid('tec.1', md):
        md['tec.2'] = md['tec.1'] * (100.00 / 140.00)
    if (type == 'all' or 'tec.3' in cols) and isvalid('120 121 122', md):
        md['tec.3'] = md['120'] + md['121'] + md['122']
    if (type == 'all' or 'tec.4' in cols) and isvalid('tec.3', md):
        md['tec.4'] = md['tec.3'] * (100.00 / 140.00)
    if (type == 'all' or 'tec.5' in cols) and isvalid('tec.2 tec.4', md):
        md['tec.5'] = md['tec.2'] + md['tec.4']
    if (type == 'all' or 'tec.6' in cols) and isvalid('tec.5', md):
        md['tec.6'] = md['tec.5'] / 2


def calc_arogya(md, type, cols):
    if (type == 'all' or 'aro.1' in cols) and isvalid('123 124 125 126 127',
                                                      md):
        md['aro.1'] = md['123'] + md['124'] + md['125'] + md['126'] + md['127']
    if (type == 'all' or 'aro.2' in cols) and isvalid('aro.1', md):
        md['aro.2'] = get_grade(md['aro.1'])
    if (type == 'all' or 'aro.3' in cols) and isvalid('128 129 130 131 132',
                                                      md):
        md['aro.3'] = md['128'] + md['129'] + md['130'] + md['131'] + md['132']
    if (type == 'all' or 'aro.4' in cols) and isvalid('aro.3', md):
        md['aro.4'] = get_grade(md['aro.3'])
    if (type == 'all' or 'aro.5' in cols) and isvalid('aro.1 aro.3', md):
        md['aro.5'] = md['aro.1'] + md['aro.3']
    if (type == 'all' or 'aro.6' in cols) and isvalid('aro.5', md):
        md['aro.6'] = md['aro.5'] / 2
    if (type == 'all' or 'aro.7' in cols) and isvalid('aro.6', md):
        md['aro.7'] = get_grade(md['aro.6'])


def calc_ncc(md, type, cols):
    if (type == 'all' or 'ncc.1' in cols) and isvalid(
            '133 134 135 136 137 138 139 140 141', md):
        md['ncc.1'] = md['133'] + md['134'] + md['135'] + md['136'] + md[
            '137'] + md['138'] + md['139'] + md['140'] + md['141']
    if (type == 'all' or 'ncc.2' in cols) and isvalid('ncc.1 142', md):
        md['ncc.2'] = md['ncc.1'] + md['142']
    if (type == 'all' or 'ncc.3' in cols) and isvalid(
            '143 144 145 146 147 148 149 150 151', md):
        md['ncc.3'] = md['143'] + md['144'] + md['145'] + md['146'] + md[
            '147'] + md['148'] + md['149'] + md['150'] + md['151']
    if (type == 'all' or 'ncc.4' in cols) and isvalid('ncc.3 152', md):
        md['ncc.4'] = md['ncc.3'] + md['152']
    if (type == 'all' or 'ncc.5' in cols) and isvalid('ncc.2 ncc.4', md):
        md['ncc.5'] = md['ncc.2'] + md['ncc.4']
    if (type == 'all' or 'ncc.6' in cols) and isvalid('ncc.5', md):
        md['ncc.6'] = md['ncc.5'] / 2
    if (type == 'all' or 'ncc.7' in cols) and isvalid('ncc.6', md):
        md['ncc.7'] = get_grade(md['ncc.6'])


def calc_unit_1(md, type, cols):
    if (type == 'all' or 'gc1.1' in cols):
        md['gc1.1'] = oneof('13 25 ssh.1', md)
    if (type == 'all' or 'gc1.2' in cols):
        md['gc1.2'] = oneof('smj.1 117', md)
    if (type == 'all' or 'gc1.3' in cols) and isvalid(
            '1 gc1.1 53 mat.1 sci.1 gc1.2', md):
        md['gc1.3'] = md['1'] + md['gc1.1'] + md['53'] + md['mat.1'] + md[
            'sci.1'] + md['gc1.2']
    if (type == 'all' or 'gc1.4' in cols) and isvalid('gc1.3', md):
        md['gc1.4'] = md['gc1.3'] * (100.00 / 140.00)
    if (type == 'all' or 'gc1.5' in cols) and isvalid(
            '1 gc1.1 53 mat.1 sci.1 gc1.2', md):
        val = 0
        val += 1 if md['1'] < 7 else 0
        val += 1 if md['gc1.1'] < 7 else 0
        val += 1 if md['53'] < 7 else 0
        val += 1 if md['mat.1'] < 14 else 0
        val += 1 if md['sci.1'] < 7 else 0
        val += 1 if md['gc1.2'] < 7 else 0
        if val == 0:
            md['gc1.5'] = 'Pass'
        else:
            md['gc1.5'] = f'F{val}'


def calc_unit_2(md, type, cols):
    if (type == 'all' or 'gc2.1' in cols):
        md['gc2.1'] = oneof('19 31 ssh.5', md)
    if (type == 'all' or 'gc2.2' in cols):
        md['gc2.2'] = oneof('smj.9 120', md)
    if (type == 'all' or 'gc2.3' in cols) and isvalid(
            '7 gc2.1 59 mat.8 sci.5 gc2.2', md):
        md['gc2.3'] = md['7'] + md['gc2.1'] + md['59'] + md['mat.8'] + md[
            'sci.5'] + md['gc2.2']
    if (type == 'all' or 'gc2.4' in cols) and isvalid('gc2.3', md):
        md['gc2.4'] = md['gc2.3'] * (100.00 / 140.00)
    if (type == 'all' or 'gc2.5' in cols) and isvalid(
            '7 gc2.1 59 mat.8 sci.5 gc2.2', md):
        val = 0
        val += 1 if md['7'] < 7 else 0
        val += 1 if md['gc2.1'] < 7 else 0
        val += 1 if md['59'] < 7 else 0
        val += 1 if md['mat.8'] < 14 else 0
        val += 1 if md['sci.5'] < 7 else 0
        val += 1 if md['gc2.2'] < 7 else 0
        if val == 0:
            md['gc2.5'] = 'Pass'
        else:
            md['gc2.5'] = f'F{val}'


def calc_term_1(md, type, cols):
    if (type == 'all' or 'ps.1' in cols):
        md['ps.1'] = oneof('hin.2 snsk.2 ssh.4', md)
    if (type == 'all' or 'ps.2' in cols) and isvalid('eng.2 ps.1 mar.2', md):
        md['ps.2'] = md['eng.2'] + md['ps.1'] + md['mar.2']
    if (type == 'all' or 'ps.3' in cols) and isvalid('sci.4 mat.7', md):
        md['ps.3'] = md['sci.4'] + md['mat.7']
    if (type == 'all' or 'ps.4' in cols):
        md['ps.4'] = oneof('smj.8 tec.2', md)
    if (type == 'all' or 'ps.5' in cols) and isvalid('ps.2 ps.3 ps.4', md):
        md['ps.5'] = md['ps.2'] + md['ps.3'] + md['ps.4']
    if (type == 'all' or 'ps.6' in cols) and isvalid('ps.5', md):
        md['ps.6'] = md['ps.5'] / 6
    if (type == 'all' or 'ps.7' in cols) and isvalid(
            'mar.2 ps.1 eng.2 mat.7 sci.4 ps.4', md):
        val = 0
        val += 1 if md['mar.2'] < 35 else 0
        val += 1 if md['ps.1'] < 35 else 0
        val += 1 if md['eng.2'] < 35 else 0
        val += 1 if md['mat.7'] < 35 else 0
        val += 1 if md['sci.4'] < 35 else 0
        val += 1 if md['ps.4'] < 35 else 0
        if val == 0:
            md['ps.7'] = 'Pass'
        else:
            md['ps.7'] = f'F{val}'


def calc_term_2(md, type, cols):
    if (type == 'all' or 'ds.1' in cols):
        md['ds.1'] = oneof('hin.4 snsk.4 ssh.8', md)
    if (type == 'all' or 'ds.2' in cols) and isvalid('eng.4 ds.1 mar.4', md):
        md['ds.2'] = md['eng.4'] + md['ds.1'] + md['mar.4']
    if (type == 'all' or 'ds.3' in cols) and isvalid('sci.8 mat.14', md):
        md['ds.3'] = md['sci.8'] + md['mat.14']
    if (type == 'all' or 'ds.4' in cols):
        md['ds.4'] = oneof('smj.16 tec.4', md)
    if (type == 'all' or 'ds.5' in cols) and isvalid('ds.2 ds.3 ds.4', md):
        md['ds.5'] = md['ds.2'] + md['ds.3'] + md['ds.4']
    if (type == 'all' or 'ds.6' in cols) and isvalid('ds.5', md):
        md['ds.6'] = md['ds.5'] / 6
    if (type == 'all' or 'ds.7' in cols) and isvalid(
            'mar.4 ds.1 eng.4 mat.14 sci.8 ds.4', md):
        val = 0
        val += 1 if md['mar.4'] < 35 else 0
        val += 1 if md['ds.1'] < 35 else 0
        val += 1 if md['eng.4'] < 35 else 0
        val += 1 if md['mat.14'] < 35 else 0
        val += 1 if md['sci.8'] < 35 else 0
        val += 1 if md['ds.4'] < 35 else 0
        if val == 0:
            md['ds.7'] = 'Pass'
        else:
            md['ds.7'] = f'F{val}'


def calc_final_step_1(md, type, cols):
    if (type == 'all' or 'fin.mar.t1' in cols) and isvalid('mar.6', md):
        md['fin.mar.1'] = md['mar.6']
        md['fin.mar.t1'] = md['mar.6']
    if (type == 'all' or 'fin.hin.t1' in cols) and isvalid(
            'snsk.6 hin.6 ssh.10', md):
        md['fin.hin.1'] = oneof('snsk.6 hin.6 ssh.10', md)
        md['fin.hin.t1'] = oneof('snsk.6 hin.6 ssh.10', md)
    if (type == 'all' or 'fin.eng.t1' in cols) and isvalid('eng.6', md):
        md['fin.eng.1'] = md['eng.6']
        md['fin.eng.t1'] = md['eng.6']
    if (type == 'all' or 'fin.grp.t1' in cols) and isvalid(
            'fin.mar.1 fin.hin.1 fin.eng.1', md):
        md['fin.grp.1'] = md['fin.mar.1'] + md['fin.hin.1'] + md['fin.eng.1']
        md['fin.grp.t1'] = md['fin.mar.1'] + md['fin.hin.1'] + md['fin.eng.1']
    if (type == 'all' or 'fin.mat.t1' in cols) and isvalid('mat.16', md):
        md['fin.mat.1'] = md['mat.16']
        md['fin.mat.t1'] = md['mat.16']
    if (type == 'all' or 'fin.sci.t1' in cols) and isvalid('sci.10', md):
        md['fin.sci.1'] = md['sci.10']
        md['fin.sci.t1'] = md['sci.10']
    if (type == 'all' or 'fin.grp.t2' in cols) and isvalid(
            'fin.mat.1 fin.sci.1', md):
        md['fin.grp.2'] = md['fin.mat.1'] + md['fin.sci.1']
        md['fin.grp.t2'] = md['fin.mat.1'] + md['fin.sci.1']
    if (type == 'all' or 'fin.soc.t1' in cols) and isvalid('smj.18 tec.6', md):
        md['fin.soc.1'] = oneof('smj.18 tec.6', md)
        md['fin.soc.t1'] = oneof('smj.18 tec.6', md)
    if (type == 'all' or 'fin.aro.t1' in cols) and isvalid('aro.7', md):
        md['fin.aro.1'] = md['aro.7']
        md['fin.aro.t1'] = md['aro.7']
    if (type == 'all' or 'fin.scout.t1' in cols) and isvalid('ncc.7', md):
        md['fin.scout.1'] = md['ncc.7']
        md['fin.scout.t1'] = md['ncc.7']
    if (type == 'all' or 'fin.total.t1' in cols) and isvalid(
            'fin.grp.1 fin.grp.2 fin.soc.1', md):
        md['fin.total.1'] = md['fin.grp.1'] + md['fin.grp.2'] + md['fin.soc.1']
        md['fin.total.t1'] = md['fin.grp.1'] + md['fin.grp.2'] + md['fin.soc.1']
    if (type == 'all' or 'fin.100.t1' in cols) and isvalid('fin.total.1', md):
        md['fin.100.1'] = md['fin.total.1'] / 6
        md['fin.100.t1'] = md['fin.total.1'] / 6


def calc_final_fail_count(md, type, cols):
    if (type == 'all' or 'fin.rem.t1' in cols) and isvalid('mar.6 fin.hin.1 '
                                                           'eng.6 mat.16 '
                                                           'sci.10 fin.soc.1',
                                                           md):
        val = 0
        val += 1 if md['mar.6'] < 35 else 0
        val += 1 if md['fin.hin.1'] < 35 else 0
        val += 1 if md['eng.6'] < 35 else 0
        val += 1 if md['mat.16'] < 35 else 0
        val += 1 if md['sci.10'] < 35 else 0
        val += 1 if md['fin.soc.1'] < 35 else 0
        md['fcount'] = val


def calc_final_combined_passing(md, type, cols):
    if (type == 'all' or 'fin.rem.t1' in cols) and isvalid('mar.6 fin.hin.1 '
                                                           'eng.6 mat.16 '
                                                           'sci.10 fin.soc.1',
                                                           md):
        if md['fcount'] == 0:
            md['lang_pass'], md['msci_pass'], md['msoc_pass'] = (
                True, True, True)
            return
        if md['mar.6'] < 25 or md['fin.hin.1'] < 25 or md['eng.6'] < 25:
            lang_pass = False
        elif md['mar.6'] + md['fin.hin.1'] + md['eng.6'] < 105:
            lang_pass = False
        else:
            lang_pass = True

        if md['mat.16'] < 25 or md['sci.10'] < 25:
            msci_pass = False
        elif md['mat.16'] + md['sci.10'] < 70:
            msci_pass = False
        else:
            msci_pass = True

        if md['fin.soc.1'] < 35:
            msoc_pass = False
        else:
            msoc_pass = True

        md['lang_pass'], md['msci_pass'], md['msoc_pass'] = (
            lang_pass, msci_pass, msoc_pass)


def calc_final_auto_condo(md, type, cols):
    if (type == 'all' or 'fin.rem.t1' in cols) and isvalid('mar.6 fin.hin.1 '
                                                           'eng.6 mat.16 '
                                                           'sci.10 fin.soc.1',
                                                           md):
        md['mar.6'] = auto_condo(md['mar.6'])
        md['fin.hin.1'] = auto_condo(md['fin.hin.1'])
        md['eng.6'] = auto_condo(md['eng.6'])
        md['mat.16'] = auto_condo(md['mat.16'])
        md['sci.10'] = auto_condo(md['sci.10'])
        md['fin.soc.1'] = auto_condo(md['fin.soc.1'])


def calculate(md, type, cols):
    calc_marathi(md, type, cols)
    calc_maths(md, type, cols)
    calc_sanskrit(md, type, cols)
    calc_hindi(md, type, cols)
    calc_english(md, type, cols)
    calc_hindi_sanskrit_combo(md, type, cols)
    calc_science(md, type, cols)
    calc_social_science(md, type, cols)
    calc_technical(md, type, cols)
    calc_arogya(md, type, cols)
    calc_ncc(md, type, cols)

    calc_unit_1(md, type, cols)
    calc_unit_2(md, type, cols)
    calc_term_1(md, type, cols)
    calc_term_2(md, type, cols)

    calc_final_step_1(md, type, cols)
    calc_final_fail_count(md, type, cols)
    calc_final_combined_passing(md, type, cols)
    calc_final_auto_condo(md, type, cols)
