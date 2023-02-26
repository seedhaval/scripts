def isvalid(txt, md):
    for idx in txt.strip().split():
        if idx not in md:
            return False
    return True


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


