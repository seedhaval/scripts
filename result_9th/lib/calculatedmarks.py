def oneof(md, type, cols, nm, txt_ar):
    if type != 'all' and nm not in cols:
        return
    ar = txt_ar.strip().split()
    if not any([x in md for x in ar]):
        return
    for idx in ar:
        if idx in md and str(md[idx]).strip() != '':
            md[nm] = md[idx]
            return


def auto_condo(md, type, cols, nm, sub):
    if nm not in md:
        return
    if 33 <= md[nm] <= 35:
        md['fin.cmnt'] += f"Automatic Condonation - {sub}, "
        md[nm] = 35


def get_grade(md, type, cols, nm, base):
    if type != 'all' and nm not in cols:
        return
    if base not in md:
        return
    marks = md[base]
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


def get_fail_count(md, type, cols, nm, txt):
    if type != 'all' and nm not in cols:
        return
    ar = [x.split(':') for x in txt.strip().split()]
    if not all([x[0] in md for x in ar]):
        return
    val = 0
    for row in ar:
        val += 1 if md[row[0]] < float(row[1]) else 0
    md[nm] = val


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
    add(md, type, cols, "soc.1", "108 109")
    add(md, type, cols, "soc.2", "110 111")
    multiply(md, type, cols, "soc.3", "soc.2", 0.5)
    add(md, type, cols, "soc.4", "112 113")
    multiply(md, type, cols, "soc.5", "soc.4", 0.5)
    add(md, type, cols, "soc.6", "soc.1 soc.3 soc.5")
    add(md, type, cols, "soc.7", "116 117")
    add(md, type, cols, "soc.8", "118 119")
    multiply(md, type, cols, "soc.9", "soc.8", 0.5)
    add(md, type, cols, "soc.11", "120 121")
    multiply(md, type, cols, "soc.12", "soc.11", 0.5)
    add(md, type, cols, "soc.13", "soc.7 soc.9 soc.12")
    add(md, type, cols, "soc.14", "soc.6 soc.13")
    multiply(md, type, cols, "soc.15", "soc.14", 0.5)


def calc_technical(md, type, cols):
    add(md, type, cols, "tec.1", "122 123 124")
    multiply(md, type, cols, "tec.2", "tec.1", 0.71428)
    add(md, type, cols, "tec.3", "125 126 127")
    multiply(md, type, cols, "tec.4", "tec.3", 0.71428)
    add(md, type, cols, "tec.5", "tec.2 tec.4")
    multiply(md, type, cols, "tec.6", "tec.5", 0.5)


def calc_arogya(md, type, cols):
    add(md, type, cols, "aro.1", "128 129")
    add(md, type, cols, "aro.2", "130 131")
    add(md, type, cols, "aro.3", "aro.1 aro.2")
    multiply(md, type, cols, "aro.4", "aro.3", 0.5)


def calc_jals(md, type, cols):
    add(md, type, cols, "jals.1", "132 133")
    add(md, type, cols, "jals.2", "134 135")
    add(md, type, cols, "jals.3", "jals.1 jals.2")
    multiply(md, type, cols, "jals.4", "jals.3", 0.5)


def calc_ncc(md, type, cols):
    add(md, type, cols, "ncc.1", "136 137")
    add(md, type, cols, "ncc.2", "138 139")
    add(md, type, cols, "ncc.3", "ncc.1 ncc.2")
    multiply(md, type, cols, "ncc.4", "ncc.3", 0.5)


def calc_unit_1(md, type, cols):
    add(md, type, cols, 'tmp.1', '37 38')
    add(md, type, cols, 'tmp.2', '106 107')
    add(md, type, cols, 'gc1.6', '70 71')
    add(md, type, cols, 'gc1.7', '86 87')
    oneof(md, type, cols, 'gc1.1', '13 25 tmp.1')
    oneof(md, type, cols, 'gc1.2', 'tmp.2 122')
    add(md, type, cols, 'gc1.3', '1 gc1.1 58 gc1.6 gc1.7 gc1.2')
    multiply(md, type, cols, 'gc1.4', 'gc1.3', 0.71428)
    get_fail_count(md, type, cols, 'gc1.fcount',
                   '1:7 gc1.1:7 58:7 gc1.6:14 gc1.7:7 gc1.2:7')
    if 'gc1.fcount' in md:
        if md['gc1.fcount'] == 0:
            md['gc1.5'] = 'Pass'
        else:
            md['gc1.5'] = f"F{md['gc1.fcount']}"


