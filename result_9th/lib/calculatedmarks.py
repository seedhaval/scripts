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
