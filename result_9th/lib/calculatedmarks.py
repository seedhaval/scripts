def isvalid(txt, md):
    for idx in txt.strip().split():
        if idx not in md:
            return False
    return True


def oneof(txt, md):
    for idx in txt.strip().split():
        if idx in md and str(md[idx]).strip() != '':
            return md[idx]
    return ''


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


def calculate(md, type, cols):
    if (type == 'all' or 'mar.1' in cols) and isvalid("3 4 5 6", md):
        md["mar.1"] = md["3"] + md["4"] + md["5"] + md["6"]
    if (type == 'all' or 'mar.2' in cols) and isvalid("2 mar.1", md):
        md["mar.2"] = md["2"] + md["mar.1"]
    if (type == 'all' or 'mar.3' in cols) and isvalid("9 10 11 12", md):
        md["mar.3"] = md["9"] + md["10"] + md["11"] + md["12"]
    if (type == 'all' or 'mar.4' in cols) and isvalid("8 mar.3", md):
        md["mar.4"] = md["8"] + md["mar.3"]
    if (type == 'all' or 'mar.5' in cols) and isvalid("mar.2 mar.4", md):
        md["mar.5"] = md["mar.2"] + md["mar.4"]
    if (type == 'all' or 'mar.6' in cols) and isvalid("mar.5", md):
        md["mar.6"] = md["mar.5"] / 2

    if (type == 'all' or 'mat.1' in cols) and isvalid("65 66", md):
        md["mat.1"] = md["65"] + md["66"]
    if (type == 'all' or 'mat.2' in cols) and isvalid("67 68", md):
        md["mat.2"] = md["67"] + md["68"]
    if (type == 'all' or 'mat.3' in cols) and isvalid("69 70", md):
        md["mat.3"] = md["69"] + md["70"]
    if (type == 'all' or 'mat.4' in cols) and isvalid("71 72", md):
        md["mat.4"] = md["71"] + md["72"]
    if (type == 'all' or 'mat.5' in cols) and isvalid("mat.4", md):
        md["mat.5"] = md["mat.4"] / 2
    if (type == 'all' or 'mat.6' in cols) and isvalid("mat.3 mat.5", md):
        md["mat.6"] = md["mat.3"] + md["mat.5"]
    if (type == 'all' or 'mat.7' in cols) and isvalid("mat.2 mat.6", md):
        md["mat.7"] = md["mat.2"] + md["mat.6"]

    if (type == 'all' or 'mat.8' in cols) and isvalid("73 74", md):
        md["mat.8"] = md["73"] + md["74"]
    if (type == 'all' or 'mat.9' in cols) and isvalid("75 76", md):
        md["mat.9"] = md["75"] + md["76"]
    if (type == 'all' or 'mat.10' in cols) and isvalid("77 78", md):
        md["mat.10"] = md["77"] + md["78"]
    if (type == 'all' or 'mat.11' in cols) and isvalid("79 80", md):
        md["mat.11"] = md["79"] + md["80"]
    if (type == 'all' or 'mat.12' in cols) and isvalid("mat.11", md):
        md["mat.12"] = md["mat.11"] / 2
    if (type == 'all' or 'mat.13' in cols) and isvalid("mat.10 mat.12", md):
        md["mat.13"] = md["mat.10"] + md["mat.12"]
    if (type == 'all' or 'mat.14' in cols) and isvalid("mat.9 mat.13", md):
        md["mat.14"] = md["mat.9"] + md["mat.13"]

    if (type == 'all' or 'mat.15' in cols) and isvalid("mat.7 mat.14", md):
        md["mat.15"] = md["mat.7"] + md["mat.14"]
    if (type == 'all' or 'mat.16' in cols) and isvalid("mat.15", md):
        md["mat.16"] = md["mat.15"] / 2

    if (type == 'all' or 'snsk.1' in cols) and isvalid("15 16 17 18", md):
        md["snsk.1"] = md["15"] + md["16"] + md["17"] + md["18"]
    if (type == 'all' or 'snsk.2' in cols) and isvalid("14 snsk.1", md):
        md["snsk.2"] = md["14"] + md["snsk.1"]
    if (type == 'all' or 'snsk.3' in cols) and isvalid("21 22 23 24", md):
        md["snsk.3"] = md["21"] + md["22"] + md["23"] + md["24"]
    if (type == 'all' or 'snsk.4' in cols) and isvalid("20 snsk.3", md):
        md["snsk.4"] = md["20"] + md["snsk.3"]
    if (type == 'all' or 'snsk.5' in cols) and isvalid("snsk.2 snsk.4", md):
        md["snsk.5"] = md["snsk.2"] + md["snsk.4"]
    if (type == 'all' or 'snsk.6' in cols) and isvalid("snsk.5", md):
        md["snsk.6"] = md["snsk.5"] / 2

    if (type == 'all' or 'hin.1' in cols) and isvalid("27 28 29 30", md):
        md["hin.1"] = md["27"] + md["28"] + md["29"] + md["30"]
    if (type == 'all' or 'hin.2' in cols) and isvalid("26 hin.1", md):
        md["hin.2"] = md["26"] + md["hin.1"]
    if (type == 'all' or 'hin.3' in cols) and isvalid("33 34 35 36", md):
        md["hin.3"] = md["33"] + md["34"] + md["35"] + md["36"]
    if (type == 'all' or 'hin.4' in cols) and isvalid("32 hin.3", md):
        md["hin.4"] = md["32"] + md["hin.3"]
    if (type == 'all' or 'hin.5' in cols) and isvalid("hin.2 hin.4", md):
        md["hin.5"] = md["hin.2"] + md["hin.4"]
    if (type == 'all' or 'hin.6' in cols) and isvalid("hin.5", md):
        md["hin.6"] = md["hin.5"] / 2

    if (type == 'all' or 'eng.1' in cols) and isvalid("55 56 57 58", md):
        md["eng.1"] = md["55"] + md["56"] + md["57"] + md["58"]
    if (type == 'all' or 'eng.2' in cols) and isvalid("54 eng.1", md):
        md["eng.2"] = md["54"] + md["eng.1"]
    if (type == 'all' or 'eng.3' in cols) and isvalid("61 62 63 64", md):
        md["eng.3"] = md["61"] + md["62"] + md["63"] + md["64"]
    if (type == 'all' or 'eng.4' in cols) and isvalid("60 eng.3", md):
        md["eng.4"] = md["60"] + md["eng.3"]
    if (type == 'all' or 'eng.5' in cols) and isvalid("eng.2 eng.4", md):
        md["eng.5"] = md["eng.2"] + md["eng.4"]
    if (type == 'all' or 'eng.6' in cols) and isvalid("eng.5", md):
        md["eng.6"] = md["eng.5"] / 2

    if (type == 'all' or 'ssh.1' in cols) and isvalid("37 38", md):
        md["ssh.1"] = md["37"] + md["38"]
    if (type == 'all' or 'ssh.2' in cols) and isvalid("39 40", md):
        md["ssh.2"] = md["39"] + md["40"]
    if (type == 'all' or 'ssh.3' in cols) and isvalid("41 42 43 44", md):
        md["ssh.3"] = md["41"] + md["42"] + md["43"] + md["44"]
    if (type == 'all' or 'ssh.4' in cols) and isvalid("ssh.2 ssh.3", md):
        md["ssh.4"] = md["ssh.2"] + md["ssh.3"]
    if (type == 'all' or 'ssh.5' in cols) and isvalid("45 46", md):
        md["ssh.5"] = md["45"] + md["46"]
    if (type == 'all' or 'ssh.6' in cols) and isvalid("47 48", md):
        md["ssh.6"] = md["47"] + md["48"]
    if (type == 'all' or 'ssh.7' in cols) and isvalid("49 50 51 52", md):
        md["ssh.7"] = md["49"] + md["50"] + md["51"] + md["52"]
    if (type == 'all' or 'ssh.8' in cols) and isvalid("ssh.6 ssh.7", md):
        md["ssh.8"] = md["ssh.6"] + md["ssh.7"]
    if (type == 'all' or 'ssh.9' in cols) and isvalid("ssh.4 ssh.8", md):
        md["ssh.9"] = md["ssh.4"] + md["ssh.8"]
    if (type == 'all' or 'ssh.10' in cols) and isvalid("ssh.9", md):
        md["ssh.10"] = md["ssh.9"] / 2

    if (type == 'all' or 'sci.1' in cols) and isvalid("81 82", md):
        md["sci.1"] = md["81"] + md["82"]
    if (type == 'all' or 'sci.2' in cols) and isvalid("83 84", md):
        md["sci.2"] = md["83"] + md["84"]
    if (type == 'all' or 'sci.3' in cols) and isvalid("85 86 87 88 89 90", md):
        md["sci.3"] = md["85"] + md["86"] + md["87"] + md["88"] + md["89"] + md[
            "90"]
    if (type == 'all' or 'sci.4' in cols) and isvalid("sci.2 sci.3", md):
        md["sci.4"] = md["sci.2"] + md["sci.3"]
    if (type == 'all' or 'sci.5' in cols) and isvalid("91 92", md):
        md["sci.5"] = md["91"] + md["92"]
    if (type == 'all' or 'sci.6' in cols) and isvalid("93 94", md):
        md["sci.6"] = md["93"] + md["94"]
    if (type == 'all' or 'sci.7' in cols) and isvalid("95 96 97 98 99 100", md):
        md["sci.7"] = md["95"] + md["96"] + md["97"] + md["98"] + md["99"] + md[
            "100"]
    if (type == 'all' or 'sci.8' in cols) and isvalid("sci.6 sci.7", md):
        md["sci.8"] = md["sci.6"] + md["sci.7"]
    if (type == 'all' or 'sci.9' in cols) and isvalid("sci.4 sci.8", md):
        md["sci.9"] = md["sci.4"] + md["sci.8"]
    if (type == 'all' or 'sci.10' in cols) and isvalid("sci.9", md):
        md["sci.10"] = md["sci.9"] / 2

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