def calc_unit_2(md, type, cols):
    add(md, type, cols, 'tmp.1', '47 48')
    add(md, type, cols, 'tmp.2', '114 115')
    add(md, type, cols, 'gc2.6', '78 79')
    add(md, type, cols, 'gc2.7', '96 97')
    oneof(md, type, cols, 'gc2.1', '19 31 tmp.1')
    oneof(md, type, cols, 'gc2.2', 'tmp.2 125')
    add(md, type, cols, 'gc2.3', '7 gc2.1 64 gc2.6 gc2.7 gc2.2')
    multiply(md, type, cols, 'gc2.4', 'gc2.3', 0.71428)
    get_fail_count(md, type, cols, 'gc2.fcount',
                   '7:7 gc2.1:7 64:7 gc2.6:14 gc2.7:7 gc2.2:7')
    if 'gc2.fcount' in md:
        if md['gc2.fcount'] == 0:
            md['gc2.5'] = 'Pass'
        else:
            md['gc2.5'] = f"F{md['gc2.fcount']}"


def calc_term_1(md, type, cols):
    oneof(md, type, cols, 'ps.1', 'hin.2 snsk.2 ssh.3')
    add(md, type, cols, 'ps.2', 'eng.2 ps.1 mar.2')
    add(md, type, cols, 'ps.3', 'sci.3 mat.3')
    oneof(md, type, cols, 'ps.4', 'soc.6 tec.2')
    add(md, type, cols, 'ps.5', 'ps.2 ps.3 ps.4')
    multiply(md, type, cols, 'ps.6', 'ps.5', 0.1666)
    get_grade(md, type, cols, 'ps.8', 'aro.1')
    get_grade(md, type, cols, 'ps.9', 'jals.1')
    get_grade(md, type, cols, 'ps.10', 'ncc.1')
    get_fail_count(md, type, cols, 'ps.fcount',
                   'mar.2:35 ps.1:35 eng.2:35 mat.3:35 sci.3:35 ps.4:35')
    if 'ps.fcount' in md:
        if md['ps.fcount'] == 0:
            md['ps.7'] = 'Pass'
        else:
            md['ps.7'] = f"F{md['ps.fcount']}"


def calc_term_2(md, type, cols):
    oneof(md, type, cols, 'ds.1', 'hin.4 snsk.4 ssh.6')
    add(md, type, cols, 'ds.2', 'eng.4 ds.1 mar.4')
    add(md, type, cols, 'ds.3', 'sci.6 mat.6')
    oneof(md, type, cols, 'ds.4', 'soc.13 tec.4')
    add(md, type, cols, 'ds.5', 'ds.2 ds.3 ds.4')
    multiply(md, type, cols, 'ds.6', 'ds.5', 0.1666)
    get_grade(md, type, cols, 'ds.8', 'aro.2')
    get_grade(md, type, cols, 'ds.9', 'jals.2')
    get_grade(md, type, cols, 'ds.10', 'ncc.2')
    get_fail_count(md, type, cols, 'ds.fcount',
                   'mar.4:35 ds.1:35 eng.4:35 mat.6:35 sci.6:35 ds.4:35')
    if 'ds.fcount' in md:
        if md['ds.fcount'] == 0:
            md['ds.7'] = 'Pass'
        else:
            md['ds.7'] = f"F{md['ds.fcount']}"


def calc_final_step_1(md, type, cols):
    add(md, type, cols, 'fin.mar.1', 'mar.6')
    oneof(md, type, cols, 'fin.hin.1', 'hin.6 snsk.6 ssh.9')
    add(md, type, cols, 'fin.eng.1', 'eng.6')
    add(md, type, cols, 'fin.mat.1', 'mat.8')
    add(md, type, cols, 'fin.sci.1', 'sci.8')
    oneof(md, type, cols, 'fin.smj.1', 'soc.15 tec.6')
    add(md, type, cols, 'fin.aro.1', 'aro.4')
    add(md, type, cols, 'fin.jals.1', 'jals.4')
    add(md, type, cols, 'fin.ncc.1', 'ncc.4')
    md['fin.cmnt'] = ''


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


def calc_final_combined_lang(md, type, cols):
    get_fail_count(md, type, cols, 'tmp.lang.fail.cnt',
                   'fin.mar.1:35 fin.hin.1:35 fin.eng.1:35')
    get_fail_count(md, type, cols, 'tmp.lang.lessthan.25.cnt',
                   'fin.mar.1:25 fin.hin.1:25 fin.eng.1:25')
    if 'ssh.7' in md and 'ssh.8' in md:
        get_fail_count(md, type, cols, 'tmp.lang.lessthan.25.cnt2',
                       'ssh.7:13 ssh.8:13')
        md['tmp.lang.lessthan.25.cnt'] += md['tmp.lang.lessthan.25.cnt2']
    add(md, type, cols, 'tmp.lang.total',
        'fin.mar.1 fin.hin.1 fin.eng.1')

    if md['tmp.lang.fail.cnt'] == 0:
        md['tmp.lang.combined.pass'] = True
        return
    if md['tmp.lang.lessthan.25.cnt'] > 0:
        md['tmp.lang.combined.pass'] = False
        return
    if md['tmp.lang.total'] < 105:
        md['tmp.lang.combined.pass'] = False
        return
    md['tmp.lang.combined.pass'] = True
    md['fin.cmnt'] += "Combined passing भाषा गट, "


def calc_final_combined_maths(md, type, cols):
    get_fail_count(md, type, cols, 'tmp.maths.fail.cnt',
                   'fin.mat.1:35 fin.sci.1:35')
    get_fail_count(md, type, cols, 'tmp.maths.lessthan.25.cnt',
                   'fin.mat.1:25 fin.sci.1:25')
    add(md, type, cols, 'tmp.maths.total',
        'fin.mat.1 fin.sci.1')

    if md['tmp.maths.fail.cnt'] == 0:
        md['tmp.maths.combined.pass'] = True
        return
    if md['tmp.maths.lessthan.25.cnt'] > 0:
        md['tmp.maths.combined.pass'] = False
        return
    if md['tmp.maths.total'] < 70:
        md['tmp.maths.combined.pass'] = False
        return
    md['tmp.maths.combined.pass'] = True
    md['fin.cmnt'] += "Combined passing गणित गट, "


def calc_final_combined_passing(md, type, cols):
    if 'fin.mar.1' not in md:
        return
    calc_final_combined_lang(md, type, cols)
    calc_final_combined_maths(md, type, cols)


def calc_final_auto_condo(md, type, cols):
    auto_condo(md, type, cols, 'fin.mar.1', 'मराठी')
    auto_condo(md, type, cols, 'fin.hin.1', 'हिंदी / संस्कृत')
    auto_condo(md, type, cols, 'fin.eng.1', 'इंग्लिश')
    auto_condo(md, type, cols, 'fin.mat.1', 'गणित')
    auto_condo(md, type, cols, 'fin.sci.1', 'विज्ञान')
    auto_condo(md, type, cols, 'fin.smj.1', 'समाजशास्त्र / टेकनिकल')
    auto_condo(md, type, cols, 'fin.aro.1', 'आरोग्य व शा.शिक्षण')
    auto_condo(md, type, cols, 'fin.jals.1', 'जलसंरक्षण')
    auto_condo(md, type, cols, 'fin.ncc.1',
               'स्काऊट गाईड/NCC/RSP/स्व विकास कलारसास्वाद')


def calc_grace(md, type, cols):
    if 'tmp.lang.combined.pass' not in md:
        return
    add(md, type, cols, 'tmp.6.total',
        'fin.mar.1 fin.hin.1 fin.eng.1 fin.mat.1 fin.sci.1 fin.smj.1')
    get_fail_count(md, type, cols, 'tmp.total.fail.cnt',
                   'fin.mar.1:35 fin.hin.1:35 fin.eng.1:35 fin.mat.1:35 '
                   'fin.sci.1:35 fin.smj.1:35')
    if md['tmp.6.total'] < 210:
        return
    if md['tmp.total.fail.cnt'] == 0:
        return
    grace_req = []
    if md['tmp.lang.combined.pass'] != True:
        for sub in 'fin.mar.1 fin.hin.1 fin.eng.1'.split():
            if 25 <= md[sub] < 35:
                grace_req.append([sub, 35 - md[sub]])
    if md['tmp.maths.combined.pass'] != True:
        for sub in 'fin.mat.1 fin.sci.1'.split():
            if 25 <= md[sub] < 35:
                grace_req.append([sub, 35 - md[sub]])
    if 25 <= md['fin.smj.1'] < 35:
        grace_req.append(['fin.smj.1', 35 - md['fin.smj.1']])
    avlbl_grace = 20
    grace_applied = []
    for row in sorted(grace_req, key=lambda x: x[1]):
        if row[1] < avlbl_grace:
            avlbl_grace -= row[1]
            grace_applied.append(row)
            print(row)
        else:
            break


def calc_final(md, type, cols):
    calc_final_step_1(md, type, cols)
    calc_final_auto_condo(md, type, cols)
    calc_final_combined_passing(md, type, cols)
    calc_grace(md, type, cols)
    # calc_final_fail_count(md, type, cols)
    md['fin.cmnt'] = md['fin.cmnt'].strip().strip(',')


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
    calc_jals(md, type, cols)
    calc_ncc(md, type, cols)

    calc_unit_1(md, type, cols)
    calc_unit_2(md, type, cols)
    calc_term_1(md, type, cols)
    calc_term_2(md, type, cols)

    calc_final(md, type, cols)
